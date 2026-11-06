"""Minimal SOCKS5 server for the dashboard browser on the DE server.

Runs on this PC and listens on 127.0.0.1 only. The server reaches it through a reverse SSH tunnel
(see start_egress.cmd), so the dashboard browser leaves to the internet from this PC's home IP.

* CONNECT only, no authentication (loopback only, the tunnel is the only way in);
* destinations that are not public internet addresses (LAN, loopback, link-local) are refused,
  so the server can never be used to reach this home network;
* hostnames are resolved here, on the PC.
"""
import asyncio
import ipaddress
import socket
import struct
import sys

HOST, PORT = "127.0.0.1", int(sys.argv[1]) if len(sys.argv) > 1 else 1081
MAX_CONNECTIONS = 300
IDLE_SECONDS = 600
active = 0


async def pipe(reader, writer):
    try:
        while True:
            data = await asyncio.wait_for(reader.read(65536), timeout=IDLE_SECONDS)
            if not data:
                break
            writer.write(data)
            await writer.drain()
    except (asyncio.TimeoutError, ConnectionError, OSError):
        pass
    finally:
        try:
            writer.close()
        except OSError:
            pass


async def reply(writer, code):
    writer.write(bytes([5, code, 0, 1]) + b"\x00\x00\x00\x00\x00\x00")
    await writer.drain()


async def handle(reader, writer):
    global active
    if active >= MAX_CONNECTIONS:
        writer.close()
        return
    active += 1
    try:
        head = await asyncio.wait_for(reader.readexactly(2), timeout=10)
        if head[0] != 5:
            return
        await reader.readexactly(head[1])
        writer.write(b"\x05\x00")                                  # no authentication
        await writer.drain()
        ver, cmd, _, atyp = await asyncio.wait_for(reader.readexactly(4), timeout=10)
        if cmd != 1:
            await reply(writer, 7)
            return
        if atyp == 1:
            host = socket.inet_ntoa(await reader.readexactly(4))
        elif atyp == 3:
            host = (await reader.readexactly((await reader.readexactly(1))[0])).decode("ascii", "replace")
        elif atyp == 4:
            host = socket.inet_ntop(socket.AF_INET6, await reader.readexactly(16))
        else:
            await reply(writer, 8)
            return
        port = struct.unpack(">H", await reader.readexactly(2))[0]
        loop = asyncio.get_running_loop()
        try:
            infos = await asyncio.wait_for(loop.getaddrinfo(host, port, type=socket.SOCK_STREAM), timeout=10)
        except (OSError, asyncio.TimeoutError):
            await reply(writer, 4)
            return
        public = [i for i in infos if ipaddress.ip_address(i[4][0]).is_global]
        if not public:
            await reply(writer, 2)                                  # not allowed: not a public address
            return
        remote = None
        for info in public:
            try:
                remote = await asyncio.wait_for(asyncio.open_connection(info[4][0], port), timeout=15)
                break
            except (OSError, asyncio.TimeoutError):
                continue
        if remote is None:
            await reply(writer, 5)
            return
        await reply(writer, 0)
        r_reader, r_writer = remote
        await asyncio.gather(pipe(reader, r_writer), pipe(r_reader, writer))
    except (asyncio.IncompleteReadError, asyncio.TimeoutError, ConnectionError, OSError):
        pass
    finally:
        active -= 1
        try:
            writer.close()
        except OSError:
            pass


async def main():
    server = await asyncio.start_server(handle, HOST, PORT)
    print(f"socks5 on {HOST}:{PORT}", flush=True)
    async with server:
        await server.serve_forever()


asyncio.run(main())

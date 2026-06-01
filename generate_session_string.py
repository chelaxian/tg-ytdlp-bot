#!/usr/bin/env python3
"""
Session string generator for Channel Guard.

Creates a user Telegram session needed for reading channel admin logs.

Usage:
  python generate_session_string.py                    # Interactive (asks API keys)
  python generate_session_string.py --api-id=XXX --api-hash=XXX  # With custom keys
  python generate_session_string.py --phone            # Phone number method

IMPORTANT: Public API_IDs (like 6119513) are often blocked by Telegram.
Get your own at https://my.telegram.org -> API Development Tools
"""

import sys
import asyncio
import datetime
import base64
from pyrogram import Client, raw, types, handlers


PUBLIC_API_IDS = {
    6113, 14184, 2040, 2834, 714290, 48536, 6119513, 1084092,
    24945, 12345678, 17349, 17079118,
}


def _get_api_credentials():
    try:
        from CONFIG.config import Config
        cfg_id = getattr(Config, "API_ID", None)
        cfg_hash = getattr(Config, "API_HASH", None)
    except Exception:
        cfg_id, cfg_hash = None, None

    cli_id, cli_hash = None, None
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        a = args[i]
        if a.startswith("--api-id="):
            cli_id = int(a.split("=", 1)[1])
        elif a.startswith("--api-hash="):
            cli_hash = a.split("=", 1)[1]
        elif a == "--api-id" and i + 1 < len(args):
            cli_id = int(args[i + 1])
            i += 1
        elif a == "--api-hash" and i + 1 < len(args):
            cli_hash = args[i + 1]
            i += 1
        i += 1

    api_id = cli_id or cfg_id
    api_hash = cli_hash or cfg_hash

    if api_id and api_hash:
        if api_id in PUBLIC_API_IDS:
            print(f"WARNING: API_ID {api_id} is a known public key.")
            print("Telegram often blocks auth with public API keys.")
            print()
            print("Get your own at: https://my.telegram.org")
            print("  -> API Development Tools -> Create new application")
            print()
            choice = input("Continue anyway? (y/N): ").strip().lower()
            if choice != "y":
                print("Aborted.")
                return None, None
        return api_id, api_hash

    print("API credentials not found.")
    print("Get them at: https://my.telegram.org -> API Development Tools")
    print()
    api_id = int(input("Enter API_ID: ").strip())
    api_hash = input("Enter API_HASH: ").strip()
    return api_id, api_hash


def _print_qr_ascii(url: str):
    try:
        import qrcode
        qr = qrcode.QRCode(version=1)
        qr.add_data(url)
        qr.print_ascii(tty=True)
    except ImportError:
        print("QR URL (paste into any QR generator or open in browser):")
        print()
        print(f"  {url}")
        print()


async def _qr_login(client: Client):
    token = await client.invoke(
        raw.functions.auth.ExportLoginToken(
            api_id=client.api_id,
            api_hash=client.api_hash,
            except_ids=[],
        )
    )

    if isinstance(token, raw.types.auth.LoginToken):
        url = f"tg://login?token={base64.urlsafe_b64encode(token.token).decode()}"
        expires = token.expires - int(datetime.datetime.now().timestamp())

        print("Scan the QR code in Telegram:")
        print("  Settings -> Devices -> Link Desktop Device")
        print()
        _print_qr_ascii(url)
        print("Waiting for scan...")
        print()

        event = asyncio.Event()

        def _on_update(cl, update, users, chats):
            if isinstance(update, raw.types.UpdateLoginToken):
                event.set()

        handler = client.add_handler(
            handlers.RawUpdateHandler(_on_update)
        )

        await client.dispatcher.start()

        try:
            await asyncio.wait_for(event.wait(), timeout=expires)
        except asyncio.TimeoutError:
            print("QR expired, regenerating...")
            await _safe_dispatcher_stop(client)
            return await _qr_login(client)
        finally:
            try:
                client.remove_handler(*handler)
            except Exception:
                pass
            await _safe_dispatcher_stop(client)

        result = await client.invoke(
            raw.functions.auth.ExportLoginToken(
                api_id=client.api_id,
                api_hash=client.api_hash,
                except_ids=[],
            )
        )

        if isinstance(result, raw.types.auth.LoginTokenSuccess):
            user = types.User._parse(client, result.authorization.user)
            await client.storage.user_id(user.id)
            await client.storage.is_bot(False)
            print(f"Logged in as: {user.first_name} (ID: {user.id})")
            return user

        if isinstance(result, raw.types.auth.LoginTokenMigrateTo):
            await client.storage.dc_id(result.dc_id)
            client.session = await client.get_session(result.dc_id, export_authorization=False)
            result2 = await client.invoke(
                raw.functions.auth.ImportLoginToken(token=result.token)
            )
            if isinstance(result2, raw.types.auth.LoginTokenSuccess):
                user = types.User._parse(client, result2.authorization.user)
                await client.storage.user_id(user.id)
                await client.storage.is_bot(False)
                print(f"Logged in as: {user.first_name} (ID: {user.id})")
                return user

        raise TypeError(f"Unexpected login token response: {type(result).__name__}")

    raise TypeError(f"Unexpected token type: {type(token).__name__}")


async def _safe_dispatcher_stop(client: Client):
    try:
        await client.dispatcher.stop()
    except TypeError:
        try:
            await client.dispatcher.stop()
        except Exception:
            pass
    except Exception:
        pass


async def generate_session_string():
    api_id, api_hash = _get_api_credentials()
    if not api_id or not api_hash:
        return

    print()
    print("=" * 60)
    print("Session String Generator")
    print("=" * 60)
    print(f"API_ID: {api_id}")
    print(f"API_HASH: {api_hash[:10]}...")
    print()

    use_phone = "--phone" in sys.argv

    client = Client(
        name=":memory:",
        api_id=api_id,
        api_hash=api_hash,
        in_memory=True,
    )

    try:
        is_authorized = await client.connect()

        if is_authorized:
            print("Session already authorized.")
        elif use_phone:
            print("Method: Phone number")
            print()
            await client.authorize()
        else:
            print("Method: QR code")
            print()
            await _qr_login(client)

        client.me = await client.get_me()
        await client.initialize()

        session_string = await client.export_session_string()

        print()
        print("=" * 60)
        print("SUCCESS! Session String generated!")
        print("=" * 60)
        print()
        print("Add this to CONFIG/config.py:")
        print()
        print(f'    CHANNEL_GUARD_SESSION_STRING = "{session_string}"')
        print()
        print("=" * 60)
        print()
        print("WARNING:")
        print("  - Keep session string secret!")
        print("  - Do not publish it anywhere!")
        print("  - It grants full access to your account!")
        print()

        try:
            with open("channel_guard_session_string.txt", "w", encoding="utf-8") as f:
                f.write(f'CHANNEL_GUARD_SESSION_STRING = "{session_string}"\n')
            print("Saved to: channel_guard_session_string.txt")
            print("(delete this file after copying to config!)")
        except Exception as e:
            print(f"Could not save to file: {e}")

    except Exception as e:
        print()
        print("=" * 60)
        print(f"Error: {e}")
        print("=" * 60)
        print()
        if use_phone:
            print("If the code is not received, try QR code method instead:")
            print("  python generate_session_string.py")
        print()
    finally:
        try:
            await client.disconnect()
        except Exception:
            pass
        print("Client stopped.")


if __name__ == "__main__":
    print()
    try:
        asyncio.run(generate_session_string())
    except KeyboardInterrupt:
        print("\n\nInterrupted.")
    except Exception as e:
        print(f"\n\nFatal error: {e}")

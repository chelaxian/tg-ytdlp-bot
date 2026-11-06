Browser egress through this PC
==============================
Why: X and TikTok distrust the server's address (Oracle datacenter, Frankfurt) and ask for a phone
number / refuse the login. Through this PC the browser leaves from the address your own browser uses.

Use:   double-click start_egress.cmd   (keep the two minimized windows open)
       panel -> Browser tab -> switch on "Leave through my PC (home IP)" -> restart the browser
       log in to the services; cookies stay in the browser profile on the server
Stop:  stop_egress.cmd (the tunnel is only needed while you log in)

If the tunnel is down when the browser starts, it starts normally from the server address.

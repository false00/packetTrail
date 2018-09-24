#!/usr/bin/python3
#
# NAME - packetTrail.py
# Version 1.1
#
# SYNOPSIS
# python3 ./packetTrail.py 10.0.0.1 514
#
# DESCRIPTION
# Associates netflow data with process name and logs to syslog
#
# AUTHOR
# Juan Ortega
#
# HISTORY:
#
# Date(YYYY/MM/DD):     Version:        Modified By:    Description of Change:
# 2018-09-08             1.0            Juan Ortega     First Working Version of Script
# 2018-09-23             1.1            Juan Ortega     Added username and process id. Performance Improvements.

import socket
import psutil
import datetime
import logging
import sys
import time

#UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def main():

    global udp_ip
    global udp_port

    watchlist = {}
    while 1:
        time.sleep(.5)
        for i in psutil.net_connections(kind='inet4'):
            try:

                # Destination IP, if null skip
                try:
                    rip = str(i.raddr).split('\'')[1]
                except:
                    continue

                # Get PID
                pid = i.pid

                # Source Port
                sport = i.laddr.port

                if (sport, pid) not in watchlist.items():
                    watchlist[sport] = pid

                    # Destination Port
                    rport = str(i.raddr).split(',')[1].strip().strip(')').strip("port=")

                    # Get Source IP
                    sip = str(i.laddr).split('\'')[1]

                    # Get Username
                    username = psutil.Process(pid).username()
                    username = ''.join(username.split())

                    # Get Process Name Using PID
                    p = psutil.Process(pid)
                    process_name = p.name()
                    process_name = ''.join(process_name.split())

                    # Timestamp
                    event_time = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

                    # Local
                    local_ip = get_ip()
                    hostname = socket.gethostname()

                    log = (" username=" + str(username) + " process=" + str(process_name) + " pid=" + str(pid) + " sip=" + str(sip) + " sport=" + str(sport) + " rip=" + str(rip) + " rport=" + str(rport))
                    message = "<12>" + str(event_time) + " " + local_ip + " " + hostname + " " + str("packetTrail") + str(log)
                    logger.info(message)
                    sock.sendto(str.encode(message), (udp_ip, udp_port))

            except:
                break


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == "__main__":
    try:
        udp_ip = sys.argv[1]
        udp_port = int(sys.argv[2])
    except:
        print("===============packetTrail=============== \n"
              "Pass the IP you wish to send syslog traffic to.\n"
              "\n"
              "Usage: packetTrail syslogIP udpPort\n"
              "Example: packetTrail.exe 10.0.0.1 514")
        sys.exit(1)
    # Initialize Logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    hdlr = logging.FileHandler('trail.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    hdlr.setLevel(logging.INFO)
    logger.addHandler(hdlr)
    main()
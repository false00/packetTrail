#!/usr/bin/python3
#
# NAME - packetTrail.py
# Version 1.0
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

import socket
import psutil
import datetime
import logging
import sys
import time

#UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
    #Dictionary
    #SPORT:PROCESS - If Sport and Process combination are new; action.
    global udp_ip
    global udp_port

    watchlist = {}
    while 1:
        time.sleep(1)
        for i in psutil.net_connections(kind='inet4'):
            try:
                #Get Process Name Using PID
                p = psutil.Process(i.pid)
                process = p.name().split()[0]

                #Timestamp
                eventTime = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

                #Local
                localip = get_ip()
                hostname = socket.gethostname()

                #Source
                sip = str(i.laddr).split('\'')[1]
                sport = i.laddr.port

                #Destination
                try:
                    rip = str(i.raddr).split('\'')[1]
                except:
                    rip = 'null'
                    continue

                try:
                    rport = str(i.raddr).split(',')[1].strip().strip(')').strip("port=")
                except:
                    rport = 'null'
                    continue

                if (sport, process) not in watchlist.items():
                    watchlist[sport] = process
                    log = ("process=" + str(process) + " sip=" + str(sip) + " sport=" + str(sport) + " rip=" + str(rip) + " rport=" + str(rport))
                    message = "<12>" + str(eventTime) + " " + localip + " " + hostname + " " + str("packetTrail") + " " + str(log)
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
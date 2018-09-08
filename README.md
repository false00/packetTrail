# packetTrail

This program creates a record of every network connection on a system and generates a log that contains the process name that initiated the connection. This data has potential to assist incident responders and SOC teams in incident response or threat hunting.    
```
Log Sample:
syslog format = log_priority + utc_timestamp + host_ip + host_hostname + program_name + process + sip + sport + rip + rport
2018-09-08 04:27:19,768 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=firefox.exe sip=127.0.0.1 sport=50410 rip=127.0.0.1 rport=50411
2018-09-08 04:27:19,785 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=firefox.exe sip=127.0.0.1 sport=50399 rip=127.0.0.1 rport=50400
2018-09-08 04:27:19,795 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=firefox.exe sip=127.0.0.1 sport=50415 rip=127.0.0.1 rport=50416
2018-09-08 04:27:19,800 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=pycharm64.exe sip=127.0.0.1 sport=49161 rip=127.0.0.1 rport=49160
2018-09-08 04:27:19,800 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=chrome.exe sip=192.168.50.129 sport=50434 rip=172.217.5.195 rport=443
2018-09-08 04:27:19,805 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=firefox.exe sip=127.0.0.1 sport=50402 rip=127.0.0.1 rport=50401
2018-09-08 04:27:19,810 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=pycharm64.exe sip=127.0.0.1 sport=49162 rip=127.0.0.1 rport=49163
2018-09-08 04:27:19,815 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=firefox.exe sip=127.0.0.1 sport=50401 rip=127.0.0.1 rport=50402
2018-09-08 04:27:19,818 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=firefox.exe sip=127.0.0.1 sport=50411 rip=127.0.0.1 rport=50410
2018-09-08 04:27:19,820 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=pycharm64.exe sip=127.0.0.1 sport=49163 rip=127.0.0.1 rport=49162
2018-09-08 04:27:19,823 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=chrome.exe sip=192.168.50.129 sport=50433 rip=216.58.219.10 rport=443
2018-09-08 04:27:19,825 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=pycharm64.exe sip=127.0.0.1 sport=49160 rip=127.0.0.1 rport=49161
2018-09-08 04:27:19,828 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=firefox.exe sip=127.0.0.1 sport=50416 rip=127.0.0.1 rport=50415
2018-09-08 04:27:19,848 INFO <12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=firefox.exe sip=127.0.0.1 sport=50400 rip=127.0.0.1 rport=50399
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.  

### Prerequisites

Python
```
pip install psutil
```

### How to Run

Windows
```
Usage: packetTrail.exe syslog_ip syslog_udp_port
Example: packetTrail.exe 10.0.0.20 514
```

Python
```
Usage: packetTrail.exe syslog_ip syslog_udp_port
Example: packetTrail.exe 10.0.0.20 514
```

### How to Build Windows Binary 
If you're not comfortable running the provided Windows binary, you can build your own version using pyinstaller.

Python 3.6.4 Required
```
pyinstaller --onefile --hidden-import=queue packetTrail.py
```

## Built With

* [Pyinstaller](https://www.pyinstaller.org) - Library used to convert python script to windows binary 


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Juan Ortega** - *Initial work* - [falseShepherd](https://github.com/ucatech)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details




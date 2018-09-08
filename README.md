# packetTrail

This program creates a record of every network connection on a system and generates a log that contains the process name that initiated the connection. packetTrail supports forwarding these logs real time via syslog. 

packetTrail assists SOC/IR teams in incident response missions and threat hunting.    
```
Log Sample:
syslog format = log_priority + utc_timestamp + host_ip + host_hostname + program_name + process + sip + sport + rip + rport
<12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=chrome.exe sip=192.168.50.129 sport=50434 rip=172.217.5.195 rport=443
<12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=chrome.exe sip=192.168.50.129 sport=50433 rip=216.58.219.10 rport=443
<12>2018-09-08T11:27:19Z 192.168.50.129 juans-windowsvm packetTrail process=firefox.exe sip=127.0.0.1 sport=50400 rip=127.0.0.1 rport=50399
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.  

### Prerequisites

Python
```
pip install psutil
```

### Supported Operating Systems
```
Windows 7
Windows 10
macOS High Sierra 10.13.6
Ubuntu 16.04
```

### How to Run

Windows
```
Usage: packetTrail.exe syslog_ip syslog_udp_port
Example: packetTrail.exe 10.0.0.20 514
```

Python
```
Usage: packetTrail.py syslog_ip syslog_udp_port
Example: packetTrail.py 10.0.0.20 514
```

### How to Build Windows Binary 
If you're not comfortable running the provided Windows binary, you can build your own version using pyinstaller.
```
Requirements

Software:
Python 3.6.4 

Operating System:
Windows 7
```

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




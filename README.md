# packetTrail

This program creates a record of every network connection on a system and generates a log that contains the process name that initiated the connection. This gives attribution to which process generated what traffic. Thus, allowing an incident responder or SOC analyst visibility into the host. Use cases are endless, but the log data can be used for incident response missions or threat hunting. 

For example, if powershell.exe beacons out to an IP, dies, then that same IP is observed communicating with explorer.exe, this may be an indicator of malware injecting itself into another process. packetTrail would produce the data required to detect something like this. You could also create baselines using packetTrail and trigger on anomalies that don't match your baseline. It can be used many different ways. Currently it only supports forwarding logs via syslog and writing to a local file. I'm working on adding elasticsearch support soon. If you find any bugs let me know. I'd appreciate it. 
   
```
Log Sample:
syslog format = log_priority + utc_timestamp + host_ip + host_hostname + program_name + process + sip + sport + rip + rport
<12>2018-09-08T11:25:19Z 192.168.50.129 juans-windowsvm packetTrail process=powershell.exe sip=192.168.50.129 sport=50434 rip=192.168.50.134 rport=80
<12>2018-09-08T11:27:56Z 192.168.50.129 juans-windowsvm packetTrail process=explorer.exe sip=192.168.50.129 sport=50433 rip=192.168.50.134 rport=80
<12>2018-09-08T11:28:19Z 192.168.50.129 juans-windowsvm packetTrail process=notepad.exe sip=192.168.50.129 sport=50400 rip=192.168.50.134 rport=80
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.  

### Prerequisites

Windows
```
vc_redist.x64.exe - https://www.microsoft.com/en-US/download/details.aspx?id=52685
```

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

### How to Install as a Service

Windows
```
sc create packetTrail binPath= "C:\packetTrail-master\packetTrail-master\packetTrail.exe 10.0.0.20 514"
```

### How to Build Windows Binary 
If you're not comfortable running the provided Windows binary, you can build your own version using pyinstaller.

Requirements
```
Software:
Python 3.6.4 

Operating System:
Windows 7
```

Build
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




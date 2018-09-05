# trafficBeat

trafficBeat allows you to mirror network traffic from your Windows or Mac operating system to any IP on the same local subnet. It accomplishes this by editing the destination MAC of each packet and replacing it with the provided IP's MAC. The edited packets are sent over layer 2 and reach the traget system. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine

### Prerequisites

Requirements for using the .py version of the script. Not Required for the windows binary.

```
Windows 
WinPcap - https://www.winpcap.org/
```

```
Python
pip install scapy
```

### How to Use

```
Windows
trafficBeat.exe 10.0.0.20
```

```
Python/Mac
trafficBeat.py 10.0.0.20
```

### How to Build Windows Binary 
If you're not comfortable running the provided Windows binary, you can build your own version using pyinstaller.

```
#Python 3.6.4 Required
pyinstaller --onefile --hidden-import=queue trafficBeat.py
```

## Built With

* [Pyinstaller](https://www.pyinstaller.org) - Library used to convert python script to windows binary 


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Juan Ortega** - *Initial work* - [falseShepherd](https://github.com/ucatech)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



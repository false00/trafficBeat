# trafficBeat

trafficBeat allows you to mirror traffic from your Windows or Mac operating system to any IP on the same local subnet. It accomplishes this by editing the destination MAC of each packet with a new destination, and sending the edited packets over layer 2. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine

### Prerequisites

Requirements for using the .py version of the script. Not Required for the windows binary.

```
pip install scapy
```

### Installing

```
Windows
trafficBeat.exe 10.0.0.20
```

```
Python/Mac
trafficBeat.py 10.0.0.20
```

## Built With

* [Pyinstaller](https://www.pyinstaller.org) - Library used to convert python script to windows binary 


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Juan Ortega** - *Initial work* - [falseShepherd](https://github.com/ucatech)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



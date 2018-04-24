# Clouding Things Python MQTT agent

This python module is used to create python clients connected to Clouding Things platform.

## Getting Started

### Prerequisites

The module require paho-mqtt:

```
pip install paho-mqtt
```

### Installing

Simply execute:

```
python setup.py install
```

## Running example

### Update Clouding Things parameters

In example folder, open simple_client.py file and update config:

```
gtw_config={
   'client': 'demo',
   'serial': 'demo',
   'credential_file': 'path_to_crt_file.crt',
   'broker': '5.135.83.28',
   'transport': 'ssl',
   'port': 8883,
   'auto_reconnect': True
}
```

Parameters:
* client: your client name
* serial: your gateway serial number
* credential_file: the path to the crt file created for the gateway

### Run example

In examples folder, execute the following command:

```
python simple_client.py
```

## Author

* Jean Poma - Initial development

## License

This project is licensed under the MIT License - see the LICENSE file for details

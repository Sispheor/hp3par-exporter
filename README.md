# HP 3PAR Prometheus Exporter

Blackbox likes exporter used to exports overall system capacity of a 3PAR storage backend to Prometheus.

Example of metrics exported
```
# HELP hp3par_totalCapacityMiB Total system capacity in MiB
# TYPE hp3par_totalCapacityMiB gauge
hp3par_totalCapacityMiB{hp3par_name="sante5",id="29721"} 40255488.0
# HELP hp3par_allocatedCapacityMiB Total allowed capacity in MiB
# TYPE hp3par_allocatedCapacityMiB gauge
hp3par_allocatedCapacityMiB{hp3par_name="sante5",id="29721"} 7336960.0
# HELP hp3par_freeCapacityMiB Total free capacity in MiB
# TYPE hp3par_freeCapacityMiB gauge
hp3par_freeCapacityMiB{hp3par_name="sante5",id="29721"} 32918528.0
# HELP hp3par_failedCapacityMiB Total failed capacity in MiB
# TYPE hp3par_failedCapacityMiB gauge
hp3par_failedCapacityMiB{hp3par_name="sante5",id="29721"} 0.0
```


### Manual installation

Can be installed locally with `setup.py`
```
sudo python setup.py install
```

### Usage

Usage and command line flags:
```
usage: hp3par-exporter [-h] [--address ADDRESS] [--port PORT]
                       [--endpoint ENDPOINT] [--config CONFIG]

optional arguments:
  -h, --help           show this help message and exit
  --address ADDRESS    address to serve on
  --port PORT          port to bind
  --endpoint ENDPOINT  endpoint where metrics will be published
  --config CONFIG      path to the YAML configuration file
```

E.g:
```
hp3par-exporter --config /path/to/hp3par_config.yml
```

### Config

The configuration file, passed as argument to the program, contains a list (in YAML) of HP 3PAR API you want to query and expose.
```yml
- hp3par_api_url: "https://192.168.1.20:8080/api/v1"
  hp3par_username: "hp3par_admin"
  hp3par_password: "hp3par_password"

- hp3par_api_url: "https://192.168.1.30:8080/api/v1"
  hp3par_username: "user"
  hp3par_password: "password"
```

Each 3PAR will be differentiated by their name and ID added in the label of each metrics. Example:
```
hp3par_totalCapacityMiB{hp3par_name="my3par_1",id="12345"} 24058802.0
hp3par_totalCapacityMiB{hp3par_name="my3par_2",id="67891"} 40255488.0
```

### Docker

Build the image
```
docker build --rm -t hp3par-exporter .
```

To run the container
```
docker run -it -p 8080:8080 -v $PWD/hp3par_config.yml:/hp3par_config.yml hp3par-exporter
```

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


## Installation

### Manual installation

Can be installed locally with `setup.py`
```
sudo python setup.py install
```

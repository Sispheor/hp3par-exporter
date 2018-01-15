from prometheus_client import Gauge
from prometheus_client import REGISTRY

registry = REGISTRY

gauge_hp3par_total_capacity_mib = Gauge('hp3par_totalCapacityMiB', 'Total system capacity in MiB', ["id", "hp3par_name"])
gauge_hp3par_allocated_capacity_mib = Gauge('hp3par_allocatedCapacityMiB',
                                            'Total allowed capacity in MiB', ["id", "hp3par_name"])
gauge_hp3par_free_capacity_mib = Gauge('hp3par_freeCapacityMiB',
                                       'Total free capacity in MiB', ["id", "hp3par_name"])
gauge_hp3par_failed_capacity_mib = Gauge('hp3par_failedCapacityMiB',
                                         'Total failed capacity in MiB', ["id", "hp3par_name"])



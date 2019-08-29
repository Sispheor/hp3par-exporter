from http.server import BaseHTTPRequestHandler

from . import prometheus_metrics

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from hpe3parclient.client import HPE3ParClient
from hpe3parclient.exceptions import HTTPUnauthorized
from prometheus_client import generate_latest


class RequestHandler(BaseHTTPRequestHandler):
    """
    Endpoint handler
    """
    def return_error(self):
        self.send_response(500)
        self.end_headers()

    def do_GET(self):
        """
        Process GET request

        :return: Response with Prometheus metrics
        """

        # get parameters from the URL
        url = urlparse(self.path)

        if url.path == self.server.endpoint:
            if self.server.yaml_config:
                for hp3par_config in self.server.yaml_config:
                    # do a call to the 3PAR backend
                    hp3parclient = HPE3ParClient(hp3par_config["hp3par_api_url"], secure=False)
                    try:
                        hp3parclient.login(str(hp3par_config["hp3par_username"]),
                                           str(hp3par_config["hp3par_password"]))
                        print("Login worked!")

                    except HTTPUnauthorized as ex:
                        print(ex)

                    system_info = hp3parclient.getStorageSystemInfo()
                    hp3parclient.logout()
                    prometheus_metrics.gauge_hp3par_total_capacity_mib \
                        .labels(id=system_info["id"],
                                hp3par_name=system_info["name"]) \
                        .set(system_info["totalCapacityMiB"])

                    prometheus_metrics.gauge_hp3par_allocated_capacity_mib \
                        .labels(id=system_info["id"],
                                hp3par_name=system_info["name"]) \
                        .set(system_info["allocatedCapacityMiB"])

                    prometheus_metrics.gauge_hp3par_free_capacity_mib \
                        .labels(id=system_info["id"],
                                hp3par_name=system_info["name"]) \
                        .set(system_info["freeCapacityMiB"])

                    prometheus_metrics.gauge_hp3par_failed_capacity_mib \
                        .labels(id=system_info["id"],
                                hp3par_name=system_info["name"]) \
                        .set(system_info["failedCapacityMiB"])

                # generate and publish metrics
                metrics = generate_latest(prometheus_metrics.registry)
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(metrics)

        elif url.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""<html>
            <head><title>HP 3PAR Exporter</title></head>
            <body>
            <h1>HP iLO Exporter</h1>
            <p>Visit <a href="/metrics">Metrics</a> to use.</p>
            </body>
            </html>""")

        else:
            self.send_response(404)
            self.end_headers()

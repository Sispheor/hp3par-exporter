import os

import yaml

from .ForkingHTTPServer import ForkingHTTPServer
from .RequestHandler import RequestHandler
from .Utils import *


class HP3PARExporterServer(object):
    """
    Basic server implementation that exposes metrics to Prometheus
    """

    def __init__(self, address='0.0.0.0', port=8080, endpoint="/metrics", config="hp3par_config.yml"):
        self._address = address
        self._port = port
        self.endpoint = endpoint
        self.config = config
        self.yaml_config = None

    def print_info(self):
        print_err("Starting exporter on: http://{}:{}{}".format(self._address, self._port, self.endpoint))
        print_err("Configuration file: %s" % self.config)
        print_err("Press Ctrl+C to quit")

    def run(self):

        # load yaml config
        if os.path.isfile(self.config):
            with open(self.config, "r") as f:
                self.yaml_config = yaml.load(f)

        server = ForkingHTTPServer((self._address, self._port), RequestHandler)
        server.endpoint = self.endpoint
        if self.yaml_config is not None:
            server.yaml_config = self.yaml_config
        else:
            print("No configuration file provided")
            exit(1)

        self.print_info()
        try:
            while True:
                server.handle_request()
        except KeyboardInterrupt:
            print_err("Killing exporter")
            server.server_close()

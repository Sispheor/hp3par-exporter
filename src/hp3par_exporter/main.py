"""
Entrypoint for the application
"""

import argparse

from HP3PARExporterServer import HP3PARExporterServer


def main():
    parser = argparse.ArgumentParser(description='Exports HP 3PAR overall system capacity to Prometheus')

    parser.add_argument('--address', type=str, dest='address', default='0.0.0.0', help='address to serve on')
    parser.add_argument('--port', type=int, dest='port', default='8080', help='port to bind')
    parser.add_argument('--endpoint', type=str, dest='endpoint', default='/metrics',
                        help='endpoint where metrics will be published')
    parser.add_argument('--config', type=str, dest='config', default='hp3par_config.yml')

    args = parser.parse_args()

    exporter = HP3PARExporterServer(**vars(args))
    exporter.run()


if __name__ == '__main__':
    main()

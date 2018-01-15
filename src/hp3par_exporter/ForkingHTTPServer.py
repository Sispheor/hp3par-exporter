from http.server import HTTPServer
from socketserver import ForkingMixIn


class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    max_children = 30
    timeout = 30

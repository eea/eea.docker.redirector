import BaseHTTPServer
import SocketServer
import os, sys

__version__ = "0.6"

__all__ = ["RedirectRequestHandler"]

PORT = 8080

class RedirectRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    server_version = "RedirectHTTP/" + __version__

    def send_redirect(self):
        self.send_response(301)
        self.send_header("Location", REDIRECT + ("/" if APPENDPATH is None else self.path))
        self.end_headers()
        return None

    def do_GET(self):
        self.send_redirect()

    def do_POST(self):
        self.send_redirect()

def run():
    Handler = RedirectRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "Serving at port", PORT
    httpd.serve_forever()

#def test(HandlerClass = RedirectRequestHandler,
#         ServerClass = BaseHTTPServer.HTTPServer):
#    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    PORT = int(os.getenv("PORT", "8080"))
    REDIRECT = os.getenv("REDIRECT")
    if REDIRECT is None:
        print "REDIRECT environment variable is not specified"
        sys.exit(1)
    while REDIRECT.endswith("/"):
        REDIRECT = REDIRECT[:-1]
    APPENDPATH = os.getenv("APPENDPATH")
    print "Redirecting to:", REDIRECT
    run()


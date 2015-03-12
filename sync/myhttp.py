# Define a simple webserver .
# Answers "OK" on "/" on port 80

from circuits.web import Server, Controller

class Root(Controller):

    def index(self):
        """Index Request Handler
        Controller(s) expose implicitly methods as request handlers.
        Request Handlers can still be customized by using the ``@expose``
        decorator. For example exposing as a different path.
        """
        return "OK"

def register_webserver(ip, port):
    webserver = Server((ip, port))
    Root().register(webserver)
    return webserver  

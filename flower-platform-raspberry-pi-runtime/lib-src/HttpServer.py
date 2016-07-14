import time
import BaseHTTPServer
import threading

"""
documentation of HTttpServer component
"""
class HttpServer:

    """    
    documentation of onCommandReceived handler
    """    
    onCommandReceived = None
    
    port = 8080
  
    """    
    documentation of setup method
    """ 
    def setup(self) :
      self.server = BaseHTTPServer.HTTPServer(('', self.port), HttpRequestHandler)
      self.server.onCommandReceived = self.onCommandReceived
      thread = threading.Thread(target = self.server.serve_forever)
      thread.daemon = True
      thread.start()

    def loop(self) :
      return

    def stop(self) :
      self.server.shutdown()
      self.server.server_close()

class HttpRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
      if self.server.onCommandReceived is None:
          return
      event = HttpCommandEvent()
      event.url = self.path[1:]
      event.client = self
      self.server.onCommandReceived(event)

class HttpCommandEvent:

    url = None

    client = None
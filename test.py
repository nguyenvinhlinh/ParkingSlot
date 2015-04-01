import signal, sys, ssl, logging
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
from optparse import OptionParser 

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)



class SimpleChat(WebSocket):
    
    def handleMessage(self):
        if self.data is None:
            self.data = ''
      
        for client in self.server.connections.itervalues():
            if client != self:
                try:
                    client.sendMessage(str(self.address[0]) + ' - ' + str(self.data))
                except Exception as n:
                    print n
            

    def handleConnected(self):
        print self.address, 'connected'
        for client in self.server.connections.itervalues():
            if client != self:
                try:
                    client.sendMessage(str(self.address[0]) + ' - connected')
                except Exception as n:
                    print n

    def handleClose(self):
        print self.address, 'closed'
        for client in self.server.connections.itervalues():
            if client != self:
                try:
                    client.sendMessage(str(self.address[0]) + ' - disconnected')
                except Exception as n:
                    print n

    def main():
        print "Hello"

if __name__ == "__main__":
    cls = SimpleChat
    server = SimpleWebSocketServer("localhost", 8000, cls)

    def close_sig_handler(signal, frame):
        server.close()
        sys.exit()

    signal.signal(signal.SIGINT, close_sig_handler)
    server.serveforever()
    print "hello"
    
    
    




                    

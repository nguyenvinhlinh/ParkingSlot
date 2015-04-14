import signal, sys, ssl, logging,thread, range2
from SimpleWebSocketServer import SimpleWebSocketServer
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

class ParkingSlot(WebSocket):
    def handleMessage(self):
        if self.data is None:
            self.data = ''
        try:
            self.sendMessage('slot1:'+ str(range2.Output[0])+',slot2:'+ str(range2.Output[1])+',slot3:'+str(range2.Output[2])+',slot4:'+str(range2.Output[3])) 
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


if __name__ == "__main__":
    try:
            thread.start_new_thread(range2.checkSensor, ())
    except:
        print 'unable to start new thread for sensor checker'
    cls = ParkingSlot
    server = SimpleWebSocketServer("localhost", 8000, cls)

    def close_sig_handler(signal, frame):
        server.close()
        sys.exit()
    signal.signal(signal.SIGINT, close_sig_handler)
    server.serveforever()

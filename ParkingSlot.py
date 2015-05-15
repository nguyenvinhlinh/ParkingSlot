import signal, sys, thread
import range2 as SocketSensor
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class ParkingSlot(WebSocket):
    def handleMessage(self):
        if self.data is None:
            self.data = ''
        try:
            self.sendMessage('slot1:'+ str(SocketSensor.Output[0])+',slot2:'+ str(SocketSensor.Output[1])+',slot3:'+str(SocketSensor.Output[2])+',slot4:'+str(SocketSensor.Output[3])) 
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
        thread.start_new_thread(SocketSensor.checkSensor, ()) 
    except Exception as n:
        print 'unable to start new thread for sensor checker'
        print n
    cls = ParkingSlot
    server = SimpleWebSocketServer("172.16.120.57", 8530, cls)

    def close_sig_handler(signal, frame):
        server.close()
        sys.exit()
    signal.signal(signal.SIGINT, close_sig_handler)
    server.serveforever()

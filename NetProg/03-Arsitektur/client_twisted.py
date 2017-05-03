from twisted.internet import stdio, reactor, protocol

class DataForwardingProtocol(protocol.Protocol):
    def __init__(self):
        self.output = None

    def dataReceived(self, data):
        if self.output:
            self.output.write(data)

class StdioProxyProtocol(DataForwardingProtocol):
    def connectionMade(self):
        inputForwarder = DataForwardingProtocol()
        inputForwarder.output = self.transport
        stdioWrapper = stdio.StandardIO(inputForwarder)
        self.output = stdioWrapper

        print "Connected to server"

class StdioProxyFactory(protocol.ClientFactory):
    protocol = StdioProxyProtocol


def main():
    reactor.connectTCP("localhost", 8000, StdioProxyFactory())

    reactor.run()

if __name__ == '__main__':
    main()
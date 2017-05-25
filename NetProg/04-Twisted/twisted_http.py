from twisted.web import resource, server
from twisted.internet import reactor

# Protocol untuk handle HTTP
class Home(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        return "Hello World"

    def render_POST(self, request):
        return "Anda mengirimkan : " + str(request.args)


# Factory
site = server.Site(Home())

# Reactor
reactor.listenTCP(8888, site)
reactor.run()

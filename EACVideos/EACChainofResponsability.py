#Emiliano Aguilar Cerna GITI9072
class Handler: #abstrac handler
    """Abstracc handler"""
    def __init__(self, successor):
        self._successor = successor
        #Define who is the next headler

    def handle(self, request):
        handled = self._handle(request) #if hadled, stop here

        #otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): #Inherist from the abstract handler
    """Concrete Handler 1"""
    def _handle(self, request):
        if 0 < request <= 10: #provide a condition for handling
            print("Request{} handled in handler 1 ".format(request))
            return True #indicates that the has been handler

class DefaultHandler(Handler): #inherist from the abstrac handler
    """Default handler"""

    def _handle(self, request):
        """If there is no handler avilable"""
        #no conditional cheking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True #indicates  that the request has been handler

class Client: #using handler
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))
        #create handlers and use them in a sequence you want
        #Note that the default  handler has no successor

    def delegate(self, requests): #Send your requests one at a time for handler has no successor
        for request in requests:
            self.handler.handle(request)

#create Client
c = Client()
#Create request
requests = [2, 5, 30]
#Send the request
c.delegate(requests)
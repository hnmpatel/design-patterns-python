from abc import ABCMeta, abstractmethod
from queue import Queue


class AbstractAuthentication(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.next_handler = None
        
    def set_next(self, handler):
        self.next_handler = handler
        
    def run(self, request):
        self.authenticate(request)
        if not request.get("is_authenticated"):
            if self.next_handler:
                self.next_handler.run(request)
            else:
                print("Request is not authenticated")
        
    @abstractmethod
    def authenticate(self, request):
        pass

class BaseAuthentication(AbstractAuthentication):
    def authenticate(self, request):
        if "username" in request and "password" in  request:
            print("User is authenticated using basic authentication")
            request["is_authenticated"] = True
            

class SessionAuthentication(AbstractAuthentication):
    def authenticate(self, request):
        if "session" in  request:
            print("User is authenticated using session authentication")
            request["is_authenticated"] = True

class TokenAuthentication(AbstractAuthentication):
    def authenticate(self, request):
        if "token" in  request:
            print("User is authenticated using token authentication")
            request["is_authenticated"] = True

authentication_chain = BaseAuthentication()
session_authentication = SessionAuthentication()
token_authentication = TokenAuthentication()
authentication_chain.set_next(session_authentication)
session_authentication.set_next(token_authentication)

request1 = {
    "username": "test",
    "password": "test"
}

authentication_chain.run(request1)

request2 = {
    "session": "test"
}

authentication_chain.run(request2)

request3 = {
    "token": "test"
}

authentication_chain.run(request3)

authentication_chain.run({})

from abc import ABCMeta, abstractmethod
from queue import Queue


class Handler(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.next_handler = None
        
    def set_next(self, handler):
        self.next_handler = handler
        
    def run(self, request):
        self.handle(request)
        if self.next_handler:
            self.next_handler.run(request)
        
    @abstractmethod
    def handle(self, request):
        pass

class FileHandler(Handler):
    def handle(self, request):
        with open("log.txt", "a") as f:
            f.write(f"{request}\n")
            

class DatabaseHandler(Handler):
    def handle(self, request):
        print("Getting database connection")
        print(f"INSERT INTO requests (request) VALUES ('{request}')")
        print("closing connection")

class EmailHandler(Handler):
    def handle(self, request):
        print(f"Sending Email for request: {request}")
        
class DefaultHandler(Handler):
    def handle(self, request):
        print("There is no handler for this request")


file_handler = FileHandler()
db_handler = DatabaseHandler()
email_handler = EmailHandler()
file_handler.set_next(db_handler)
db_handler.set_next(email_handler)

request = "This is a request"
file_handler.run(request)

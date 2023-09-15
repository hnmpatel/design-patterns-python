'''
Memento Design pattern
Required Clasess
- Originator - 
- Memento
- CareTaker
'''
import copy

class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f'{self.name} - {self.age}'


class Memento:
    def __init__(self, state):
        self.state = state

class Originator:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def get_memento(self):
        return Memento(self.state)

    def restore_memento(self, memento):
        self.state = memento.state

class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]

def main():
    originator = Originator()
    caretaker = Caretaker()

    user = User('hardik', 20)

    originator.set_state(copy.deepcopy(user))
    memento = originator.get_memento()
    caretaker.add_memento(memento)

    user.age = 33
    originator.set_state(copy.deepcopy(user))
    print("Current state:", originator.state)

    originator.restore_memento(caretaker.get_memento(0))
    print("Current state:", originator.state)

main()
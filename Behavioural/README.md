# ðŸ§  Behavioural Design Patterns

<p align="center">
  <img src="https://images.unsplash.com/photo-1542831371-29b0f74f9713?q=80&w=2000&auto=format&fit=crop" alt="Behavioural Design Patterns Banner" width="100%" style="border-radius:15px;"/>
</p>

<p align="center">
  <b>Behavioural Design Patterns</b> are concerned with algorithms and the assignment of responsibilities between objects. They not only describe patterns of objects or classes but also the patterns of communication between them.
</p>

---

## ðŸ“– Overview

While creational patterns deal with object creation and structural patterns deal with object composition, **behavioural patterns** focus on how objects distribute work and communicate with each other. They help you define clear communication channels and abstract the flow of control.

This repository contains the following behavioural design patterns implemented in **Python**:

| Pattern | Description | Implementation |
| :--- | :--- | :--- |
| **ðŸ”— Chain of Responsibility** | Passes a request along a chain of handlers until one of them handles it. | [chainofresponsibilty.py](./chainofresponsibilty.py) |
| **ðŸ•¹ï¸ Command** | Turns a request into a stand-alone object containing all information about the request. | [Command.py](./Command.py) |
| **ðŸ”„ Iterator** | Lets you traverse elements of a collection without exposing its underlying representation. | [Iterator.py](./Iterator.py) |
| **ðŸ¤ Mediator** | Restricts direct communications between objects, forcing them to collaborate via a mediator. | [Mediator.py](./Mediator.py) |
| **ðŸ’¾ Memento** | Lets you save and restore the previous state of an object without revealing its implementation. | [Momento.py](./Momento.py) |
| **ðŸ“¡ Observer** | Defines a subscription mechanism to notify multiple objects about any events that happen. | [Observer.py](./Observer.py) |
| **ðŸš¦ State** | Lets an object alter its behavior when its internal state changes. | [State.py](./State.py) |
| **â™Ÿï¸ Strategy** | Defines a family of algorithms, encapsulates each one, and makes them interchangeable. | [Startegy.py](./Startegy.py) |
| **ðŸ“‹ Template Method** | Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps. | [Template.py](./Template.py) |
| **ðŸš¶ Visitor** | Lets you separate algorithms from the objects on which they operate. | [Visitor.py](./Visitor.py) |

---

## ðŸ› ï¸ Deep Dive into Patterns (UML Diagrams)

### 1. Observer Pattern (Observer.py)
Allows an object (subject) to publish changes to its state so other objects (observers) can react to it.
`mermaid
classDiagram
    class Subject {
        <<interface>>
        +attach(Observer)
        +detach(Observer)
        +notify()
    }
    class ConcreteSubject {
        -state
        +getState()
        +setState()
    }
    class Observer {
        <<interface>>
        +update()
    }
    class ConcreteObserver {
        -state
        +update()
    }

    Subject <|.. ConcreteSubject
    Observer <|.. ConcreteObserver
    Subject o--> Observer : notifies
`

### 2. Strategy Pattern (Startegy.py)
Extracts varying algorithms into separate classes (strategies), allowing the context to switch between them dynamically.
`mermaid
classDiagram
    class Context {
        -strategy: Strategy
        +setStrategy(Strategy)
        +executeStrategy()
    }
    class Strategy {
        <<interface>>
        +execute()
    }
    class ConcreteStrategyA {
        +execute()
    }
    class ConcreteStrategyB {
        +execute()
    }

    Context o--> Strategy : uses
    Strategy <|.. ConcreteStrategyA
    Strategy <|.. ConcreteStrategyB
`

### 3. Command Pattern (Command.py)
Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
`mermaid
classDiagram
    class Invoker {
        -command: Command
        +setCommand(Command)
        +executeCommand()
    }
    class Command {
        <<interface>>
        +execute()
    }
    class ConcreteCommand {
        -receiver: Receiver
        +execute()
    }
    class Receiver {
        +action()
    }

    Invoker o--> Command
    Command <|.. ConcreteCommand
    ConcreteCommand --> Receiver : calls
`

---

## ðŸš€ How to Run

Each file is a standalone Python script demonstrating the pattern. You can run them individually from your terminal:

`ash
python Observer.py
python Startegy.py
python chainofresponsibilty.py
# etc.
`

## ðŸ¤ Contributing
Contributions are always welcome! If you have any improvements or want to add more examples in other languages, feel free to open a Pull Request.


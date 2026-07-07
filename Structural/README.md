# ??? Structural Design Patterns

<p align="center">
  <img src="https://images.unsplash.com/photo-1605379399642-870262d3d051?q=80&w=2000&auto=format&fit=crop" alt="Structural Design Patterns Banner" width="100%" style="border-radius:15px;"/>
</p>

<p align="center">
  <b>Structural Design Patterns</b> are concerned with how classes and objects are composed to form larger structures. They use inheritance to compose interfaces and define ways to compose objects to obtain new functionality.
</p>

---

## ?? Overview

Structural patterns explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient. They are particularly useful for making independently developed class libraries work together seamlessly.

This repository contains implementations of the following structural design patterns in **Python**:

| Pattern | Description | Implementation |
| :--- | :--- | :--- |
| **?? Adapter** | Allows objects with incompatible interfaces to collaborate. | [Adapter.py](./Adapter.py) |
| **?? Bridge** | Splits a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation. | [Bridge.py](./Bridge.py) |
| **?? Composite** | Composes objects into tree structures and lets you work with these structures as if they were individual objects. | [Composite.py](./Composite.py) |
| **?? Decorator** | Attaches new behaviors to objects by placing these objects inside special wrapper objects. | [Decorator.py](./Decorator.py) |
| **?? Facade** | Provides a simplified, higher-level interface to a complex subsystem of classes. | [Facade.py](./Facade.py) |
| **?? Flyweight** | Fits more objects into the available RAM by sharing common parts of state between multiple objects. | [Flyweight.py](./Flyweight.py) |
| **??? Proxy** | Provides a substitute or placeholder for another object to control access to it. | [Proxy.py](./Proxy.py) |

---

## ??? Deep Dive into Patterns (UML Diagrams)

### 1. Adapter Pattern (Adapter.py)
Also known as **Wrapper**. It converts the interface of a class into another interface the clients expect.
`mermaid
classDiagram
    class Client
    class Target {
        <<interface>>
        +request()
    }
    class Adapter {
        +request()
    }
    class Adaptee {
        +specificRequest()
    }
    Client --> Target
    Target <|.. Adapter
    Adapter --> Adaptee : adapts
`

### 2. Bridge Pattern (Bridge.py)
Decouples an abstraction from its implementation so that the two can vary independently.
`mermaid
classDiagram
    class Abstraction {
        -implementor: Implementor
        +operation()
    }
    class Implementor {
        <<interface>>
        +operationImpl()
    }
    class RefinedAbstraction {
        +operation()
    }
    class ConcreteImplementorA {
        +operationImpl()
    }
    class ConcreteImplementorB {
        +operationImpl()
    }

    Abstraction o--> Implementor : has a
    Abstraction <|-- RefinedAbstraction
    Implementor <|.. ConcreteImplementorA
    Implementor <|.. ConcreteImplementorB
`

### 3. Composite Pattern (Composite.py)
Composes objects into tree structures to represent part-whole hierarchies.
`mermaid
classDiagram
    class Component {
        <<interface>>
        +operation()
        +add(Component)
        +remove(Component)
        +getChild(int)
    }
    class Leaf {
        +operation()
    }
    class Composite {
        -children: List~Component~
        +operation()
        +add(Component)
        +remove(Component)
        +getChild(int)
    }
    Component <|.. Leaf
    Component <|.. Composite
    Composite o--> Component : contains
`

### 4. Decorator Pattern (Decorator.py)
`mermaid
classDiagram
    class Component {
        <<interface>>
        +operation()
    }
    class ConcreteComponent {
        +operation()
    }
    class Decorator {
        -component: Component
        +operation()
    }
    class ConcreteDecorator {
        +operation()
        +addedBehavior()
    }
    Component <|.. ConcreteComponent
    Component <|.. Decorator
    Decorator o--> Component
    Decorator <|-- ConcreteDecorator
`

---

## ?? How to Run

Each file is a standalone Python script demonstrating the pattern. You can run them individually from your terminal:

`ash
python Adapter.py
python Bridge.py
python Composite.py
python Decorator.py
python Facade.py
python Flyweight.py
python Proxy.py
`

## ?? Contributing
Contributions are always welcome! If you have any improvements or want to add more examples in other languages, feel free to open a Pull Request.

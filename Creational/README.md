# 🏗️ Creational Design Patterns

<p align="center">
  <img src="https://images.unsplash.com/photo-1581092335397-9583eb92d232?q=80&w=2000&auto=format&fit=crop" alt="Creational Design Patterns Banner" width="100%" style="border-radius:15px;"/>
</p>

<p align="center">
  <b>Creational Design Patterns</b> deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. They abstract the instantiation process and help make a system independent of how its objects are created, composed, and represented.
</p>

---

## 📖 Overview

In software engineering, creational design patterns are design patterns that deal with object creation mechanisms. The basic form of object creation could result in design problems or add complexity to the design. Creational design patterns solve this problem by controlling this object creation.

This repository contains the following creational design patterns implemented in **Python**:

| Pattern | Description | Implementation |
| :--- | :--- | :--- |
| **🏭 Factory Method** | Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. | [Factory.py](./Factory.py) |
| **🏢 Abstract Factory** | Lets you produce families of related objects without specifying their concrete classes. | [AbstractFactory.py](./AbstractFactory.py) |
| **👷 Builder** | Lets you construct complex objects step by step. It allows you to produce different types and representations of an object using the same construction code. | [Builder.py](./Builder.py) |
| **🐑 Prototype** | Lets you copy existing objects without making your code dependent on their classes. | [Prototype.py](./Prototype.py) |
| **1️⃣ Singleton** | Ensures that a class has only one instance, while providing a global access point to this instance. | [Singelton.py](./Singelton.py) |

---

## 🛠️ Deep Dive into Patterns (UML Diagrams)

### 1. Abstract Factory (AbstractFactory.py)
Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
`mermaid
classDiagram
    class AbstractFactory {
        <<interface>>
        +createProductA()
        +createProductB()
    }
    class ConcreteFactory1 {
        +createProductA()
        +createProductB()
    }
    class ConcreteFactory2 {
        +createProductA()
        +createProductB()
    }
    class AbstractProductA {
        <<interface>>
    }
    class AbstractProductB {
        <<interface>>
    }
    class ProductA1
    class ProductB1
    class ProductA2
    class ProductB2

    AbstractFactory <|.. ConcreteFactory1
    AbstractFactory <|.. ConcreteFactory2
    AbstractProductA <|.. ProductA1
    AbstractProductB <|.. ProductB1
    AbstractProductA <|.. ProductA2
    AbstractProductB <|.. ProductB2
    
    ConcreteFactory1 ..> ProductA1 : creates
    ConcreteFactory1 ..> ProductB1 : creates
    ConcreteFactory2 ..> ProductA2 : creates
    ConcreteFactory2 ..> ProductB2 : creates
`

### 2. Builder (Builder.py)
Separates the construction of a complex object from its representation so that the same construction process can create different representations.
`mermaid
classDiagram
    class Director {
        -builder: Builder
        +construct()
    }
    class Builder {
        <<interface>>
        +buildPartA()
        +buildPartB()
        +getResult()
    }
    class ConcreteBuilder {
        -product: Product
        +buildPartA()
        +buildPartB()
        +getResult()
    }
    class Product

    Director o--> Builder : uses
    Builder <|.. ConcreteBuilder
    ConcreteBuilder ..> Product : creates
`

### 3. Singleton (Singelton.py)
Ensures a class has only one instance, and provides a global point of access to it.
`mermaid
classDiagram
    class Singleton {
        -static instance: Singleton
        -Singleton()
        +static getInstance() Singleton
        +doSomething()
    }
`

---

## 🚀 How to Run

Each file is a standalone Python script demonstrating the pattern. You can run them individually from your terminal:

`ash
python Factory.py
python Builder.py
python Singelton.py
# etc.
`

## 🤝 Contributing
Contributions are always welcome! If you have any improvements or want to add more examples in other languages, feel free to open a Pull Request.

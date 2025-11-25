
Personal Pet Project
Michael Whalen
•
Oct 21
Learning Progress
•
15 points
Repo: https://classroom.github.com/a/_NmmYTVg

Personal Pet Project
You will be designing an application to allow users to play with a new “pet”. Think Tamgaotchi. You may use whatever lore or character style you want.
Users will be able to create a new pet based on Python classes. After instantiating a new pet they will be able to play and care for the pet. Values for the pet should be displayed and updated. See in class example.
L1.md
Text

lesson2.md
Text

Class comments
Your work
Assigned
Private comments
# 🧠 Lesson: Python Classes & Encapsulation


## 🚀 1. What Is a Class?

Imagine you’re designing a video game.
You might have many **heroes**, each with a name, money, and items in their backpack.

Instead of writing new code for each hero, Python lets us use a **class** — a *blueprint* for making similar objects.

### Analogy:

> A **class** is like a *cookie cutter*.
> An **object** is like the *cookie* made from it.

So if `Hero` is our cookie cutter, then `Jillian` or `Mario` are individual cookies 🍪.

---

## 🧩 2. Simple Example: Calculator Class

Let’s look at this code:

```python
class Calculator():
    def add(x, y):
        print(x + y)
        return x + y

    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)

    def subtract(numbers):
        return numbers

Calculator.add(5, 6)
```

### 💡 What’s Happening

* `class Calculator()` — defines a new *type* of object called **Calculator**.
* Inside are **methods** (functions that belong to a class):
  `add`, `add_many`, and `subtract`.
* `Calculator.add(5, 6)` calls the `add` method.

---

## 🧱 3. Building Your Own Class: Hero

Now we make a **Hero** class that describes a game character.

```python
class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
```

### 🔍 Breaking it down

#### 🏗️ `__init__` Method

This is a *special* function called every time a new Hero is created.
It sets up the hero’s starting information (name, money, items).

* `self.name` — hero’s name
* `self.money` — how much money the hero has
* `self.inventory` — what items they carry

#### 🧍‍♀️ Creating a Hero

```python
Jillian = Hero("Jillian", 150, ["Potion"])
```

* We just made a new **Hero object** named Jillian!
* Jillian starts with **$150** and one **Potion**.

#### 💰 Buying an Item

```python
Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__)
```

When Jillian buys something:

* The item is added to her inventory list.
* The inventory is printed.
* `__dict__` shows all her data stored in a dictionary format.

---

## 🔒 4. Encapsulation: Protecting Data

Encapsulation means **keeping related data and methods inside a single unit (the class)** — and **controlling how outside code interacts** with that data.

### Analogy:

> Imagine the Hero’s backpack is zipped shut 🎒.
> Only the Hero knows how to open it properly (using their methods).
> You don’t just reach in and mess with it directly!

In Python, we can use **naming conventions** to mark variables as “private” (for internal use only).

Example:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
```

This way, no one outside the class should directly do `my_account.__balance = 0`.
They should use the **methods** (`deposit`, `show_balance`) instead.

---

## 🧠 5. Practice Time

### ✏️ Activity 1 – Create Your Own Hero

Make your own hero object with a name, starting money, and one item.

Then, use `.buy()` to add another item to your inventory.

### ✏️ Activity 2 – Add Encapsulation

Create a class `Pet` that has:

* A **name**
* A **private variable** for happiness level (e.g., `__happiness`)
* A method to **play()** that increases happiness
* A method to **show_status()** that prints how happy the pet is

Example output:

```
Fluffy is playing fetch!
Fluffy’s happiness is now 10
```

---

## 💬 6. Key Takeaways

| Concept           | Meaning                                       | Example                              |
| ----------------- | --------------------------------------------- | ------------------------------------ |
| **Class**         | Blueprint for creating objects                | `class Hero:`                        |
| **Object**        | A specific example from a class               | `Jillian = Hero(...)`                |
| **Method**        | Function inside a class                       | `def buy(self, item)`                |
| **Encapsulation** | Keeping data + methods together and protected | private variables like `__balance`   |
| **self**          | Refers to the *current object*                | `self.name` means “this hero’s name” |

---

## 🌟 7. Challenge (Optional)

Modify the Hero class so that:

* It has a **private money variable** (`__money`)
* You must use a method like `.spend(amount)` to reduce money when buying something

Then print out how much money Jillian has left after buying her sword.

---





Personal Pet Project
Michael Whalen
•
Oct 21
Learning Progress
•
15 points
Repo: https://classroom.github.com/a/_NmmYTVg

Personal Pet Project
You will be designing an application to allow users to play with a new “pet”. Think Tamgaotchi. You may use whatever lore or character style you want.
Users will be able to create a new pet based on Python classes. After instantiating a new pet they will be able to play and care for the pet. Values for the pet should be displayed and updated. See in class example.
L1.md
Text

lesson2.md
Text

Class comments
Your work
Assigned
Private comments
# Lesson: Using Classes with Inheritance in Python

## Introduction to Inheritance
**Inheritance** is a fundamental concept in object-oriented programming that allows a class (child class) to inherit properties and behaviors from another class (parent class). This promotes code reusability and hierarchical structuring of classes.

### Defining a Parent Class
A **parent class** (also known as a base or super class) provides common attributes and methods that other classes can inherit.

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
```

### Creating Child Classes
A **child class** (also known as a derived or subclass) inherits from the parent class. It can also extend or override its behavior.

#### Student Class
```python
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
```

#### Teacher Class
```python
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
```

#### Administrator Class
```python
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
```

### Instantiating and Using the Child Classes
```python
student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())  # Output: Student: Alice, Email: alice@example.com, Student ID: S12345
print(teacher.display_info())  # Output: Teacher: Mr. Smith, Email: smith@example.com, Subject: Mathematics
print(administrator.display_info())  # Output: Administrator: Ms. Johnson, Email: johnson@example.com, Role: Principal
```

---

## Overriding Parent Class Methods
A child class can **override** methods from the parent class to provide specialized behavior.

For example, let's modify the `Administrator` class to include an additional action:

```python
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self):
        return f"{self.name} ({self.role}) is managing the system."
```

### Using the Overridden Method
```python
admin = Administrator("Ms. Johnson", "johnson@example.com", "Principal")
print(admin.manage_system())  # Output: Ms. Johnson (Principal) is managing the system.
```

---

## Using `super()` to Extend Parent Methods
Instead of completely overriding a method, we can extend its behavior using `super()`.

```python
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"
```

### Using the Extended Method
```python
my_teacher = Teacher("Mr. Brown", "brown@example.com", "Science")
print(my_teacher.display_info())  # Output: User: Mr. Brown, Email: brown@example.com, Subject: Science
```

---

## Key Takeaways
1. **Inheritance** allows a child class to reuse and extend a parent class’s behavior.
2. **`super()`** is used to call methods from the parent class.
3. **Method overriding** enables modifying parent class methods in a child class.
4. **Extending methods** using `super()` allows the original behavior to be retained while adding new functionality.
5. **Hierarchical structuring** using inheritance improves code organization and reduces redundancy.

This lesson provides a foundation for using inheritance in Python to create efficient, modular, and maintainable code.
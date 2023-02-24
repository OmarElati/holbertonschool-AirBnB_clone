# holbertonschool-AirBnB_clone.git

## Description

This project is a command-line interface for an AirBnB clone. It allows users to manage objects, such as users, places, amenities, and more. The command interpreter is a tool for developers to test and develop the backend of the AirBnB clone.

## How to Start the Command Interpreter

- Clone the repository from GitHub:

```bash

git clone https://github.com/OmarElati/holbertonschool-AirBnB_clone.git
```
- Navigate into the directory:

```bash

cd holbertonschool-AirBnB_clone
```
- Start the command interpreter:

```pyhton

./console.py
```
## How to Use the Command Interpreter

- The command interpreter uses a simple syntax for users to create, read, update, and delete objects. Here are some of the available commands:
create

### Create a new object of a given class:

```pyhton

(hbnb) create <class name>
```
### show

- Display information about a specific object:

```python

(hbnb) show <class name> <object id>
```
### update

- Update an object's attributes:

```python

(hbnb) update <class name> <object id> <attribute name> "<attribute value>"
```
### destroy

- Delete a specific object:

```python

(hbnb) destroy <class name> <object id>
```
### all

- Display all objects of a given class or all objects in general:

```python

(hbnb) all <class name>
```
### Examples

- Here are some examples of using the command interpreter:

- Create a new User object:

```sql

(hbnb) create User
```
- Display information about a specific User object:

```sql

(hbnb) show User 1234-1234-1234
```
- Update a User object's email attribute:

```sql

(hbnb) update User 1234-1234-1234 email "5796@holbertonstudents.com"
```
- Delete a User object:

```scss

(hbnb) destroy User 1234-1234-1234
```
- Display all objects of the User class:

```scss

(hbnb) all User
```
Authors
Omar Elati <5796@holbertonstudents.com>

# AirBnB Clone(hbnb)
The overall goal of this project is to deploy on out server a simple copy of the AirBnB Website. It implements only a few features to cover the fundamentals of the higher level programming track.

It comprises:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

- A website (the front-end) that shows the final product to everybody: static and dynamic

- A database or files that store data (data = objects)

- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The Console
This is a command line interphase that works quite like the shell except it's a single use function that allows creation, modification and deletion of objects in file storage. It is helps test to see what works and what doesn't in storage before building the rest of the web application.

## Case Implementation: Interactive mode

`>$ ./console.py`

`(hbnb) help`

`Documented commands (type help <topic>):`

`========================================`

`EOF  help  quit`

`(hbnb) help quit`

`quits the interpreter`

`(hbnb)`

`(hbnb) quit`

`>$`


## Case Implementation: Non-interactive mode
`>$ echo "help" | ./console.py`

(hbnb)

`Documented commands (type help <topic>):`

`========================================`

`EOF  help  quit`

`(hbnb)`
`>$`

`>$ cat test_help`

`help`

`>$`

`>$ cat test_help | ./console.py`

`(hbnb)`

`Documented commands (type help <topic>):`

`========================================`

`EOF  help  quit`

`(hbnb)`

`>$`

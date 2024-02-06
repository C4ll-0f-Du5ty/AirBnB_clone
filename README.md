# AirBnB Clone - The Console
## Description
AirBnB Clone is a console-based application that simulates the core functionalities of AirBnB. It allows users to create, retrieve, update, and delete objects representing various entities such as Users, States, Cities, and Places. The project is built using Python and follows the principles of Object-Oriented Programming (OOP).

## Command Interpreter
The command interpreter is the heart of the AirBnB Clone application. It interprets and executes commands entered by the user, managing the lifecycle of AirBnB objects.

## Starting the Application
To start the application, navigate to the project directory and run the following command:

```$ ./console.py```
## Using the Application
Once the application is running, you can interact with it using the command prompt (hbnb). Enter commands to manage your AirBnB objects. For example:

(hbnb) create User\
(hbnb) show User\
(hbnb) destroy User
## Examples
Here are some examples of how to use the command interpreter:

## Start the console
```$ ./console.py```

## Show available commands
```(hbnb) help```

## Create a new User
```(hbnb) create User```

## Show details of the newly created User
```(hbnb) show User```

## Update the User's email
```(hbnb) update User email``` newemail@example.com

## Destroy the User
```(hbnb) destroy User```

## Quit the console
```(hbnb) quit```
# Non-Interactive Mode
The console can also be used in non-interactive mode by piping commands into the script:

```echo "show User" | ./console.py```
Or by redirecting a file containing commands:

```cat commands.txt | ./console.py```

# Authors
This project was developed by **Allem Abdelaziz**.

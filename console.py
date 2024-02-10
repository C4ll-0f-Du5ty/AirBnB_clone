#!/usr/bin/python3
"""My Executable Console File"""
import cmd
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Using the CMD module i do make this CLI"""
    prompt = "(hbnb)"

    def do_EOF(self, args):
        """Using CTRL + D to exit"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, args):
        """Creating a new instance By Class Name"""
        if len(args) == 0:
            print("** class name missing **")
            return

        name = globals().get(args)
        if not name:
            print("** class doesn't exist **")
            return
        else:
            obj = name()
            models.storage.new(obj)
            print(obj.id)
            models.storage.save()
            return

    def do_show(self, args):
        """Prints the string representation of an instance
            based on the class name"""
        found = False

        if not args:
            print("** class name missing **")
            return

        parts = args.split()
        part1 = parts[0]
        name = globals().get(part1)

        if not name:
            print("** class doesn't exist **")
            return

        if len(parts) < 2:
            print("** instance id missing **")
            return

        part2 = parts[1]

        objects = models.storage.all()
        for key, value in objects.items():
            if value.id == part2:
                print(str(value))
                found = True
                break
        if not found:
            print("** no instance found **")
            return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        found = False

        if not args:
            print("** class name missing **")
            return

        parts = args.split()
        part1 = parts[0]
        name = globals().get(part1)

        if not name:
            print("** class doesn't exist **")
            return

        if len(parts) < 2:
            print("** instance id missing **")
            return

        part2 = parts[1]

        objects = models.storage.all()
        for key, value in objects.items():
            if value.id == part2:
                del (objects[key])
                found = True
                models.storage.save()
                break
        if not found:
            print("** no instance found **")
            return

    def do_all(self, args):
        """Prints all string representation of all instances
            based or not on the class name"""

        if args:
            name = globals().get(args.split()[0])
            if not name:
                print("** class doesn't exist **")
                return
            else:
                objects = models.storage.all()
                for value in objects.values():
                    if value.__class__ == name:
                        print(value)
        else:
            objects = models.storage.all()
            for key in objects.keys():
                print(objects[key])

    def emptyline(self):
        """Neglecting the Empty Lines"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

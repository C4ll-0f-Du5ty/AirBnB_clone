#!/usr/bin/python3
"""My Executable Console File"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def convert_value(value):
    """Converts a string to the appropriate type based on its content."""
    # Try converting to integer
    try:
        return int(value)
    except ValueError:
        pass

    # Try converting to float
    try:
        return float(value)
    except ValueError:
        pass

    # Default to string
    return str(value)


class HBNBCommand(cmd.Cmd):
    """Using the CMD module i do make this CLI"""
    prompt = "(hbnb) "

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
            storage.new(obj)
            print(obj.id)
            storage.save()
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

        objects = storage.all()
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

        objects = storage.all()
        for key, value in objects.items():
            if value.id == part2:
                del (objects[key])
                found = True
                storage.save()
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
                objects = storage.all()
                for value in objects.values():
                    if value.__class__ == name:
                        print(str(value))
        else:
            objects = storage.all()
            for key in objects.keys():
                print(str(objects[key]))

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
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

        objects = storage.all()
        instance = None
        for value in objects.values():
            if value.id == part2:
                instance = value
                break
        if not instance:
            print("** no instance found **")
            return

        part3 = parts[2]
        part4 = parts[3]
        # Update the attribute
        try:
            full_attr_value = ' '.join(parts[3:])
            part4 = convert_value(full_attr_value.strip('"'))
            setattr(instance, part3, part4)
            storage.save()
        except AttributeError:
            print("** attribute name missing **")
            return
        except Exception as e:
            print("** value missing **")
            return

    def emptyline(self):
        """Neglecting the Empty Lines"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

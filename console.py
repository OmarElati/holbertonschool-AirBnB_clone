#!/usr/bin/python3
"""Command interpreter module"""

import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    storage = storage
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Handles empty line when user inputs '\n'
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to a JSON file and
        prints the id of the new instance.
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id and saves the
        change into the JSON file.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name.
        """
        args = arg.split()
        instances_list = []
        if not arg:
            for value in storage.all().values():
                instances_list.append(str(value))
            print(instances_list)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if args[0] in key:
                    instances_list.append(str(value))
            print(instances_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key not in self.storage.all():
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        obj = self.storage.all()[key]
        setattr(obj, arg_list[2], arg_list[3])
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

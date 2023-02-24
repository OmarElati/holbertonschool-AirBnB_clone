#!/usr/bin/python3
"""Command interpreter module"""
import cmd
import models
from models import models_classes
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_object = self.classes[arg]()
        new_object.save()
        print(new_object.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            instance = storage.all()[args[0] + "." + args[1]]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(instance, args[2], type(getattr(instance, args[2]))(args[3]))
            instance.save()
        except KeyError:
            print("** no instance found **")
        except IndexError:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

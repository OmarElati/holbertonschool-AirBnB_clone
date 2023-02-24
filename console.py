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
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            instance = storage.all()[args[0] + "." + args[1]]
            print(instance)
        except KeyError:
            print("** no instance found **")
        except IndexError:
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            instance = storage.all()[args[0] + "." + args[1]]
            del storage.all()[args[0] + "." + args[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")
        except IndexError:
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objects = []
        if arg:
            if arg not in storage.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if arg in k:
                    objects.append(str(v))
        else:
            for v in storage.all().values():
                objects.append(str(v))
        print(objects)

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
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

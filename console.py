#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""

import os
import sys
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line handler, does nothing"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.classes:
            print("** class doesn't exist **")
            return

        instance = self.classes[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Display an instance based on its ID"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = models.storage.all()
        instance = instances.get(key)
        if instance is None:
            print("** no instance found **")
            return

        print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on its ID"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = models.storage.all()
        instance = instances.get(key)
        if instance is None:
            print("** no instance found **")
            return

        del instances[key]
        models.storage.save()

    def do_all(self, line):
        """Retrieve all instances of a class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instances = models.storage.all(self.classes[class_name])
        print([str(instance) for instance in instances])

    def do_update(self, line):
        """Updates an instance based on its ID"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = models.storage.all()
        instance = instances.get(key)
        if instance is None:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        if hasattr(instance, attribute_name):
            try:
                attribute_value = eval(attribute_value)
            except (NameError, SyntaxError):
                pass

            setattr(instance, attribute_name, attribute_value)
            models.storage.save()
        else:
            print("** attribute doesn't exist **")

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instances = models.storage.all(self.classes[class_name])
        print(len(instances))

    def do_show_by_id(self, arg):
        """Retrieves an instance based on its ID"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy_by_id(self, arg):
        """Destroys an instance based on its ID"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return

        storage.all().pop(key)
        storage.save()

    def do_update_by_Id(self, line):
        """Updates an instance based on its ID with a dictionary"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = models.storage.all()
        instance = instances.get(key)
        if instance is None:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** dictionary missing **")
            return

        try:
            dictionary = eval(' '.join(args[2:]))
        except (NameError, SyntaxError):
            print("** invalid dictionary format **")
            return

        if not isinstance(dictionary, dict):
            print("** invalid dictionary format **")
            return

        for attr, value in dictionary.items():
            if hasattr(instance, attr):
                setattr(instance, attr, value)
            else:
                print("** attribute doesn't exist **")
                return

        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

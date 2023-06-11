#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""

import re
import cmd
import sys
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

    def do_show(self, arg):
        """Prints the string representation of an instance"""
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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
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

    def do_all(self, arg):
        """Prints all instances or instances of a specific class"""
        args = arg.split()
        objects = []
        if not args:
            objects = list(storage.all().values())
        elif args[0] in self.classes:
            objects = [v for k, v in storage.all().items() if args[0] in k]
        else:
            print("** class doesn't exist **")
            return

        print([str(obj) for obj in objects])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
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

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        if attr_name == "id" or attr_name == "created_at" or attr_name == "updated_at":
            return

        attr_value = self.parse_attr_value(attr_value)
        setattr(obj, attr_name, attr_value)
        obj.save()

    def parse_attr_value(self, value):
        """Parse and cast attribute value based on its type"""
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        count = 0
        for key in storage.all():
            if args[0] in key:
                count += 1

        print(count)

    def do_show_by_id(self, arg):
        """Retrieve an instance based on its ID"""
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
        """Destroy an instance based on its ID"""
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

    def do_update_by_id(self, arg):
        """Update an instance based on its ID"""
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

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_dict = self.parse_attr_dict(args[2:])
        for attr_name, attr_value in attr_dict.items():
            if attr_name == "id" or attr_name == "created_at" or attr_name == "updated_at":
                continue
            setattr(obj, attr_name, attr_value)
        obj.save()

    def parse_attr_dict(self, args):
        """Parse attribute dictionary representation"""
        try:
            attr_dict = json.loads(" ".join(args))
            return attr_dict
        except json.JSONDecodeError:
            print("** Invalid JSON format **")
            return {}

    def precmd(self, line):
        """Override precmd method to handle commands with class names"""
        class_commands = [
            "show",
            "destroy",
            "update",
            "count",
            "show_by_id",
            "destroy_by_id",
            "update_by_id"
        ]
        for command in class_commands:
            if line.startswith(command):
                parts = line.split("(")
                if len(parts) > 1:
                    class_name = parts[0]
                    args = parts[1][:-1]
                    return f"{class_name} {args}"

        return line

    def postcmd(self, stop, line):
        """Override postcmd method to update the prompt after each command"""
        self.prompt = "(hbnb) "
        return stop


if __name__ == "__main__":
    HBNBCommand().cmdloop()

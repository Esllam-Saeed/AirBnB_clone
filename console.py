#!/usr/bin/python3
""" This module contains the CLI-like
    command environment for data manipulation"""
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import models
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ This class defines the attributes and methods of a Command Line
        environment that can manipulate JSON-stored objects """
    prompt = "(hbnb) "

    # Basic Commands
    def do_create(self, arg):
        """ This method creates an attribute, the command format is:
            create <class name> """
        arg_list = arg.split()
        if arg_list is None or arg_list == []:
            print("** class name missing **")
            return
        elif (arg_list[0] not in ["BaseModel", "User", "City",
                                  "Place", "State", "Amenity", "Review"]):
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(f"{arg_list[0]}()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ This method prints an instance by id, the command format is:
            show <class name> <id> """
        arg_list = arg.split()
        if arg_list is None or arg_list == []:
            print("** class name missing **")
            return
        elif (arg_list[0] not in ["BaseModel", "User", "City",
                                  "Place", "State", "Amenity", "Review"]):
            print("** class doesn't exist **")
            return
        elif len(arg_list) < 2:
            print("** instance id missing **")
            return
        else:
            for key, value in models.storage.all().items():
                if key == f"{arg_list[0]}.{arg_list[1]}":
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ This method deletes an instance by id, the command format is:
            destroy <class name> <id> """
        arg_list = arg.split()
        if arg_list is None or arg_list == []:
            print("** class name missing **")
            return
        elif (arg_list[0] not in ["BaseModel", "User", "City",
                                  "Place", "State", "Amenity", "Review"]):
            print("** class doesn't exist **")
            return
        elif len(arg_list) < 2:
            print("** instance id missing **")
            return
        else:
            for key in models.storage.all().keys():
                if key == f"{arg_list[0]}.{arg_list[1]}":
                    del models.storage.all()[key]
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ This method prints all instances, with optional class name
            the command format is:
            all <class name> """
        arg_list = arg.split()
        if arg_list is None or arg_list == []:
            output_list = ([str(value) for value in
                            models.storage.all().values()])
            print(output_list)
        else:
            if (arg_list[0] not in ["BaseModel", "User", "City",
                                    "Place", "State", "Amenity", "Review"]):
                print("** class doesn't exist **")
                return
            else:
                output_list = []
                for key in models.storage.all():
                    if arg_list[0] in key:
                        output_list.append(str(models.storage.all()[key]))
                print(output_list)

    def do_update(self, arg):
        """ This method updates or creates an attribute, the command format is:
            update <class name> <id> <attribute name> <attribute value> """
        arg_list = arg.split()
        if arg_list is None or arg_list == []:
            print("** class name missing **")
            return
        elif (arg_list[0] not in ["BaseModel", "User", "City",
                                  "Place", "State", "Amenity", "Review"]):
            print("** class doesn't exist **")
            return
        elif len(arg_list) < 2:
            print("** instance id missing **")
            return
        elif len(arg_list) < 3:
            print("** attribute name missing **")
            return
        elif len(arg_list) < 4:
            print("** value missing **")
            return
        else:
            for key in models.storage.all():
                if key == f"{arg_list[0]}.{arg_list[1]}":
                    if type(arg_list[3]) is str:
                        setattr(models.storage.all()[key],
                                arg_list[2], str(arg_list[3]))
                        models.storage.save()
                        return
                    elif type(arg_list[3]) is int:
                        setattr(models.storage.all()[key],
                                arg_list[2], int(arg_list[3]))
                        models.storage.save()
                        return
                    elif type(arg_list[3]) is float:
                        setattr(models.storage.all()[key],
                                arg_list[2], float(arg_list[3]))
                        models.storage.save()
                        return
            print("** no instance found **")

    # Cmd Class Overrides
    def default(self, line):
        """ This method determines CLI behavior\
            when 'quit' or 'EOF' are encountered in args """
        if line == "quit" or line == "EOF":
            return True

        return super().default(line)

    def emptyline(self):
        """ This method determines CLI behavior when empty line is passed"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

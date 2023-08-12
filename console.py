#!/usr/bin/python3
"""This defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def tokenize(arg):
    """Creating a function to tokenize input strings
    with curly_b or cb as curly_bracket and square_bracket
    as square_b or sb.

    """
    curly_b = re.search(r"\{(.*?)\}", arg)
    square_b = re.search(r"\[(.*?)\]", arg)
    if curly_b is None:
        if square_b is None:
            return [item.strip(",") for item in split(arg)]
        else:
            before_sb = split(arg[:square_b.span()[0]])
            modified_list = [i.strip(",") for i in before_sb]
            modified_list.append(square_b.group())
            return modified_list
    else:
        before_cb = split(arg[:curly_b.span()[0]])
        modified_list = [i.strip(",") for i in before_cb]
        modified_list.append(curly_b.group())
        return modified_list


class HBNBCommand(cmd.Cmd):
    """This defines HBNB command interpreter

    Attributes:
        prompt (str): The command prompt
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }


    def do_quit(self, arg):
        """Quit to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do not execute anything upon receiving an empty line """
        pass


    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        args_list = tokenize(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args_list = tokenize(arg)
        obj_new = storage.all()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1]) not in obj_new:
            print("** no instance found **")
        else:
            print(obj_new["{}.{}".format(args_list[0], args_list[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        args_list = tokenize(arg)
        obj_new = storage.all()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1]) not in obj_new.keys():
            print("** no instance found **")
        else:
            del obj_new["{}.{}".format(args_list[0], args_list[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args_list = tokenize(arg)
        if len(args_list) > 0 and args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(args_list) > 0 and args_list[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(args_list) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args_list = tokenize(arg)
        count = 0
        for obj in storage.all().values():
            if args_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        args_list = tokenize(arg)
        obj_new = storage.all()

        if len(args_list) == 0:
            print("** class name missing **")
            return False
        if args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args_list[0], args_list[1]) not in obj_new.keys():
            print("** no instance found **")
            return False
        if len(args_list) == 2:
            print("** attribute name missing **")
            return False
        if len(args_list) == 3:
            try:
                type(eval(args_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args_list) == 4:
            obj = obj_new["{}.{}".format(args_list[0], args_list[1])]
            if args_list[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args_list[2]])
                obj.__dict__[args_list[2]] = valtype(args_list[3])
            else:
                obj.__dict__[args_list[2]] = args_list[3]
        elif type(eval(args_list[2])) == dict:
            obj = obj_new["{}.{}".format(args_list[0], args_list[1])]
            for k, v in eval(args_list[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

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


class HBNBcmd_args_match(cmd.Cmd):
    """This defines HBNB cmd_args_match interpreter

    Attributes:
        prompt (str): The cmd_args_match prompt
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
        elif args_list[0] not in HBNBcmd_args_match.__classes:
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
        elif args_list[0] not in HBNBcmd_args_match.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1]) not in obj_new:
            print("** no instance found **")
        else:
            print(obj_new["{}.{}".format(args_list[0], args_list[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file)
        """
        args_list = tokenize(arg)
        obj_new = storage.all()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBcmd_args_match.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1]) not in obj_new.keys():
            print("** no instance found **")
        else:
            del obj_new["{}.{}".format(args_list[0], args_list[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args_list = tokenize(arg)
        if len(args_list) > 0 and args_list[0] not in HBNBcmd_args_match.__classes:
            print("** class doesn't exist **")
        else:
            obj_lists = []
            for obj in storage.all().values():
                if len(args_list) > 0 and args_list[0] == obj.__class__.__name__:
                    obj_lists.append(obj.__str__())
                elif len(args_list) == 0:
                    obj_lists.append(obj.__str__())
            print(obj_lists)


    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        args_list = tokenize(arg)
        obj_new = storage.all()

        if len(args_list) == 0:
            print("** class name missing **")
            return False
        if args_list[0] not in HBNBcmd_args_match.__classes:
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

        """Updating the instance attributes based on the provided arguments"""
        if len(args_list) == 4:
            obj = obj_new["{}.{}".format(args_list[0], args_list[1])]
            if args_list[2] in obj.__class__.__dict__.keys():
                attr_type = type(obj.__class__.__dict__[args_list[2]])
                obj.__dict__[args_list[2]] = attr_type(args_list[3])
            else:
                obj.__dict__[args_list[2]] = args_list[3]
        elif type(eval(args_list[2])) == dict:
            obj = obj_new["{}.{}".format(args_list[0], args_list[1])]
            for key, value in eval(args_list[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    attr_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = attr_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def do_count(self, arg):
        """Updating cmd_args_match interpreter to retrieve the
        number of instances of a class: <class name>.count()."""
        args_list = tokenize(arg)
        count = 0
        for obj in storage.all().values():
            if args_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """This handle the dispatching
        of cmd_args_matchs based on the input"""
        cmd_methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        cmd_match = re.search(r"\.", arg)
        if cmd_match is not None:
            arg_lists = [arg[:cmd_match.span()[0]], arg[cmd_match.span()[1]:]]
            cmd_match = re.search(r"\((.*?)\)", arg_lists[1])
            if cmd_match is not None:
                cmd_args_match = [arg_lists[1][:cmd_match.span()[0]], cmd_match.group()[1:-1]]
                if cmd_args_match[0] in cmd_methods.keys():
                    call = "{} {}".format(arg_lists[0], cmd_args_match[1])
                    return cmd_methods[cmd_args_match[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

if __name__ == "__main__":
    HBNBcmd_args_match().cmdloop()

#!/usr/bin/python3
"""This defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage


"""Creating a function to tokenize input strings"""

def tokenize(arg):
    curly_brackets = re.search(r"\{(.*?)\}", arg)
    square_brackets = re.search(r"\[(.*?)\]", arg)

    if not curly_brackets and not square_brackets:
        return split(arg)
    elif square_brackets:
        """cbrackets means square brackets"""
        before_sbrackets = split(arg[:square_brackets.span()[0]])
        modified_list = [item.strip(",") for item in before_sbrackets]
        modified_list.append(square_brackets.group())
        return modified_list
    else:
        """cbrackets means curly brackets"""
        before_cbrackets = split(arg[:curly_brackets.span()[0]])
        modified_list = [item.strip(",") for item in before_cbrackets]
        modified_list.append(curly_brackets.group())
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

    def empty_line(self):
        """Do not execute anything upon receiving an empty line """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        args_list = tokenize(arg)
        if len(args_list) == 0:
            print("* class name missing **")
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
            print("* class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1] not in obj_new):
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
            print("* class name missing **")
            return
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args_list) == 1:
            print("** instance id missing **")
            return
        instance_key = "{}.{}".format(args_list[0], args_list[1])
        if instance_key not in obj_new:
            print("** no instance found **")
            return
        del obj_new[instance_key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args_list = tokenize(arg)
        if len(args_list) > 0 and args_list[0] not in HBNBCommand.__classes:
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
        attr_name = args_list[2]
        attr_value = args_list[3]
        if len(args_list) == 0:
            print("* class name missing **")
            return
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args_list) == 1:
            print("** instance id missing **")
            return
        instance_key = "{}.{}".format(args_list[0], args_list[1])
        if instance_key not in obj_new:
            print("** no instance found **")
            return
        if len(args_list) == 2:
            print("** attribute name missing **")
            return
        if len(args_list) == 3:
            try:
                type(eval(attr_name)) != dict
            except NameError:
                print("** value missing **")
                return

        """Updating the instance attributes based on the provided arguments"""
        if len(args_list) == 4:
            obj = obj_new[instance_key]
            if attr_name in obj.__class__.__dict__.keys():
                atrr_type = type(obj.__class__.__dict__[attr_name])
                obj.__dict__[attr_name] = atrr_type(attr_value)
            else:
                obj.__dict__[attr_name] = attr_value
        elif type(eval(attr_name)) == dict:
            dict_update = obj_new[instance_key]
            for key, value in eval(attr_name).items():
                if (key in dict_update.__class__.__dict__.keys() and
                        type(dict_update.__class__.__dict__[key]) in {str, int, float}):
                    atrr_type = type(dict_update.__class__.__dict__[key])
                    dict_update.__dict__[key] = atrr_type(value)
                else:
                    dict_update.__dict__[key] = value
        storage.save()

    def do_count(self, arg):
        """Updating command interpreter to retrieve the
        number of instances of a class: <class name>.count()."""
        args_list = tokenize(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for obj in storage.all().values():
                if args_list[0] == obj.__class__.__name__:
                    count += 1
            print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()


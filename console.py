#!/usr/bin/python3
"""this program contains the entry point of the command interpreter"""
import cmd

from models import storage

class HBNBCommand(cmd.Cmd):
    """command processor"""
    prompt = '(hbnb) '
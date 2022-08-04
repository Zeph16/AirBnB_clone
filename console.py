#!/usr/bin/python3
""" The Command Interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """ Includes all functions to handle commands """
    prompt = "(hbnb) "
    models = []
    cmds = []

    def help_help(self):
        """ Shows help command description """
        print("Displays how to use a certain command")

    def help_EOF(self):
        """ EOF command help """
        print("Exits the interpreter with an EOF command")

    def help_quit(self):
        """ quit command help """
        print("Quits the interpreter")

    def emptyline(self):
        """ Doesn't do anything when empty line is input """
        pass

    def do_EOF(self, line):
        """ Exit function with EOF """
        return True

    def do_quit(self, line):
        """ Normally quits the interpreter """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

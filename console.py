#!/usr/bin/python3
""" The Command Interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.place import Place
from models.state import State
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """ Includes all functions to handle commands """
    prompt = "(hbnb) "
    models = ['BaseModel', 'User', 'Amenity', 'Place', 'State', 'Review']
    cmds = ['create', 'show', 'destroy', 'all', 'update', 'count']

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

    def precmd(self, arg):
        """ Formats command input before processing """
        if '.' in arg and '(' in arg and ')' in arg:
            model = arg.split('.')
            cmd = model[1].split('(')
            args = cmd[1].split(')')
            if model[0] in HBNBCommand.models and cmd[0] in HBNBCommand.cmds:
                arg = cmd[0] + ' ' + model[0] + ' ' + args[0]
            print(arg)
        return arg

    def do_count(self, cls_name):
        """ Displays number of stored instances of a specified class """
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def do_create(self, model):
        """ Creates an instance of the given class """
        if not model:
            print("** class name missing **")
        elif model not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            objdict = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'City': City,
                'Amenity': Amenity,
                'Review': Review,
                'State': State,
                }
            m = objdict[model]()
            print(m.id)
            m.save()

    def do_show(self, arg):
        """ Displays a string representation of the given instance """

        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        if args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes a specified instance """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        if args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Displays the string rep of all instances of a specified class """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        if args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """ Updates an instance """
        if not arg:
            print("** class name missing **")
            return
        a = ""
        for argv in arg.split(','):
            a = a + argv
        args = shlex.split(a)
        if args[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_EOF(self, line):
        """ Exit function with EOF """
        return True

    def do_quit(self, line):
        """ Normally quits the interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

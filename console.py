#!/usr/bin/env python3
import cmd
"""

a program called console.py that contains the entry point of the
command interpreter

"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def do_EOF(self, arg):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")
        print()

"""

if class called, loop

"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
import cmd
"""

a program called console.py that contains the entry point of the
command interpreter

"""


class HBNBCommand(cmd.Cmd):
    """

    class HBNBCommand, entry point of command interpreter

    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ exit the program """
        return True

    def help_quit(self):
        """ help quit """
        print("Quit command to exit the program")
        print()

    def do_EOF(self, arg):
        """ exit the program """
        return True

    def help_EOF(self):
        """ help EOF """
        print("EOF command to exit the program")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

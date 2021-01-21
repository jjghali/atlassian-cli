from sys import argv
# from gandalf import app

commands = ['help', '-v', 'product']


def help():
    print("this is help")


def version():
    print("app version here")


if __name__ == '__main__':
    if argv[1].lower() in commands:
        if argv[1].lower() == "help":
            help()
        elif argv[1].lower() == "-v":
            version()
    else:
        help()

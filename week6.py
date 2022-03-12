# import sys
#
# print(sys.path)
# #prints file path to this file. Site packages folder - pre-built folder

# define so useful functions
def cool_func1(none):
    return "Hello" + name + " from cool func 1"


def cool_func2(none):
    return "Hey" + name + " from cool func 2"

# invoking own useful function:
def main():

message = cool_func1("Everyone")
greeting = cool_func2("Team")

print(message, "\n", greeting)

# main is an inbuilt attribute
if __name__ == "__main__":
    main()
    # only call the main function if I'm the starting script of the python file

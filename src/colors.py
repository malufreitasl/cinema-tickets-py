# Function that returns a line of hyphen characters with a specific size
def line(size=42):
    return "-" * size

# Function to print a centered blue header with the provided text
def header_blue(txt):
    print(line())  
    print("\033[1;34m {}\033[0m".format(txt.center(40)))  
    print(line()) 

# Function to print a centered yellow header with the provided text
def header_yellow(txt):
    print(line())  
    print("\033[1;33m {}\033[0m".format(txt.center(40)))  
    print(line()) 

# Function to print a centered green header with the provided text
def header_green(txt):
    print(line())  
    print("\033[1;32m {}\033[0m".format(txt.center(40)))  
    print(line())  

# Function to print a centered cyan header with the provided text
def header_cyan(txt):
    print(line())  
    print("\033[1;36m {}\033[0m".format(txt.center(40)))  
    print(line()) 

# Function to print blue text
def blue(txt):
    print("\033[0;34m{}\033[0m".format(txt))  

# Function to print purple text
def purple(txt):
    print("\033[0;35m{}\033[0m".format(txt))  

# Function to print red text
def red(txt):
    print("\033[0;31m{}\033[0m".format(txt)) 

# Function to print green text
def green(txt):
    print("\033[0;32m{}\033[0m".format(txt))  

# Function to print yellow text
def yellow(txt):
    print("\033[0;33m{}\033[0m".format(txt))  

import pyfiglet
from termcolor import colored

valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan')

message = (input("Enter your message: "))
chose_color = input("what color do you want? : ")
if chose_color not in valid_colors:
    print("sorry! color not available! I selected one for you : cyan ")
    chose_color = 'cyan'


colored_ascii = colored(pyfiglet.figlet_format(message), color=chose_color)
print((colored_ascii))

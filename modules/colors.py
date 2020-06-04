import termcolor


text = termcolor.colored("hi there", color='red',
                         on_color="on_cyan", attrs=['blink'])

print(text)

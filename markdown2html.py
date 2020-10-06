!/usr/bin/python3
'''Markdown2HTML'''
import os
from sys import argv, exit, stderr


def run():
    ''' def run '''
    if len(argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    if not os.path.isfile(argv[1]):
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)

    final = ""
    with open(argv[1], 'r') as file:
        for line in file:
            if '#' in line:
                level = line.count("#")
                text = line.strip('#\n')
                text = text.lstrip()
                html = "<h{}>{}</h{}>".format(level, text, level)
                final += html + '\n'
    final = final.rstrip()
    with open(argv[2], 'w') as file:
        file.write(final)
    exit(0)

if __name__ == "__main__":
    run()

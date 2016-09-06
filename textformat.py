#!/usr/bin/python3

import textwrap

with open("text.txt") as t:
    old_text = t.read()

with open("text.txt") as t:
    new_text = t.read()

print(old_text)
a = textwrap.fill(new_text, width = 40)
print(textwrap.indent(a, ))

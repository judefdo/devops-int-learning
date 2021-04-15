import os

name="jude fernando"
name="100"
print(name[::-1])
print(name[:-1])
print(next((i for i,e in enumerate(name) if not e.isdigit()),'0'))
print(name.title())
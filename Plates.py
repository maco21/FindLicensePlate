import re

Targhe = [r'\D{2}\d{3}\D{2}',
          r'\D{2}\d{3}\D{1}',
          r'\D{2}\d{2}\D{2}',
          r'\D{2}\d{4}\D{2}',
          r'\D{1}\d{4}\D{2}',
          r'\D{1}\d{3}\D{2}',
          r'\D{2}\d{4}\D{1}',
          r'\D{1}\d{4}',
          r'\d{4}\D{4}']



"""
from Andrew Clark on Reddit:
You can use the character class [A-Z] to match any uppercase character,
and [0-9] to match any digit. You can specify repetition using {m,n}, 
which means "match the previous element between m and n times":
You may also want to add beginning and end of string anchors (^ and $ respectively):

^[A-Za-z]{1,4}-[A-Za-z]{1,2}-[0-9]{1,4}$

This depends on whether you are trying to pull license plates out of a larger string 
or trying to see if a particular string is a license plate (and nothing else).

If you also need to match lowercase characters, change each of the [A-Z] classes to [A-Za-z].

"""



    
with open('plates.txt', "r") as f: 
    for line in f:
        plate = any(re.match(targa, line) for targa in Targhe)
        if (plate):
            print("License: {plate} is present!".format(plate=line.strip()))
        else:
            print("License: {plate} is NOT present!".format(plate=line.strip()))


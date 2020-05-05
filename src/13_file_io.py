"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# with open('src/foo.txt') as file:
#     print(file.read())

from os import path
absfile = path.join(path.dirname(path.abspath(__file__)), "foo.txt")
with open(absfile, "r") as f:
    print(f.read())
f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
from os import path
absfile = path.join(path.dirname(path.abspath(__file__)), "bar.txt")
with open(absfile, "w") as f:
    content = "I am the new text"
    print(f.write(content))
f.close()

from os import path
absfile = path.join(path.dirname(path.abspath(__file__)), "bar.txt")
with open(absfile, "r") as f:
    print(f.read())
f.close()
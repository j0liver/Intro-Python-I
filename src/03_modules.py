"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))


# Print out the OS platform you're using:
# YOUR CODE HERE
import os
print(os.name)

import platform
print(platform.system())


# Print out the version of Python you're using:
# YOUR CODE HERE

import platform
print(platform.python_version())


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
pid = os.getpid() 
print(pid)

# Print the current working directory (cwd):
# YOUR CODE HERE
cdw = os.getcwd()
print(cdw)

# Print out your machine's login name
# YOUR CODE HERE
myhost = os.uname()[1]
print(myhost)
# Date (18/1/26)
# sys is sort for system
# sys basicly a modul that let u talk to python interpreter syste

import sys

sys.stderr.write("test")
sys.stderr.flush()


#print(sys.version)    # U can view the version of the python interpreter
print(sys.path)    # U can see the path of how peathon find ur file that have .py extention 
print(sys.platform)    # Telss u what your operating system do u use
print(sys.argv)    # Python will get ur argument and use it in command line
sys.exit()    # U can tell python to exit or end your program/code
#sys.getsizeof(object)   # the sisze of an object in memory
#sys.stdin   # The way an input# get in
#sys.stdout  # The way of an otput appear or writted in terminal
#sys.stderr  # The way of warning messages appear in terminal

#sys.stdout.write()  # Same as print. Instead, stout.write is the basic form of print. Add "\n" to make new line
#sys.stdout.flush()  # To make python print or write your value faster

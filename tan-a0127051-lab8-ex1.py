"""
Name: Tan Yi Yan
Matric. no.: A0127051U
Email: yiyan@u.nus.edu
"""
import os
import subprocess
import sys

def is_secret_msg(msg):
    """ Returns True if msg matches the format of the secret msg, otherwise return False"""
    return msg[:-4].isalpha() and msg[-4:].isdigit()

def main():
    """ Fuzzes the binary and prints all the arguments which give the secret msg and the secret msg """
    if len(sys.argv) != 2:
        print "USAGE: python tan-a0127051-lab8-ex1.py <binary file name>"
        return

    if not os.path.isfile(sys.argv[1]):
        print "ERROR: the binary file \"" + sys.argv[1] + "\" does not exist"
        return

    if not os.access(sys.argv[1], os.X_OK):
        print "ERROR: you have no permissions to execute \"" + sys.argv[1] + "\""
        return

    # Try all the possible arguments
    for i in range(256):
        for j in range(256):
            process = subprocess.Popen(["./" + sys.argv[1], str(i), str(j)], stdout=subprocess.PIPE)
            output = process.stdout.read()
            msg = output.split("\n\n")[1]
            if is_secret_msg(msg):
                print i, j, msg
main()

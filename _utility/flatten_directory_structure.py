import sys
import re
'''
	This code strips slashes and replaces with underscore to assist in flattening deep directory structures
	ex: _data/sn95079246$ find 1900 -type f -name *.txt | python ~/INS560-Project/_regex/flatten_directory_structure.py

	Input is stdin - expecting a qualified file name
	Output is stdout - a copy statement
'''
flatener = re.compile('\/', re.VERBOSE)

def main():
    line = sys.stdin.readline()
    while line:
	outline = "cp " + line.rstrip('\n') + " " + flatener.sub('_', line)
	sys.stdout.write(outline)
        line = sys.stdin.readline()

main()	

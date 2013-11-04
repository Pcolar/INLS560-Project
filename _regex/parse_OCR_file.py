import sys
import re

'''
parse_OCR_file

Input: 	filename to be parsed
	# of lines to be parsed

Parse the input file for #lines 
using the regex expressions, search input for Volume Number Page and Date
exit when all variables found or #lines reached

'''
total_args = int(len(sys.argv))
if ( total_args <> 3 ):
	print("Two input arguments are required -")
	print(" (filename to be parsed) and (# of lines to parse)")
	print("Script name: %s" % str(sys.argv[0]))
	for i in xrange(total_args):
    		print ("Argument # %d : %s" % (i, str(sys.argv[i])))
	exit(1)

filename = str(sys.argv[1])
print("file: %s" % filename)
Parse_limit = int(sys.argv[2])
print "# of lines to parse: ", Parse_limit
line_count = 0

volume = re.compile("(Volume|Vol)\s(\w+|\d+)", re.IGNORECASE)
number = re.compile("(number|num|no)\s\d+", re.IGNORECASE)
pdate  = re.compile("(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)\s\d+,\s\d+", re.IGNORECASE)

with open(filename) as OCR_File:	
#  for line_count in range(1, Parse_limit):
    for line in OCR_File:
	line_count += 1
	# search through the line for the strings
	found_volume = volume.search(line)
	if (found_volume):
		print "Volume found:", found_volume.span(), ":", line[found_volume.start():found_volume.end()]
	issue_number = number.search(line)
	if (issue_number):
		print "Issue found:", issue_number.span(), ":", line[issue_number.start():issue_number.end()]
	found_date = pdate.search(line)
	if (found_date):
		print "Date found: ", found_date.span(), ":", line[found_date.start():found_date.end()]
	if ((found_volume and issue_number and found_date) or (line_count >= Parse_limit)):
		break
#	print "line: ", line_count, "--", line

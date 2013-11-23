import sys
import re
from datetime import datetime

'''
parse_OCR_file

Input: 	filename to be parsed
	# of lines to be parsed

Parse the input file for #lines 
using the regex expressions, search input for Volume Number Page and Date
write result to CSV file when all variables found or #lines reached

'''
total_args = int(len(sys.argv))
if ( total_args <> 4 ):
	print("Three input arguments are required -")
	print(" (filename to be parsed), (# of lines to parse), (results filename)")
	print("Script name: %s" % str(sys.argv[0]))
	for i in xrange(total_args):
    		print ("Argument # %d : %s" % (i, str(sys.argv[i])))
	exit(1)

filename = str(sys.argv[1])
print("file: %s" % filename)
Parse_limit = int(sys.argv[2])
print "# of lines to parse: ", Parse_limit
outfilename = str(sys.argv[3])
print("output file: %s" % outfilename)
line_count = 0
double_quote = "\""
date_string = ""  
volume_string = ""
issue_string = ""
page_string = ""
volume = re.compile("(Volume|Vol)\s(\w+|\d+)", re.IGNORECASE)
number = re.compile("(number|num|no)\s\d+", re.IGNORECASE)
pdate  = re.compile("(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)\s\d+,\s\d+", re.IGNORECASE)
pageno = re.compile("(PAGE|PG)\s*(\w+|\d+)", re.IGNORECASE)
string_value = re.compile("(\w+|\d+)$")

with open(filename) as OCR_File:	
#  for line_count in range(1, Parse_limit):
    for line in OCR_File:
	line_count += 1
	# search through the line for the strings
	found_volume = volume.search(line)
	if (found_volume):
		print "Volume found:", found_volume.span(), ":", line[found_volume.start():found_volume.end()]
		raw_substring = line[found_volume.start():found_volume.end()]
		found_value = string_value.search(raw_substring)
		volume_string = raw_substring[found_value.start():found_value.end()]
		print "Volume: ", volume_string 
	issue_number = number.search(line)
	if (issue_number):
		print "Issue found:", issue_number.span(), ":", line[issue_number.start():issue_number.end()]
		raw_substring = line[issue_number.start():issue_number.end()]
		found_value = string_value.search(raw_substring)
		issue_string = raw_substring[found_value.start():found_value.end()]
	found_date = pdate.search(line)
	if (found_date):
		print "Date found: ", found_date.span(), ":", line[found_date.start():found_date.end()]
		date_string = line[found_date.start():found_date.end()]
#		raw_date = line[found_date.start():found_date.end()]
#		date_object = datetime.strptime( raw_date, '%B %m, %Y')
#		print "formatted date: ", date_object
        found_pageno = pageno.search(line)
	if (found_pageno):
		print "Page found: ", found_pageno.span(), ":", line[found_pageno.start():found_pageno.end()]
		raw_substring = line[found_pageno.start():found_pageno.end()]
		found_value = string_value.search(raw_substring)
		page_string = raw_substring[found_value.start():found_value.end()]
	if ((found_volume and issue_number and found_date) or (line_count >= Parse_limit)):
		break

output_line =  double_quote + filename + double_quote + ","
output_line += double_quote + date_string + double_quote + "," 
output_line += double_quote + volume_string + double_quote + "," 
output_line += double_quote + issue_string + double_quote + ","
output_line += double_quote + page_string + double_quote

print "output: ", output_line 
#csv_file = open(outfilename, 'a')
#csv_file.write(output_line)
#csv_file.close()
OCR_File.close()

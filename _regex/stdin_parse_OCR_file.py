
import sys
import re
from datetime import datetime

'''
parse_OCR_files from Stdin

Input: 	(stdin) filename to be parsed
	output CSV filename
	# of lines to be parsed

Parse the input file for #lines 
using the regex expressions, search input for Volume Number, Page, and Date
write result to CSV file when all variables found or #lines reached

'''

def find_volume(line):
	volume = re.compile("(Volume|Vol.)\s(\w+|\d+)", re.IGNORECASE)
	string_value = re.compile("(\w+|\d+)$")
        found_volume = volume.search(line)
        if (found_volume):
                raw_substring = line[found_volume.start():found_volume.end()]
                found_value = string_value.search(raw_substring)
                volume_string = raw_substring[found_value.start():found_value.end()]
                return volume_string

def find_issue(line):
	number = re.compile("(number|num.|no.)\s\d+", re.IGNORECASE)
	string_value = re.compile("(\w+|\d+)$")
        issue_number = number.search(line)
        if (issue_number):
                raw_substring = line[issue_number.start():issue_number.end()]
                found_value = string_value.search(raw_substring)
                issue_string = raw_substring[found_value.start():found_value.end()]
		print issue_string
                return issue_string

def find_date(line):
	pdate  = re.compile("(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)\s\d+,\s(\d+|.{4})", re.IGNORECASE)
	found_date = pdate.search(line)
        if (found_date):
                date_string = line[found_date.start():found_date.end()]
#               raw_date = line[found_date.start():found_date.end()]
#               date_object = datetime.strptime( raw_date, '%B %m, %Y')
#               print "formatted date: ", date_object
		print date_string
		return date_string

def find_pageno(line):
	pageno = re.compile("(PAGE|PG)\s*(\w+|\d+)", re.IGNORECASE)
	string_value = re.compile("(\w+|\d+)$")
        found_pageno = pageno.search(line)
        if (found_pageno):
                raw_substring = line[found_pageno.start():found_pageno.end()]
                found_value = string_value.search(raw_substring)
                page_string = raw_substring[found_value.start():found_value.end()]
		return page_string


total_args = int(len(sys.argv))
if ( total_args <> 3 ):
	print("two input arguments are required -")
	print(" (# of lines to parse), (results filename)")
	print("Script name: %s" % str(sys.argv[0]))
	for i in xrange(total_args):
    		print ("Argument # %d : %s" % (i, str(sys.argv[i])))
	exit(1)

Parse_limit = int(sys.argv[1])
print "# of lines to parse: ", Parse_limit
outfilename = str(sys.argv[2])
#print("output file: %s" % outfilename)
sequence_count = 0
double_quote = "\""

print "format: filename, date, volume, issue, page, sequence"


filename = sys.stdin.readline()  # read a filename from stdin
while filename:
  infile = filename.rstrip('\n')
  with open(infile) as OCR_File:    
    # setup parse of the input file
    date_string = None
    volume_string = None
    issue_string = None
    page_string = None
    line_count = 0

    for line in OCR_File:  # process each line in the OCR text file until Parse_limit
	line = line.rstrip('\n')
	line_count += 1
#	print line
	if (not volume_string):
		volume_string = find_volume(line)
#		print "Volume: ", volume_string 
	if (not issue_string):
		issue_string = str(find_issue(line))
#		print "issue: ", issue_string
	if (not date_string):
		date_string = str(find_date(line))
#		print "Date found: ", date_string
	if (not page_string):
	        page_string = str(find_pageno(line))
#		print "Page: ", page_string
	if (line_count >= Parse_limit):
		break

    sequence_count += 1
    #if ((found_volume) or (issue_number) or (found_date) or (found_pageno)):
    output_line =  double_quote + infile + double_quote + ","
    output_line += double_quote + date_string + double_quote + "," 
    output_line += double_quote + volume_string + double_quote + "," 
    output_line += double_quote + issue_string + double_quote + ","
    output_line += double_quote + page_string + double_quote + ","
    output_line += double_quote + str(sequence_count) + double_quote
    print "output: ", output_line 
    #else:
    #	print "No data found!"

    #csv_file = open(outfilename, 'a')
    #csv_file.write(output_line)
    #csv_file.close()
    OCR_File.close()
    filename = sys.stdin.readline()

import sys
import re
import os
import csv
from datetime import datetime

'''
parse_OCR_file

Parse the input file for #lines 
using the regex expressions, search input for Volume Number, Page, and Date
write result to CSV file when all variables found or #lines reached

'''

def extract_rightmost_string(raw_string):
	string_value = re.compile("(\w+|\d+)$")
	found_value = string_value.search(raw_string)
	return raw_string[found_value.start():found_value.end()]

def find_volume(line):
        volume = re.compile("(Volume|Vol.)\s(\w+|\d+)", re.IGNORECASE)
        found_volume = volume.search(line)
        if (found_volume):
		return extract_rightmost_string(line[found_volume.start():found_volume.end()])

def find_issue(line):
	number = re.compile("(number|num.|no.)\s\d+", re.IGNORECASE)
        issue_number = number.search(line)
        if (issue_number):
                return extract_rightmost_string(line[issue_number.start():issue_number.end()])

def find_date(line):
	pdate  = re.compile("(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)\s\d+,\s\d+", re.IGNORECASE)
        found_date = pdate.search(line)
        if (found_date):
		return line[found_date.start():found_date.end()]

def find_pageno(line):
	pageno = re.compile("(PAGE|PG)\s*(\w+|\d+)", re.IGNORECASE)
	found_pageno = pageno.search(line)
	if (found_pageno):
		return extract_rightmost_string(line[found_pageno.start():found_pageno.end()])

def import_value(var_name):
        return os.environ[var_name]  



Parse_Limit = int(import_value("Parse_Limit"))
print Parse_Limit
outfile = str(import_value("CSV_output_file"))
print outfile
CSV_File = open(outfile, 'a');
csv_writer = csv.writer(CSV_File, delimiter=',', quotechar='\"')
filename = str(import_value("OCR_File"))
print filename


# initial setup

line_count = 0
double_quote = "\""
date_string = None
volume_string = None
issue_string = None
page_string = None

# start Main

with open(filename) as OCR_File:	
    for line in OCR_File:
	line_count += 1
	# search through the line for the strings
        if  (volume_string is None):
                volume_string = find_volume(line)
#                print "Volume: ", volume_string 
	if (issue_string is None):
		issue_string = find_issue(line)
#		print "issue: ", issue_string
	if (date_string is None):
		date_string = find_date(line)
#		print "Date found: ", date_string
	if (page_string is None):
		page_string = find_pageno(line)
#		print "Page found: ", page_string
	if (line_count >= Parse_Limit):
		break

# Write output to the CSV file
csv_writer.writerow((filename, date_string, volume_string, issue_string, page_string))
OCR_File.close()
CSV_File.close()


exit()

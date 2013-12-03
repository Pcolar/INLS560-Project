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

def find_volume(line):
        volume = re.compile("(Volume|Vol.)\s(\w+|\d+)", re.IGNORECASE)
        string_value = re.compile("(\w+|\d+)$")
        found_volume = volume.search(line)
        if (found_volume):
                raw_substring = line[found_volume.start():found_volume.end()]
                found_value = string_value.search(raw_substring)
                volume_string = raw_substring[found_value.start():found_value.end()]
                return volume_string


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
date_string = ""  
volume_string = None
issue_string = ""
page_string = ""
volume = re.compile("(Volume|Vol.)\s(\w+|\d+)", re.IGNORECASE)
number = re.compile("(number|num.|no.)\s\d+", re.IGNORECASE)
pdate  = re.compile("(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)\s\d+,\s\d+", re.IGNORECASE)
pageno = re.compile("(PAGE|PG)\s*(\w+|\d+)", re.IGNORECASE)
string_value = re.compile("(\w+|\d+)$")

# start Main

with open(filename) as OCR_File:	
    for line in OCR_File:
	line_count += 1
	# search through the line for the strings
#	volume_string = find_volume(line)
#	if (found_volume):
#		print "Volume found:", found_volume.span(), ":", line[found_volume.start():found_volume.end()]
#		raw_substring = line[found_volume.start():found_volume.end()]
#		found_value = string_value.search(raw_substring)
#		volume_string = raw_substring[found_value.start():found_value.end()]
#	print "Volume: ", volume_string 
        if  (volume_string is None):
                volume_string = find_volume(line)
                print "Volume: ", volume_string 
	issue_number = number.search(line)
	if (issue_number):
		print "Issue found:", issue_number.span(), ":", line[issue_number.start():issue_number.end()]
		raw_substring = line[issue_number.start():issue_number.end()]
		found_value = string_value.search(raw_substring)
		issue_string = raw_substring[found_value.start():found_value.end()]
		print "issue: ", issue_string
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
#	if ((found_volume and issue_number and found_date and found_pageno) or 
	if (line_count >= Parse_Limit):
		break

csv_writer.writerow((filename, date_string, volume_string, issue_string, page_string))
OCR_File.close()
CSV_File.close()
exit()

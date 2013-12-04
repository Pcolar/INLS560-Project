import sys
import re
import os
import csv
from datetime import datetime

from regex_library import *

'''
parse_OCR_files from Stdin

Input:  (stdin) filename to be parsed
        output CSV filename
        # of lines to be parsed

Parse the input file for #lines 
using the regex expressions, search input for Volume Number, Page, and Date
write result to CSV file when all variables found or #lines reached

'''
Parse_Limit = int(import_value("Parse_Limit"))
outfile = str(import_value("CSV_output_file"))
CSV_File = open(outfile, 'a');
csv_writer = csv.writer(CSV_File, delimiter=',', quotechar='\"')
sequence_count = 0

# start Main
filename = sys.stdin.readline()  # read a filename from stdin
while filename:
  infile = filename.rstrip('\n')
  print "Processing: ", infile
  with open(infile) as OCR_File:	
    # clear variables for this file
    line_count = 0
    double_quote = "\""
    date_string = None
    volume_string = None
    issue_string = None
    page_string = None

    # parse the input file
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
    sequence_count += 1
    # Write output to the CSV file
    csv_writer.writerow((infile, date_string, volume_string, issue_string, page_string, sequence_count))
    OCR_File.close()
    # get the next filename from stdin
    filename = sys.stdin.readline()

CSV_File.close()
exit()

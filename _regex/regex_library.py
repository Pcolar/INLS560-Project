import sys
import re
import os
import csv
from datetime import datetime

'''
Regex Library

Location for functions and regex strings

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



import sys
import csv

### csv_template_manager library
###
###  implement functions to populate a csv template with metadata
###

###  Setup for initial code test

#total_args = int(len(sys.argv))
#if ( total_args <> 3 ):
#	print("Two input arguments are required -")
#	print(" (filename to be parsed) and (# of lines to parse)")
#	print("Script name: %s" % str(sys.argv[0]))
#	for i in xrange(total_args):
#    		print ("Argument # %d : %s" % (i, str(sys.argv[i])))
#	exit(1)

Inputfile   = '../_templates/WCC.csv'
Outputfile  = '../test_output.csv'


#  def open_init(Inputfile):
'''
	Input: Inputfile
	Opens the template and output file
	Transfers the header information
	returns the template line as a single string
'''
csv_input  = csv.reader(open(Inputfile, 'rb'))
csv_header = csv_input.next()
for csv_MD_Template in csv_input:
	print(csv_header)

#  def open_init_output
'''
	Input Outputfile
	Opens the output file
	writes the header line
	returns the file handle
'''
csv_output = csv.writer(open(Outputfile, 'w'))
csv_output.writerow(csv_header)

print(csv_MD_Template)
exit

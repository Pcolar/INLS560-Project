#!/bin/bash
#set -x
export Parse_Limit=15
export CSV_output_file="testfile.csv"
#export OCR_File="/home/pcolar/OCR-Parser/_data/dailytarheel_june15_1946_dec12_1946_0001.txt"

#find $1 -type f -name *.txt 

ls --width=50 $1 | python ~/OCR-Parser/_regex/parse_OCR_file.py

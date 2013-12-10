Getting Started 
OCR-Parser
===============

## Requirements

* command line (shell) access 
* Python
* Standard *nix utilities (grep, find, ls, etc.)

## OCR Files

* OCR output of the image files returned from digitization
  * these should be flat text files, no XML, rtf, or other encoding
* Files must be accessible to the program 
  * Locally stored
  * Accessible via a network file system

##Usage

* Project File organization
  * _data - some sample test data, can be ignored
  * _regex - executable python scripts and libraries for parsing the OCR text files
  * _scripts - shell scripts to automate running the program and set up the environment
  * _templates - example CSV files from our site
  * _utility - utility programs and scripts to prepare and organize files

* Running the program
  * _scripts/parse_OCR_file.py
    * accepts a list of files to STDIN to be processed (*needs more definition*)
    * obtains startup information from shell variables
        * Parse_Limit - # of lines in the input file to parse for metadata
        * CSV_output_file - filename of the spreadsheet file produced by the program 
            * it will append to an existing file
  *  _scripts / run_parse_OCR.sh
    * sets up the environment and runs the program
    * needs to be tweaked for your environment
    * chmod +x run_parse_OCR.sh (to permit execution of the script)

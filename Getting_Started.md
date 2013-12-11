Getting Started 
OCR-Parser
===============

## Requirements

* command line (shell) access
  * while this is typically done from a linux operating system, the following video can assist windows users http://www.youtube.com/watch?v=VlqpiKHz7Gw
* Python
* Standard *nix utilities (grep, find, ls, etc.)

## OCR Files

* OCR output of the image files returned from digitization
  * these should be flat text files, no XML, rtf, or other encoding
* Files must be accessible to the program 
  * Locally stored
  * Accessible via a network file system
* Files should be ordered sequentially for each batch

##Usage

*File Prep
  Save all of the files from github in a folder called OCR-Parser with subfolder like they are 
  arranged on github
  
  ![File Arrangement](http://farm8.staticflickr.com/7428/11314863716_a43b9b1f47_o.png)
  
  Save all of the OCR text files in the data folder in sequential order
  
  ![Text Files](http://farm3.staticflickr.com/2858/11314938023_bb4a984501_o.png)

*Run the Program
  In a new terminal change directories to OCR-Parser:
  
  ![Change Directories](http://www.unc.edu/~epeele/file/parser_cd.png)
  
  Run the program by typing 
  ```
  ~/OCR-Parser/_scripts/run_parse_OCR.sh  ~/OCR-Parser/_data
  ```

  ![Run Program](http://www.unc.edu/~epeele/file/parser_program.png)
  
  You should see all of the text files processing like this
  
  ![Processing](http://www.unc.edu/~epeele/file/parser_processing.png)
  
  The default setup is to append data to 'testfile.csv' 
  
  ![Cat](http://www.unc.edu/~epeele/file/parser_cat.png)
  
  The output will display for each file  
  
  ![Output](http://www.unc.edu/~epeele/file/parser_output.png)
  
  The CSV file will save in your OCR-Parser folder with the data
  
  ![testfile.CSV](http://www.unc.edu/~epeele/file/parser_testfile.png)
  
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

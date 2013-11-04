import re

volume = re.compile("(Volume|Vol)\s(\w+|\d+)")
number = re.compile("(number|num|no)\s\d+")
date   = re.compile("January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec")



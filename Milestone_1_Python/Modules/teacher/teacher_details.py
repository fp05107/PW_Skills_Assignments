# A file with py extension is a Python module.
# Collection of modules organized in a directory is called package
# Collection of modules and packages is a library

import os, sys
from os.path import dirname, join, abspath

parent_dir_path = abspath(join(dirname(__file__), ".."))
print("🚀 ~ parent_dir_path:", __file__)
print("🚀 ~ parent_dir_path:", parent_dir_path)
sys.path.insert(0, parent_dir_path)
from student import student_details

def teacher():
    print('This is teacher details...')

student_details.student()
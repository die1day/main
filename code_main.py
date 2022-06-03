# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 07:24:08 2022

@author: Jeff

how to import from a different paranet path
https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

a method withou changing sys.path, withour adding __init__.py file
https://stackoverflow.com/questions/22955684/how-to-import-py-file-from-another-directory
"""

# import sys
# sys.path.insert(1, r'C:\Users\Jeff\git_test')
# sys.path.remove(r'C:\Users\Jeff\git_test')
# sys.path

# from git_test.sub1.code_sub1 import cal
# from code_sub1 import cal



# from ...sub1.code_sub1 import cal

# from ..sub1.code_sub1 import cal
# from .sub1.code_sub1 import cal
# __package__

# from .sub1 import code_sub1

# code_sub1.cal(1,2)

# from sub2 import code_sub2
# code_sub2.


import importlib.machinery

loader = importlib.machinery.SourceFileLoader('sub1', r'C:\Users\Jeff\git_test\sub1\code_sub1.py')
handle = loader.load_module('sub1')

print(handle.cal(5,10))

loader2 = importlib.machinery.SourceFileLoader('sub2', r'..\sub2\code_sub2.py')
handle2 = loader2.load_module('sub2')
handle2.get_table()

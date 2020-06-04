import bdb
"""
PDB
Python DeBugger

you have to import 

import pdb; pdb.set_trace()
"""

first = "First"
second = "Second"
bdb.set_trace()
result = first + second

third = "Third"
result += third
print(result)

# import pdb
# import pdb.set_trace()

# also commonly on one line:
# pdb.set_trace()

# common pdb commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

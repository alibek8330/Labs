print(6 & 3)

"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 | 3)
"""
The | operator compares each bit and 
set it to 1 if one or both is 1, 
otherwise it is set to 0:
"""
print(6 ^ 3)
"""
The ^ operator compares each bit and 
set it to 1 if only one is 1, 
otherwise (if both are 1 or both are 0) it is set to 0:
"""
print(~3)
"""
The ~ operator 
inverts each bit (0 becomes 1 and 1 becomes 0).
"""
print(3 << 2)
"""
The << operator inserts the specified number of 0's 
(in this case 2) from the right
 and let the same amount of leftmost bits fall off:
"""
print(8 >> 2)
"""
The >> operator moves each bit the specified number of 
times to the right. Empty holes at the left are filled with 0's.
"""


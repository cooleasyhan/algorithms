"""
http://www.geeksforgeeks.org/find-the-element-that-appears-once/
"""

#%%
i = 3
j = 5
print('i', i, bin(i))
print('j', j, bin(j))
_or = i | j
_and = i & j
_xor = i ^ j
_i_turn = ~i
_j_turn = ~j


print('or', _or, bin(_or))
print('and', _and, bin(_and))
print('xor', _xor, bin(_xor))
print('_i_turn', _i_turn, bin(_i_turn))
print('_j_turn', _j_turn, bin(_j_turn))
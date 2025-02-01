"""
Idea is simple, from index end to 0,
if you find a position i where [i-1] > [i], then [i-1] -= 1 and from i, fill 9
for example:
    123 41 789
position i is 5, [4] > [5] ==> 4 > 1, so 123 39 999

for example:
    332
i = 2, 329
i = 1, 299
"""
"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

start=1020304050607080900
end=1929394959697989990

import math
for i in range(int(math.sqrt(start)),int(math.sqrt(end))):
    if i%10==0:
        if str(i*i)[::2]==str(start)[::2]:
            print(i)
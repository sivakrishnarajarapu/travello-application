# Given array of integers, check if it represents either a strictly increasing or a strictly decreasing sequence.

# def fun(s):
#     z=len(s)-1
#     if z==0:
#         return  True
#     a=[s[i+1]-s[i] for i in range(z)]
#     if 0 in a:
#         return False
#     a=set([i/abs(i) for i in a])
#     return len(a)==1
# print(fun([1,4,5,7,3,9]))

import json
import pandas as pd
ls=[1,2,3,(4,5)]
# ls1=dict(ls)
# json.dumps(ls)
print(json.dumps(ls))
# df=pd.DataFrame(ls)
# print(df)
# df1=to_dict(df)




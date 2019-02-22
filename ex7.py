res_dict = dict()

# Checks if the arguments are already in the results dict.
# If not, adds the result to the dictionary and return result.
# If it is in the dictionary, returns the result.
def big_func(a, b, c):
    tup = (a,b,c)
    if tup not in res_dict:
        res_dict[tup] = a + b + c   # <--- big calculation here
    return res_dict[tup]

# You can debug and see it work!
big_func(3,4,5)
big_func(3,4,5)
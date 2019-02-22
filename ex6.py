# returns the list l after the function f 
# is ran on every element in the list.
def Map(f, l):
    return [f(i) for i in l]

def double_string(x):
    return str(x)*2

print(Map(double_string, [2,5,4,3]))
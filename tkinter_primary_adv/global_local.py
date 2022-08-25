
a = 1000 # global

def func_a():
    # 1. 
    a = 10  # local
    
    # 2.
    # global a
    
    print(a)

print(a)
func_a()
print(a)
t = 1000

def funcA():
    global t
    t = 3000
    print(t)

print(t)
funcA()
print(t)
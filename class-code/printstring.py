#print string

print("hello number " + str(2))
print("hello number", 2)    
#When using comma, it will print space between them

print("hi number", end="")
print(2)


a = 12
res1 = print(2 + 3, a)
#print(res1 + 7)    ERROR:res1 is None
res2 = min(2 + 3, a)

print(print(1), print(2))
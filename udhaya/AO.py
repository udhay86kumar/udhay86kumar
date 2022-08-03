a = int(input("Enter the A value: "))
b = int(input("Enter the B value:"))
add = a+b
sub = a-b
mul=a*b
div = a/b
mod =a%b
print("Sum: {0},{1},{2},{3},{4}".format(add,sub,mul,div,mod))#python using format
print("Sum: %d,Diff: %d,Mul: %d,Div: %25.3f,Mod: %d"%(add,sub,div,mul,mod))#python using padding 

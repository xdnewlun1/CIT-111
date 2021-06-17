value = int(input("Num: "))
#All Numbers
def even(x):
    if(x==0):
        return "Even"
    elif(x==1):
        return "Odd"
    return(even(x-2))

def prepNum(x):
    while x > 1995:
        x -= 1000
    return x

print(f"{even(abs(prepNum(value)))}")
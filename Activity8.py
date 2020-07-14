numbers=list(input("Enter the numbers comma separated ").split(","))
length=len(numbers)
print(length)
if numbers[0]==numbers[-1] :
    print("true")
else:
    print("false")
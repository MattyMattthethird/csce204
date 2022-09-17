print("Let's Count!")
start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

numbers = 0
if start > end:
    print("The start should be before the end.")
else:
    for n in range(end-start+1):
        numbers += 1
        if n+start == end:
            print(n+start)
        else:
            print(n+start, end=", ")
    print("There are ", numbers, " nubmers.")

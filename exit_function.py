def exit_function():
    total=0
    count=0
    for i in range(10):
        count+=1
        total+=i
        if total>5:
            return print(f"The count is {count} and the total is {total}.")
exit_function()
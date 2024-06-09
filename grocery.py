groceries = {}

print("Enter grocery item:")
while True:
    try:
        grocery_item = input().upper()
        if grocery_item in groceries:
            groceries[grocery_item] += 1
        else:
            groceries[grocery_item] = 1
    except EOFError:
        for grocery in groceries:
            print(f"{groceries[grocery]} {grocery} ")
        break

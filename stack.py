stack = ['apple', 'ball', 'cat', 'dog']

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if empty")
    print("5. Display")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        item = input("Enter item: ")
        stack.append(item)
        print("Item pushed.")
    elif choice == '2':
        if stack:
            print("Popped:", stack.pop())
        else:

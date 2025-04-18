try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))

    print("Choose calculation: \n",
          "1. Addition\n",
          "2. Subtraction\n",
          "3. Multiplication\n",
          "4. Division\n")
    
    cal = input().strip().lower()
    
    if cal == "addition":
        ans = num_1 + num_2
    elif cal == "subtraction":
        ans = num_1 - num_2
    elif cal == "multiplication":
        ans = num_1 * num_2
    elif cal == "division":
        if num_2 == 0:
            print("Cannot divide by zero.")
            ans = None
        else:
            ans = num_1 / num_2
    else:
        print("Invalid operation. Please choose from addition, subtraction, multiplication, or division.")
        ans = None

    if ans is not None:
        print(f"The result of {cal} is: {ans}")
except ValueError:
    print
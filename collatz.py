def collatz(number): # Collatz project from chapter 4
    try:
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
            else:
                number % 2 == 1
                number = 3 * number + 1
                print(number)
    except ValueError:
        print('Hey, only integer is allowed')

collatz(int(input('User input: ')))

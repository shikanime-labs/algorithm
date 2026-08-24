def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz", end="")
            if i % 5 == 0:
                print("Buzz")
            else:
                print()
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzBuzz(100)

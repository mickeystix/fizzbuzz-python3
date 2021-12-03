n = 100 # Change this input to test values

def fizzBuzz(n):
    for i in range(1, n + 1):
        print("Fizz"*(i%3<1)+(i%5<1)*"Buzz" or i) 
# In simple terms this Prints "Fizz" X times and/or "Buzz" X times depending on if the modulus value returns a 1 or 0
# If both modulus values return 0, it prints the original value

if __name__ == '__main__':
    fizzBuzz(n)

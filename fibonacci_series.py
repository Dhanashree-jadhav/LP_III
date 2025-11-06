# Fibonacci Series (Non-Recursive) with Step Count


# non recursssive
# Input from user
#n = int(input("Enter number of terms: "))

#a, b = 0, 1
#step_count = 0

#print("Fibonacci Series:")

# Loop to generate Fibonacci series
#for i in range(1, n + 1):
#    print(a, end=" ")
#    c = a + b
#    a = b
#    b = c
#    step_count += 1  # Count each loop as one step

#print("\nTotal Steps:", step_count)



#Recursive
# Recursive Fibonacci with Step Count

# Global variable to count recursive calls
step_count = 0

# Recursive function to find Fibonacci number
def fibonacci(n):
    global step_count
    step_count += 1  # Count every function call
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Main program
n = int(input("Enter number of terms: "))
print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")

print("\nTotal Steps (recursive calls):", step_count)

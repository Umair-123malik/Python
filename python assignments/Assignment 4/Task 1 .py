def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    # Gather user's name and favorite numbers
    name = input("Enter your name: ")
    numbers = []
    
    for i in range(1, 4):
        number = int(input(f"Enter your {i} favorite number: "))
        numbers.append(number)
    
    # Greet the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")
    
    # Determine if the numbers are even or odd
    even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    for num, eo in even_odd_list:
        print(f"The number {num} is {eo}.")
    
    # Create and print tuples of numbers and their squares
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num ** 2})")
    
    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
    
    # Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number, but it's still a cool number!")

# Run the program
if __name__ == "__main__":
    main()

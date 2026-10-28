def square(n):
    return n * n

num = int(input("Enter a number: "))
print("Square:", square(num))

def even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

nums = [10, 15, 20, 25, 30]
print("Even numbers:", even_numbers(nums))

def reverse_string(text):
    return text[::-1]

word = input("Enter a string: ")
print("Reversed string:", reverse_string(word))

def is_positive(num):
    return num > 0

n = int(input("Enter a number: "))
print(is_positive(n))

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

nums = [10, 20, 30, 40, 50]
print("Average:", average(nums))

celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

c = float(input("Enter Celsius: "))
print("Fahrenheit:", celsius_to_fahrenheit(c))

def largest(*args):
    return max(args)

print("Largest:", largest(10, 50, 30, 80, 20))

def display_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_details(
    name="Santhosh",
    age=22,
    skill="Python",
    role="Developer"
)

def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count

word = input("Enter a string: ")
print("Vowel count:", count_vowels(word))

def final_price(price, discount):
    discount_amount = price * discount / 100
    return price - discount_amount

price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

if price >= 0 and 0 <= discount <= 100:
    print("Final price:", final_price(price, discount))
else:
    print("Invalid price or discount")
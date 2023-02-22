def prime_numbers(number):
  is_prime = True
  for i in range(2, number):
      if number % i == 0:
        is_prime = False
  if is_prime:
    print("it's a Prime number")
  else:
    print("it's not a Prime Number")

n = int(input("check the number "))
prime_numbers(number=n)
      
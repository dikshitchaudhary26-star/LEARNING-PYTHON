#CHECK PRIME A FASTER METHOD

num = int(input("ENTER THE NUMBER: "))

if num < 2:
    print(f"{num} IS NOT A PRIME NUMBER")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} IS A PRIME NUMBER")
    else:
        print(f"{num} IS NOT A PRIME NUMBER")

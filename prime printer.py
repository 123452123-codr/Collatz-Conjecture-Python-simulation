import json

a = int(input("Enter the limit till which you want the primes:"))
prime_set = []

for i in range(2,a+1,1):
    p = int(i/2)
    prime = 1
    for j in range(2,p+1,1):
        if(i % j == 0):
            prime = 0
            break
    if(prime == 1):
        print(i,"\n")
        prime_set.append(i)
        prime_json = {a : prime_set}
        with open('prime_data.json', 'w') as file:
            for j in prime_json:
                json.dump(prime_json, file, indent=2)
    else:
        waste = 1
no_of_primes = len(prime_set)
percent_primes = (no_of_primes/a) * 100
print("There are {} primes between 1 and {} and their percentage is {}%".format(no_of_primes, a, percent_primes))
    
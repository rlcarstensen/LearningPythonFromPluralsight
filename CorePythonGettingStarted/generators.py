def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, list(distinct(items))):
        print(item)

run_pipeline()

# infinite loop!!!
# def lucas():
#     yield 2
#     a = 2
#     b = 1
#     while True:
#         yield b
#         a, b = b, a + b

# for x in lucas():
#     print(x)

from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

from itertools import count, islice
thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
thousand_primes
list(thousand_primes)[-10:]
sum(islice((x for x in count() if is_prime(x)), 1000))

any(is_prime(x) for x in range(1328, 1361))
all(name == name.title() for name in ['London', 'Paris', 'Tokyo', 'New York', 'Sydney', 'Kuala Lumpur'])

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
for item in zip(sunday, monday):
    print(item)

for sun, mon in zip(sunday, monday):
    print("average=", (sun + mon) / 2)

tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

for temps in zip(sunday, monday, tuesday):
    print(f"min = {min(temps):4.1f}, max = {max(temps):4.1f}, average = {sum(temps) / len(temps):4.1f}")

from itertools import chain
tempuratures = chain (sunday, monday, tuesday)
all(t > 0 for t in tempuratures)

# for x in (p for p in lucas() if is_prime(p)):
#     print(x)
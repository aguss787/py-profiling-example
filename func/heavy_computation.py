from typing import List


def slow_generate_prime(n: int) -> List[int]:
    """
    Generate a list of prime numbers up to n.
    """
    prime = [2]
    for i in range(3, n + 1, 2):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
    return prime


def generate_prime(n: int) -> List[int]:
    """
    Generate a list of prime numbers up to n.
    """
    prime = [2]
    for i in range(3, n + 1, 2):
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime

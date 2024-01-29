import random

def has_duplicate_birthdays(n):
    birthdays = [random.randint(1, 365) for _ in range(n)]
    return len(birthdays) != len(set(birthdays))

def test_birthday_paradox():
    for n in range(5, 101, 5):
        count = 0
        experiments = 10000
        for _ in range(experiments):
            if has_duplicate_birthdays(n):
                count += 1
        probability = count / experiments
        print(f"For a group of {n} people, probability of two people having same birthdays is {probability:.4f}")

test_birthday_paradox()

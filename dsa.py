#The dice problem

def oppositeFaceOfDice(n):
    if n == 1:
        return 6
    elif n == 2:
        return 5
    elif n == 3:
        return 4
    elif n == 4:
        return 3
    elif n == 5:
        return 2
    else:
        return 1

n = 2
print(oppositeFaceOfDice(n))


def secondSolution(n):
    return 7-n

n = 1
print(secondSolution(n))

#==========================
# Given two integers n and m, find the closest integer to n that is divisible by m.
#===========================
def closest_number(n, m):
    # find the quotient
    closest = 0
    min_difference = float('inf')

    # Check numbers around n
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n - i)

            if difference < min_difference or \
            			(difference == min_difference and abs(i) > abs(closest)):
                closest = i
                min_difference = difference
    return closest

  
if __name__ == "__main__":
  n = 13
  m = 4
  print(closest_number(n, m))
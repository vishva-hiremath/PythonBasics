import pdb


def sum_of_squares(n):
    total = 0
    for i in range(n): # Should maybe be range(1, n + 1)? Or is the logic wrong?
        print(i)
        # Let's pause execution right before the calculation in the loop
        pdb.set_trace()
        total += i * i + 1 # <--- Potential bug here? Let's investigate
    return total

result = sum_of_squares(3)
print(f"The result is: {result}") # Expected maybe 1^2 + 2^2 + 3^2 = 14?

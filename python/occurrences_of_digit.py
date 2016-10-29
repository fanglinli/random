# occurrences_of_digits:
#   Returns the number of times digit L occurs as a digit of numbers in range [0, n)
def occurrences_of_digits(L, n):
    occurrences, L = 0, str(L)              # occurrences: counter for number of occurrences of L. Convert L to string.

    for number in xrange(n):                # For all numbers in range [0, n)
        for digit in list(str(number)):     # For digits of number.
            if digit == L:                  # If the digit is L.
                occurrences += 1            # Increment occurrences.

    return occurrences                      # Return the number of occurrences.

"""
Grey Relation Analysis implemented as one function get_gra_coeff(y, S), which for given reference sequence y and comperative set S returns list of grey relation coefficients for every comperative sequence in S.

# Y - reference sequence
# S = {X1, ... , Xm} - Set of comparative sequences. |S| = m
# Y, X1, ... , Xm - Sequences of n elements.
"""

import exceptions


# Returns an array, of length m, of grey relation coefficients (gra_coeff) one for each comparative sequence in S.
# Calculation depends on the choice of parameter xi from [0, 1]. Default is xi = 0.5
def get_gra_coeff(y, s, xi=0.5):

    n = len(y)  # Length of all sequences
    m = len(s)  # Number of comparative sequences m. Cardinality of S.

    # Check if all sequences are of the same length
    for seq in s:
        if n != len(seq):
            raise exceptions.SequncesAreOfDifferentLengths()

    # min |Y(i) - Xk(i)|. For i in [1, n] and k in [1, m]
    d_min = abs(y[0] - s[0][0])

    # min |Y(i) - Xk(i)|. For i in [1, n] and k in [1, m]
    d_max = abs(y[0] - s[0][0])

    # Calculate d_min and d_max
    for i in range(n):
        for k in range(m):
            d = abs(y[i] - s[k][i])

            if d < d_min:
                d_min = d

            if d > d_max:
                d_max = d

    # If d_max = 0 then all comparative sequences are identical to reference sequence
    if d_max == 0:
        gra_coeff = []

        for c in s:
            gra_coeff.append(1)

        return gra_coeff

    gra_coeffs = []  # Array of gra _coeffs of lenght m

    # Calculate gra_coeff for every comparative sequence
    for k in range(m):
        gra_coeff = 0

        for i in range(n):
            gra_coeff += (d_min + xi * d_max) / (abs(y[i] - s[k][i]) + xi * d_max)

        gra_coeff /= n

        gra_coeffs.append(gra_coeff)

    return gra_coeffs

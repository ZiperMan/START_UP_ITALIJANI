"""
Different models for estimating wind speed under wake effect.
"""

import math


# Turbine specification
alpha = 0.05  # wake expansion constant
a = 0.655  # thrust coefficient induction factor
r0 = 38.5  # radius of wind turbines

"""
############################################# Single Wake ################################################
"""


# Jensen’s wind speed prediction model
# v0 - free range wind speed
# x - downwind distance between turbines
def jansen(v0, x):
    return v0 * (1 + (math.sqrt(1 - a * (2 - a)) - 1) * (math.pow(r0 / (r0 + alpha * x), 2)))


# Frandsen’s wind speed prediction model
# v0 - free range wind speed
# x - downwind distance between turbines
def frandsen(v0, x):
    c = a * (2 - a)
    rx = r0 * math.sqrt((0.5 * (1 + math.sqrt(1 - c)) / math.sqrt(1 - c) + (alpha * x) / (2 * r0)))

    if a <= 0.5:
        return v0 * (0.5 + 0.5 * math.sqrt(1 - 2 * c * math.pow(r0 / rx, 2)))
    else:
        return v0 * (0.5 - 0.5 * math.sqrt(1 - 2 * c * math.pow(r0 / rx, 2)))


# Bilateral Gaussian wind speed prediction model
# v0 - free range wind speed
# x - downwind distance between turbines
# TODO: x1 - ??? WTF is x1 ???
def bil_gauss(v0, x, x1):
    c = a * (2 - a)
    sigma_j = (r0 + alpha * x) / math.sqrt(2)
    sigma_f = (r0 + alpha * x) / 2
    r2 = r0 + alpha * x1
    r = r0 + alpha * x
    A_j = (a / (sigma_j / (r2 * r2))) * math.exp((-r * r) / (2 * sigma_j * sigma_j))
    # TODO: nije dobra formula, dodao sam abs
    A_f = (1 - math.sqrt(abs(1 - c / (2 * math.pow(sigma_f / r0, 2))))) * math.exp((-r * r) / (2 * sigma_f * sigma_f))

    return v0 * (1 - A_j * A_f)


"""
########################################### Multiple Wake #################################################

Models for predicting effective wind speed for turbine T under the wake effect of turbines Ti for i = 1, ... , N
"""

# Additional parameters
A0 = 1  # TODO: A0 - ???WTF is A0???


# Calculating shadowing effect of two turbines on horizontal distance d and vertical distance x
def shadowing_effect(d, x):
    r = r0 + alpha * x

    return r0 * r0 * (1 / math.cos((d * d + r0 * r0 - r * r) / (2 * d * r0))) + r * r * (1 / math.cos((d * d + r * r - r0 * r0) / (2 * d * r))) - 0.5 * math.sqrt((math.pow(r0 + d, 2) - r * r) * (r * r - math.pow(r0 - d, 2)))


# v0 - free range wind speed
# x - Array of downwind (vertical) disctances for every turbine Ti, that has wake effect on T, to target turbine T
# d - Array of horizontal distances for every turbine Ti, that has wake effect on T, to target turbine T
def multi_wake_jansen(v0, x, d):
    j_sum = 0
    c = a * (2 - a)
    r = []

    for val in x:
        r.append(r0 + alpha * val)

    for i in range(len(x)):
        j_sum += 1 - math.sqrt(1 - c) * math.pow(r0 / r[i], 2) * (shadowing_effect(d[i], x[i]) / A0)

    return v0 * (1 - j_sum)


# TODO:
# v0 - free range wind speed
# x - Array of downwind (vertical) disctances for every turbine Ti, that has wake effect on T, to target turbine T
# d - Array of horizontal distances for every turbine Ti, that has wake effect on T, to target turbine T
def multi_wake_frandsen(v0, x, d):
    pass


# Bilateral Gaussian wind speed multiple wake prediction model
# v0 - free range wind speed
# x - Array of downwind (vertical) disctances for every turbine Ti, that has wake effect on T, to target turbine T
# d - Array of horizontal distances for every turbine Ti, that has wake effect on T, to target turbine T
# x1 - Array of ???WTF is x1??
def multi_wake_bill_gauss(v0, x, d, x1):
    c = a * (2 - a)
    bill_sum = 0

    for i in range(len(x)):
        sigma_j = (r0 + alpha * x[i]) / math.sqrt(2)
        sigma_f = (r0 + alpha * x[i]) / 2
        r2 = r0 + alpha * x1[i]
        r = r0 + alpha * x[i]
        A_j = (a / (sigma_j / (r2 * r2))) * math.exp((-r * r) / (2 * sigma_j * sigma_j))
        # TODO: nije dobra formula, dodao sam abs
        A_f = (1 - math.sqrt(abs(1 - c / (2 * math.pow(sigma_f / r0, 2))))) * math.exp((-r * r) / (2 * sigma_f * sigma_f))

        bill_sum += A_j * A_f * (shadowing_effect(d[i], x[i]) / A0)

    return v0 * (1 - bill_sum)

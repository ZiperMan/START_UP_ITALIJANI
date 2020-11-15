"""
Turbines are represented as coordinates (x, y).

All turbines are in the first quadrant.

All the turbines have the same radius r0.

Wind is blowing parallel to the X axis.

Input: fr_ws_ds - dataset of n recorded free range wind speeds, turbines - m turbines

Output: Matrix P of dimension nxm. Pij = prediction of wind speed in turbine j for free range wind speed i, using multi wake bilateral gaussian model assisted with GRA. i = 1,...,n and j = 1,...,m

This is implemented through the function predict_effective_wind_speed.
"""

import wind_forecasting_with_wake.effective_w_speed_pediction_models as pred_models
import gra


# Returns vertical distance between turbines t1 and t2
def calc_vert_dist(t1, t2):
    return abs(t1[1] - t2[1])


# Returns horizontal distance between turbines t1 and t2
def calc_horiz_dist(t1, t2):
    return abs(t1[0] - t2[0])


# Returns k turbines whose wake effect on target_turbine is the greatest. Uses GRA and single wake bilateral gaussian model.
# turbines - list of turbines (coordinates)
# fr_w_speeds - list of recorded free range wind speeds
# target_turbine - index of turbine for which we want to predict wind speed under the wake effect of others turbines.
# k - number of the most influential turbines we want to return
def find_influential_turbines(turbines, fr_w_speeds, target_turbine, k):
    len_turbines = len(turbines)  # Number of turbines
    infl_turbines = []  # Turbines with highest influence on target_turbine

    # Building set s of comparative sequences
    s = []

    for j in range(len_turbines - 1):
        s.append([])

    for i in range(len(fr_w_speeds)):
        for j in range(len_turbines):
            if j != target_turbine:
                x = calc_vert_dist(turbines[j], turbines[target_turbine])
                x1 = 1  # TODO: remove

                if j < target_turbine:
                    s[j].append(pred_models.bil_gauss(fr_w_speeds[i], x, x1))

                if j > target_turbine:
                    s[j - 1].append(pred_models.bil_gauss(fr_w_speeds[i], x, x1))

    # Calculate GRA coefficients for comparative set s using fr_w_speeds as reference sequence
    gra_coeffs = gra.get_gra_coeff(fr_w_speeds, s)

    # k lowest GRA coefficients
    k_lowest = sorted(gra_coeffs)[:k]

    # Choosing influential turbines as ones whose GRA coeff is in k_lowest
    for j in range(len_turbines):

        # Two sepparate cases because len(gra_coeffs) = len(turbines) - 1
        if j < target_turbine:
            if gra_coeffs[j] in k_lowest:
                infl_turbines.append(turbines[j])

        if j > target_turbine:
            if gra_coeffs[j - 1] in k_lowest:
                infl_turbines.append(turbines[j])

    return infl_turbines


# turbines - array of turbines aka (x,y) coordinates
# w_speed_ds - array of recored free range wind speeds
# k - number of turbines we want to consider when using multi wake models
# Returns matrix P of effective wind speed predictions
def predict_effective_wind_speed(turbines, fr_ws_ds, k):
    p = []

    for j in range(len(turbines)):
        p.append([])

    for j in range(len(turbines)):
        inf_turbines = find_influential_turbines(turbines, fr_ws_ds, j, k)

        # Calculate vertical and horizontal distance between turbine j and all turbines in inf_turbines
        vert_dist = []
        hor_dist = []
        x1 = []  # TODO: remove

        for t in inf_turbines:
            vert_dist.append(calc_vert_dist(turbines[j], t))
            hor_dist.append(calc_horiz_dist(turbines[j], t))
            x1.append(1)  # TODO: remove

        for i in range(len(fr_ws_ds)):
            p[j].append(pred_models.multi_wake_bill_gauss(fr_ws_ds[i], vert_dist, hor_dist, x1))

    return p

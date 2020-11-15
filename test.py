import gra
import wind_forecasting_with_wake.w_speed_under_wake_predictor as w_s_predictor
import wind_forecasting_with_wake.effective_w_speed_pediction_models as w_w_models

y = [1, 2, 3, 4, 5]

# x1 = [2, 2, 2, 2, 2]
# x2 = [1, 3, 2, 4, 5]
# x3 = [5, 4, 3, 2, 1]

x1 = [1, 2, 3, 4, 5]
x2 = [1, 2, 3, 4, 5]
x3 = [1, 2, 3, 4, 5]

s = []
s.append(x1)
s.append(x2)
s.append(x3)

# res = gra.get_gra_coeff(y, s)
# print(res)

fr_ws_ds = [20, 25, 15, 30, 20]  # Dataset of free range wind speeds

turbines = [(1, 3), (2, 2), (4, 5), (6, 3), (8, 4.5)]  # Coordinates of turbines

print(w_s_predictor.predict_effective_wind_speed(turbines, fr_ws_ds, 3))

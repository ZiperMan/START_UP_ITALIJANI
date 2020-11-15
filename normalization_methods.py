"""
Data (Sequence) Normalization Mehods
"""


# Simple normalization
def normalize(data):
    n_data = []
    d_min = min(data)
    d_max = max(data)

    for i in range(len(data)):
        n_data.append((data[i] - d_min) / (d_max - d_min))

    return n_data


# TODO:
# Initial value normalization
def initial_value_trans(seq):
    pass


# TODO:
# Average value normalization
def average_value_trans(seq):
    pass


# TODO:
# Polar difference normalization
def polar_diff_trans(seq):
    pass

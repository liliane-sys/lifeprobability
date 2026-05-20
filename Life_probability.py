#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:55:10 2025

Author: Liliane ML Burkhard
"""

"""
Life-probability bar-chart for Earth, ancient-Mars, Europa and Enceladus.
Edit the numbers in 'params' and 'parameter_errors' as you wish, then run.
"""

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# 1. Best-estimate parameters for each world
#    (N_o, f_w, f_e, f_c, f_l)
# --------------------------------------------------------------------------
params = {
    "Earth": {
        "N_o": 1.0,  # suitable conditions
        "f_w": 1.0,  # abundant water
        "f_e": 1.0,  # ample energy
        "f_c": 1.0,  # rich chemistry
        "f_l": 0.9,  # probability life emerges
    },
    "Mars": {
        "N_o": 0.95,  # early Mars: thick atm., lakes/oceans
        "f_w": 1.0,
        "f_e": 0.8,
        "f_c": 0.9,
        "f_l": 0.3,
    },
    "Europa": {
        "N_o": 1.0,
        "f_w": 1.0,
        "f_e": 0.7,
        "f_c": 0.8,
        "f_l": 0.2,
    },
    "Enceladus": {
        "N_o": 1.0,
        "f_w": 1.0,
        "f_e": 0.8,
        "f_c": 0.9,
        "f_l": 0.25,
    },
}

# --------------------------------------------------------------------------
# 2. Optional 1-σ uncertainties for each factor (same keys, same structure)
#    → replace zeros or adjust values to propagate error bars
# --------------------------------------------------------------------------
parameter_errors = {
    "Earth":      {"N_o": 0.0,  "f_w": 0.0,  "f_e": 0.0,  "f_c": 0.0,  "f_l": 0.05},
    "Mars":       {"N_o": 0.02, "f_w": 0.0,  "f_e": 0.05, "f_c": 0.05, "f_l": 0.10},
    "Europa":     {"N_o": 0.0,  "f_w": 0.0,  "f_e": 0.05, "f_c": 0.05, "f_l": 0.05},
    "Enceladus":  {"N_o": 0.0,  "f_w": 0.0,  "f_e": 0.05, "f_c": 0.05, "f_l": 0.08},
}

# --------------------------------------------------------------------------
# 3. Compute probabilities and error propagation (δP/P ≈ Σ δx_i/x_i)
# --------------------------------------------------------------------------
bodies = list(params.keys())
probs, prob_errors = [], []

for body in bodies:
    factors = params[body]
    P = np.prod(list(factors.values()))
    probs.append(P)

    # Simple linear propagation of relative errors
    rel_error = sum(
        parameter_errors[body][k] / v if v else 0.0
        for k, v in factors.items()
    )
    prob_errors.append(P * rel_error)

# --------------------------------------------------------------------------
# 4. Plot
# --------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(
    bodies,
    np.array(probs) * 100,
    yerr=np.array(prob_errors) * 100,
    capsize=6,
    edgecolor="black",
)
ax.set_ylabel("Estimated Probability of Life (%)")
ax.set_title("Habitability Probabilities with 1σ Error Bars")
ax.set_ylim(0, 100)
ax.grid(axis="y", linestyle=":", alpha=0.5)
plt.tight_layout()
plt.show()

# Tadaaaa

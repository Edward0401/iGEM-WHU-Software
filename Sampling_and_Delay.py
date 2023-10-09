
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Differential equation for promoter concentration with decreasing light (X)
def promoter_concentration_X(X, t, k1, k2, light_decay_rate):
    phi_light = np.exp(-light_decay_rate * t)
    return k1 * phi_light - k2 * X

# Differential equations for Van der Pol oscillator
def van_der_pol(state, t, mu):
    x, y = state
    dxdt = y
    dydt = mu * (1 - x**2) * y - x
    return [dxdt, dydt]

# Parameters for promoter concentration (X) with decreasing light
k1 = 1.0  # Rate constant for production of X
k2 = 0.2  # Rate constant for degradation of X
light_decay_rate = 0.1  # Rate at which light intensity decays

# Parameters for Van der Pol oscillator
mu = 10  # Nonlinearity parameter

# Initial conditions and time grid
initial_X = 0  # Initial concentration of X
initial_state = [2.0, 0]  # Initial state for Van der Pol oscillator [x, y]
t = np.linspace(0, 100, 1000)  # Time grid

# Solve differential equations
X_vals = odeint(promoter_concentration_X, initial_X, t, args=(k1, k2, light_decay_rate))
y_vals = odeint(van_der_pol, initial_state, t, args=(mu,))[:, 0]

# Threshold value
threshold = 2.2

# Generate the plots

# Combined Plot
plt.figure(figsize=(12, 6))
plt.plot(t, X_vals, label='Promoter Concentration with Decreasing Light (X)')
plt.plot(t, y_vals, label='Van der Pol Oscillator, mu=10')
plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
plt.xlabel('Time')
plt.ylabel('Concentration (X) / Oscillator Level (y)')
plt.title('Promoter Concentration and Van der Pol Oscillator Over Time')
plt.legend()
plt.show()

# Separate Plots
fig, axs = plt.subplots(2, 1, figsize=(12, 12))

# Plot for Promoter Concentration with Decreasing Light (X)
axs[0].plot(t, X_vals, label='Promoter Concentration with Decreasing Light (X)')
axs[0].axhline(y=threshold, color='r', linestyle='--', label='Threshold')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Concentration (X)')
axs[0].set_title('Promoter Concentration with Decreasing Light Over Time')
axs[0].legend()

# Plot for Van der Pol Oscillator with mu=10
axs[1].plot(t, y_vals, label='Van der Pol Oscillator, mu=10')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Oscillator Level (y)')
axs[1].set_title('Van der Pol Oscillator Over Time')
axs[1].legend()

plt.show()

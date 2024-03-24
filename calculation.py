from math import *

k = 0.92        # Thermal conductivity of concrete W/(mK)
#TE = 22.3       # Environment temperature (C)
TO = 17         # Outer temperature (C)
TI = 16.6       # Inner temperature (C)
TW = 13.6       # Water temperature (C)
V = 6.6/1000    # Tank volume (m^3)
Dx = 0.01       # Tank thickness (m)
Cs = 4184      # Specific heat of water J/(LK)

A = 4.*pi*(V*(3.0/(4.0*pi)))**(2/3) # Tank area (in square meters)
#print(f"Area: {A}")
flow = A * k * (TI - TO) / (Cs * Dx * (TW - TI))
flow_per_hr = flow * 60 * 60
print(f"Flow rate: {flow} liters/sec = {flow_per_hr} L/hr")

# %matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import math

def equation(x):
    return 667.38/x*(1-math.pow(np.e, -0.146843*x))-40

x_low = 12.0
x_high = 16.0
error_a = 0.01
analytical_result = 14.785

iterations = 0
error_a_iterations = math.nan
x_c_previous = 0

plt.plot(x_high,equation(x_high),'mo')
plt.plot(x_low,equation(x_low),'mo')
print("Iteration \t x_low \t x_high \t true_error \t relative_error")
while((error_a_iterations > error_a) or (math.isnan(error_a_iterations))):
    x_c_current = x_high - ((equation(x_high)*(x_low - x_high))/(equation(x_low) - equation(x_high)))
    f_x_low = equation(x_low)
    f_x_c = equation(x_c_current)
    plt.plot(x_c_current,f_x_c,'mo')
    if (f_x_low*f_x_c < 0):
        x_high = x_c_current
    else:
        x_low = x_c_current
    error_true = np.abs((analytical_result - x_c_current)/analytical_result)*100
    if (iterations > 0):
        error_a_iterations = np.abs((x_c_current - x_c_previous)/x_c_current)*100
    print("\t", iterations, "\t", round(x_low, 5), "\t", round(x_high, 5), \
          "\t", round(error_true, 5), "\t", round(error_a_iterations, 5))
    x_c_previous = x_c_current
    iterations += 1

print("\nx =", x_c_current, "whit relative_error = (+/-)", error_a, "%")

#*************************************************************************
x = np.linspace(12, 16, num = 100)
f_x = []

for i in range(len(x)):
    f_x.append(667.38/x[i]*(1-math.pow(np.e, -0.146843*x[i]))-40)

plt.plot(x, f_x)
plt.scatter(x_c_current, 0, color = 'r')
plt.grid()
plt.axvline(12, color = 'r')
plt.axvline(16, color = 'r')
plt.axhline(color = 'k')
plt.show()
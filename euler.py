import numpy as np
import matplotlib.pyplot as plt


def euler(f,y_0,step,t_0,T):
    """Classic Euler Method for solving differential equations"""
    """Use this in orde to solve the problems of type y' = f(t,y)"""
    """Choose an appropriate step size and an appropriate initial value to solve the problem"""
    
    number_steps = np.arange(t_0, t_0 + T + step, step)
    y = [y_0]

    for j in range(0,len(number_steps)-1):

        dt = step
        y_n = y[j] + dt * f(number_steps[j],y[j])
        y.append(y_n)

    return number_steps , np.array(y)


# Example of Approximation problem

def f(t,y) :
    return 2 - np.exp(-4 * t) - 2*y

def exact_function(t):
    return 1 + 1/2 * np.exp(-4 * t) -1/2 * np.exp(-2 * t)

number_steps , y = euler(f=f, y_0=1, step=0.05, t_0=0, T=5)

# Plotting the reuslts and the exact results

plt.grid()
plt.plot(number_steps,y,label='Approximate Solution')
plt.plot(number_steps,exact_function(number_steps),label='exact')
plt.legend()
plt.show()
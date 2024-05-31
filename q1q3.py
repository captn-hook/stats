from scipy.integrate import quad
from scipy.optimize import fsolve

# The weekly demand for gas (in 1000s of gallons) in a particular production plant is a random variable X with pdf
# f(x) = | k( 1 - 1 / x^2 ), 1 <= x <= 3
#        | 0, otherwise 

def f(x, k):
    if x >= 1 and x <= 3:
        return k * (1 - 1 / x**2)
    else:
        return 0
    
def g(x):
    return x * f(x, 3/4)
    
def f_integrated(k):
    return quad(f, 1, 3, args=(k))[0] - 1

def f_integrated_2(k):
    return quad(f, 2, 3, args=(k))[0]

# 1. Find the constant k such as f(x) is a valid probability distribution function of X

# ∫ from 1 to 3 of k * (1 - 1 / x^2) dx = 1

# multiply by k and pull k out of the integral
# k * ∫ 1 - k * ∫ 1 / x^2

# integrate
# kx - k(-1/x)
# kx + k/x = k * (x + 1/x)

# evaluate at 3 and 1
# k * (3 + 1/3) = 10k/3
# k * (1 + 1) = 2k

# 10k/3 - 2k = 4k/3

# 4k/3 = 1 => k = 3/4

k = fsolve(f_integrated, 1)[0]
print("k = ", k) #0.75

# 2. Find the probability that the demand for gas exceeds 2 thousand gallons during a particular week

# P(X > 2) = ∫ from 2 to 3 of 0.75 * (1 - 1 / x^2) dx

# .75 * ∫ 1 - .75 * ∫ 1 / x^2

# integrate
# .75x - .75(-1/x)

# evaluate at 3 and 2
#   .75 * 3 - .75 * (-1/3) = 2.25 + .25  = 2.5
# - .75 * 2 - .75 * (-1/2) = 1.5 + .375 = 1.875
#                                        = .625

print("P(X > 2) = ", quad(f, 2, 3, args=(.75))[0]) #0.625

# 3. What is the weekly expected demand for gas

# E(X) = ∫ from 1 to 3 of x * 0.75 * (1 - 1 / x^2) dx

# ∫ 0.75 * x - 0.75 / x

# integrate
# .75 * x^2/2 - .75ln(x)

# evaluate at 3 and 1
# .75 * 9/2 - .75ln(3) = 3.375 - .75ln(3) = 2.5510407835
# .75 * 1/2 - .75ln(1) = .75/2 = .375

# 2.5510407835 - .375 = 2.176

print("E(X) = ", quad(g, 1, 3)[0]) #2.176
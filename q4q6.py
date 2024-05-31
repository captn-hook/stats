from scipy.integrate import quad
from numpy import exp
from math import sqrt
# Use the following pdf to answer questions #4 through #6. If the probability function of X equals 
# f(x) = e^(-x/7) / 7, 0 < x < +inf

def f(x):
    return exp(-x/7) / 7

def g(x):
    return x * f(x)

def h(x):
    return x**2 * f(x)


# 4. Find P(X > 2) 

# ∫ from 2 to +inf of e^(-x/7) / 7 dx

# substitute -x/7 = u => -1/7 dx, -∫e^u du = -e^u

# unsub u = -x/7 => -e^(-x/7)

# evaluate at +inf and 2
# -e^(-inf/7) = approaching 0
# -e^(-2/7) = -0.75147729307

# = 0.75147729307

print("P(X > 2) = ", quad(f, 2, float('inf'))[0]) #0.751477293075286

# 5. Compute the standard deviation of X 

# std = sqrt(E(X^2) - E(X)^2)

# E(X) = ∫ from 0 to +inf of x * e^(-x/7) / 7 dx
# E(X^2) = ∫ from 0 to +inf of x^2 * e^(-x/7) / 7 dx

# E(X) = ∫ x * e^(-x/7) / 7 dx
# substitute -x/7 = u => -1/7 dx, -∫xe^u du = -xe^u + ∫e^u du = -xe^(-x/7) + e^(-x/7)
# = -7x * e^(-x/7) + 7e^(-x/7)

# E(X^2) = ∫ x^2 * e^(-x/7) / 7 dx
# substitute -x/7 = u => -1/7 dx, -∫x^2e^u du = -x^2e^u + 2∫xe^u du = -x^2e^(-x/7) + 2(-xe^(-x/7) + e^(-x/7))
# = -7x^2 * e^(-x/7) + 14x * e^(-x/7) - 14e^(-x/7)

# 0 + 7, 0 + 0
# E(X) definate integral = 7 - 0 = 7

# 0 + 0 - 14, -inf + inf - 14
# E(X^2) definate integral = -14 + 14 = 0

ex1 = quad(g, 0, float('inf'))[0] 
ex2 = quad(h, 0, float('inf'))[0] 

#calulate upper and lower of ex2
upper = -7 * float('inf')**2 * exp(-float('inf')/7) + 14 * float('inf') * exp(-float('inf')/7) - 14 * exp(-float('inf')/7)
lower = -7 * 0**2 * exp(-0/7) + 14 * 0 * exp(-0/7) - 14 * exp(-0/7)
print("Upper: ", upper) # nan, 
print("Lower: ", lower) # -14
print(upper - lower)
print("E(X) = ", ex1)
print("E(X^2) = ", ex2)
var = ex2 - ex1**2
std = sqrt(var)

print("Standard Deviation = ", std) # 7


# calculate 0 to +inf of E(X) and E(X^2)

# 6. Find the median of X 


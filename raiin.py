from scipy.stats import norm

# The annual rainfall (in inches) in a certain region is normally distributed with µ = 38 and σ = 6. 
mu = 38
sigma = 6

# 7. What is the probability that in a given year the rainfall will exceed 50 inches? 
print("P(X > 50) = ", 1 - norm.cdf(50, mu, sigma)) #0.02275013194817921

# 8. What is the probability that in a given year the rainfall will be between 45 and 55 inches? 
print("P(45 < X < 55) = ", norm.cdf(55, mu, sigma) - norm.cdf(45, mu, sigma)) #0.11936923844268532

# 9. What is the probability that in 2 of the next 4 years the rainfall will exceed 50 inches? Assume that rainfall in different years are independent. 
p = 1 - norm.cdf(50, mu, sigma)
n = 4
k = 2
print("P(X > 50 in 2 of the next 4 years) = ", n * p**k * (1 - p)**(n - k)) #0.001977147509258365

# 10. Use the Central Limit Theorem to find the probability that the average rainfall will exceed 40 inches in the next 15 years. 

W9D-YINA QIAO- CH9 exercise 1
COLLAPSE
Page 338

Let S100 be the number of heads that turn up in 100 tosses of a fair coin. Use
the Central Limit Theorem to estimate
(a) P(S100 <= 45).
(b) P(45 < S100 < 55).
(c) P(S100 > 63).
(d) P(S100 < 57).
from scipy.stats import norm

# Parameters
n = 100  # Number of trials
p = 0.5  # Probability of success (head) in each trial
mu = n * p  # Mean
sigma = (n * p * (1 - p)) ** 0.5  # Standard deviation

# (a) P(S100 <= 45)
a = norm.cdf((45 - mu) / sigma)

# (b) P(45 < S100 < 55)
b = norm.cdf((55 - mu) / sigma) - norm.cdf((45 - mu) / sigma)

# (c) P(S100 > 63)
c = 1 - norm.cdf((63 - mu) / sigma)

# (d) P(S100 < 57)
d = norm.cdf((57 - mu) / sigma)

a, b, c, d

result: (0.15865525393145707, 0.6826894921370859, 0.004661188023718732, 0.9192433407662289)

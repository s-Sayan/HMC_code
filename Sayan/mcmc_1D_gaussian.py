import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mean, variance):
    """ Gaussian distribution formula """
    return (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-(x - mean)**2 / (2 * variance))

def metropolis_hastings(target_mean, target_variance, proposal_width, n_samples):
    samples = []
    current = np.random.randn()  # Start from a random point

    for i in range(n_samples):
        proposal = np.random.normal(current, proposal_width)  # Propose a new point

        # Calculate acceptance probability
        accept_prob = min(1, gaussian(proposal, target_mean, target_variance) / 
                             gaussian(current, target_mean, target_variance))

        # Accept or reject the proposal
        if np.random.rand() < accept_prob:
            current = proposal

        samples.append(current)

    return samples

# Parameters for the target distribution
target_mean = 0
target_variance = 1

# Number of samples to draw
n_samples = 100000

# Width of the proposal distribution
proposal_width = 1

# Run the Metropolis-Hastings algorithm
samples = metropolis_hastings(target_mean, target_variance, proposal_width, n_samples)

# Plot the results
plt.hist(samples, bins=50, density=True)
# Add the actual Gaussian distribution for comparison
x_values = np.linspace(min(samples), max(samples), 1000)
plt.plot(x_values, gaussian(x_values, target_mean, target_variance), 'r', label='Actual Distribution')
plt.title('MCMC Metropolis-Hastings Sampling')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

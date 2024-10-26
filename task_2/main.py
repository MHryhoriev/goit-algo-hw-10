import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

def f(x: float) -> float:
    """Define the function to be integrated."""
    return x ** 2

def monte_carlo_integration(a: float, b: float, num_samples: int) -> float:
    """
    Estimate the integral of a function using the Monte Carlo method.
    """
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)
    
    under_curve = np.sum(y_random < f(x_random))
    area = (b - a) * f(b) * (under_curve / num_samples)
    
    return area

def calculate_integrals(a: float, b: float, num_samples: int) -> tuple:
    """
    Calculate the integral using Monte Carlo and quad methods.
    """
    monte_carlo_value = monte_carlo_integration(a, b, num_samples)
    quad_value, _ = spi.quad(f, a, b)

    return monte_carlo_value, quad_value

def plot_integration(a: float, b: float) -> None:
    """
    Plot the function and the area under the curve between a and b.
    """
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
    plt.grid()
    plt.show()

def main() -> None:
    """Main function to execute the integration and plotting."""
    a = 0
    b = 2
    num_samples = 100000

    # Calculate integrals
    monte_carlo_value, quad_value = calculate_integrals(a, b, num_samples)

    # Print results
    print("Estimated integral value using Monte Carlo method:", monte_carlo_value)
    print("Integral value using quad:", quad_value)

    # Plot the integration
    plot_integration(a, b)

if __name__ == "__main__":
    main()

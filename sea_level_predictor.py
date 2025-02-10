import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load dataset
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    """Generates a scatter plot and predicts future sea level rise using linear regression."""
    
    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Observed Data", alpha=0.7)

    # First regression line: Using all available data
    slope_all, intercept_all, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = range(1880, 2051)
    plt.plot(years_extended, slope_all * years_extended + intercept_all, 'r', label="Best Fit Line (1880-2050)")

    # Second regression line: Using data from 2000 onward
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = range(2000, 2051)
    plt.plot(years_recent, slope_recent * years_recent + intercept_recent, 'g', label="Best Fit Line (2000-2050)")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)

    # Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()

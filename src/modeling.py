import pandas as pd
import pymc as pm
import numpy as np
import matplotlib.pyplot as plt
import arviz as az

def load_data(file_path):
    """Load and preprocess Brent oil price data."""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)  # Handle mixed formats
    df.set_index('Date', inplace=True)
    return df

def single_change_point_model(prices, dates):
    """Implement a single change point model for Brent oil prices."""
    n = len(prices)
    with pm.Model() as model:
        # Prior for change point index (discrete)
        tau = pm.DiscreteUniform("tau", lower=0, upper=n-1)
        
        # Priors for mean prices before and after change point
        mu_1 = pm.Normal("mu_1", mu=np.mean(prices), sigma=10)
        mu_2 = pm.Normal("mu_2", mu=np.mean(prices), sigma=10)
        
        # Common variance
        sigma = pm.HalfNormal("sigma", sigma=10)
        
        # Switch between means based on change point
        idx = np.arange(n)
        mu = pm.math.switch(tau > idx, mu_1, mu_2)
        
        # Likelihood
        observation = pm.Normal("obs", mu=mu, sigma=sigma, observed=prices)
        
        # Sampling
        trace = pm.sample(2000, tune=1000, return_inferencedata=True)
    return trace

def plot_results(df, trace, output_path):
    """Plot price series with change point and posterior distribution."""
    prices = df['Price'].values
    dates = df.index
    tau_posterior = trace.posterior["tau"].values.flatten()
    most_probable_tau = int(np.median(tau_posterior))
    change_date = dates[most_probable_tau]
    
    # Plot price series with change point
    plt.figure(figsize=(12, 6))
    plt.plot(dates, prices, label="Brent Oil Price")
    plt.axvline(change_date, color='r', linestyle='--', label=f"Change Point: {change_date.date()}")
    plt.title("Brent Oil Prices with Detected Change Point")
    plt.xlabel("Date")
    plt.ylabel("Price (USD/barrel)")
    plt.legend()
    plt.savefig(output_path + "/change_point.png")
    plt.show()
    
    # Plot posterior distribution of tau
    plt.figure(figsize=(12, 6))
    az.plot_posterior(trace, var_names=["tau"], kind="hist")
    plt.title("Posterior Distribution of Change Point Index")
    plt.savefig(output_path + "/tau_posterior.png")
    plt.show()
    
    return change_date, most_probable_tau

def quantify_impact(trace, df, tau_idx):
    """Quantify the impact of the change point."""
    summary = az.summary(trace, var_names=["mu_1", "mu_2"])
    mu_1 = summary.loc["mu_1", "mean"]
    mu_2 = summary.loc["mu_2", "mean"]
    percent_change = ((mu_2 - mu_1) / mu_1) * 100
    print(f"Mean Price Before: ${mu_1:.2f}")
    print(f"Mean Price After: ${mu_2:.2f}")
    print(f"Percentage Change: {percent_change:.2f}%")
    return mu_1, mu_2, percent_change

def main():
    # Load data
    df = load_data('C:/Users/Skyline/Change point analysis and statistical modelling/data/raw/BrentOilPrices.csv')
    prices = df['Price'].values
    
    # Run model
    trace = single_change_point_model(prices, df.index)
    
    # Plot results
    change_date, tau_idx = plot_results(df, trace, 'C:/Users/Skyline/Change point analysis and statistical modelling/docs')
    
    # Quantify impact
    mu_1, mu_2, percent_change = quantify_impact(trace, df, tau_idx)
    
    # Summary statistics
    summary = az.summary(trace, var_names=["mu_1", "mu_2", "sigma"])
    print("Model Summary:\n", summary)
    print(f"Most Probable Change Point: {change_date.date()} (Index: {tau_idx})")
    
    return trace, change_date, tau_idx

if __name__ == "__main__":
    trace, change_date, tau_idx = main()
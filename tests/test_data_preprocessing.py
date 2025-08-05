import pandas as pd
import pymc as pm
import numpy as np

def test_data_loading():
    df = pd.read_csv('C:/Users/Skyline/Change point analysis and statistical modelling/data/raw/BrentOilPrices.csv')
    assert not df.empty, "Dataframe is empty"
    assert 'Date' in df.columns, "Date column missing"
    assert 'Price' in df.columns, "Price column missing"

def test_model_runs():
    df = pd.read_csv('C:/Users/Skyline/Change point analysis and statistical modelling/data/raw/BrentOilPrices.csv')
    prices = df['Price'].head(100).values  # Small sample for testing
    with pm.Model() as model:
        tau = pm.DiscreteUniform("tau", lower=0, upper=len(prices)-1)
        mu_1 = pm.Normal("mu_1", mu=np.mean(prices), sigma=10)
        mu_2 = pm.Normal("mu_2", mu=np.mean(prices), sigma=10)
        sigma = pm.HalfNormal("sigma", sigma=10)
        mu = pm.math.switch(tau > np.arange(len(prices)), mu_1, mu_2)
        observation = pm.Normal("obs", mu=mu, sigma=sigma, observed=prices)
        trace = pm.sample(500, tune=500, return_inferencedata=True)
    assert trace.posterior["tau"].shape[1] > 0, "Model sampling failed"
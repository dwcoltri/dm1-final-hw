#!/usr/bin/env python3

from tqdm import tqdm
import fire
import pandas as pd
import statistics


def main(withdrawl_amount, simulations=1000, months=12 * 25, savings=10 ** 6):
    """
    simulations = the number of simulations to run
    months = total months (12 = year x 25 years)
    savings = starting money
    withdrawl_amount = how much money to take out monthly
    """

    # Prepare some variables
    successes = 0
    failures = 0
    balances = []
    data = pd.read_csv("sp500.csv")

    for i in tqdm(range(simulations)):
        # Run a simulation
        balance = simulate(savings, months, withdrawl_amount, data)
        # Tally our simulation results
        if balance >= 0:
            successes += 1
        else:
            failures += 1
        # Append the balance to our list
        balances.append(balance)
    # Print out our results
    print(f"Number of Simulations: {simulations}")
    print(f"Successes (Positive Balance): {successes}")
    print(f"Chance of Success: {successes/simulations}")
    print(f"Failures (Negative Balance): {failures}")
    print(f"Chance of Failure: {failures/simulations}")
    print(f"Average Amount Left (mean): {statistics.mean(balances)}")


def simulate(savings, months, withdrawl_amount, data):
    for i in range(months):
        # Grab a random rate:
        rate = data.sample()["MonthlyGainOrLoss"].values[0]
        # Calculate the changes to our savings based on rate
        savings = savings + (savings * rate)
        savings = savings - withdrawl_amount
    return savings


if __name__ == "__main__":
    fire.Fire(main)

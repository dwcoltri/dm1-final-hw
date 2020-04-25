# Data Mining 1 - Final Homework

## Homework Definition
Option 1 - Simulation

A few weeks back we did a simulation that checked whether we would run out of money if we retired with a million dollars, removed $4000 per month and lived 25 years after retirement.  (I've attached an R file that did the simulation in the video)

Repeat the simulation in either R or Python (no excel please!) with the following additions.
1. Create a wrapper procedure or function that takes the following parameters (# simulations, #months retired, StartingMoney, MonthlyAllowance).  So in the scenario above if we wanted to run 1000 simulations we would pass (1000, 12*25, 10^6, 4000).
2.  The procedure should print out the following:  # of simulations that ran out of money, # of simulations that made money, Average amount left.  (e.g.  if you ran the simulation 3 times and the amounts left were 5000, -1000, 5000, then you would return 3000 for the average.
3.  Run your procedure for the following scenarios (remove 3000 per month, 4000 per month, 5000 per month)
That's all worth 9 points.  If you want the 10th point answer the following:
4.  If I wanted to remove $10,000 per month and wanted to have 95% confidence that I wouldn't run out of money.  How much would I need to save up before retirement?

## Notes:

To run the code first run
```
pip3 install -r requirements.txt
```
Then run
```
./final_hw.py --withdrawl_amount=xxxx
```
where `xxxx` is the amount to withdrawl each month.

* results.txt = output from the required 3 runs
* extra_point.txt = output from the extra point question
  *   (Looks like around 3.5million is the magic savings amount)
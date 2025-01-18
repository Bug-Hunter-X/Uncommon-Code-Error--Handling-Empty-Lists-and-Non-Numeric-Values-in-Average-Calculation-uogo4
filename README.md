# Python Code Error: Average Calculation

This repository demonstrates a common error in Python when calculating the average of a list: handling empty lists and lists containing non-numeric values.  The `bug.py` file shows the initial code with the error. The `bugSolution.py` file provides the solution.

The issue arises because the original function does not have robust error handling.  An empty list will cause a `ZeroDivisionError`, and a list with non-numeric values will cause a `TypeError`. The solution includes checks to gracefully handle both of these scenarios.
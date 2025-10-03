import numpy as np  

# 1. Create a 2D NumPy array representing transaction volumes
transactions = np.array([
    [1000, 1500, 1100, 1300, 1400, 1500], 
    [1000, 3200, 4200, 1050, 1650, 1650],  
    [2000, 2100, 2000, 2050, 2000, 2100], 
    [1800, 1400, 1350, 1500, 1750, 1800]   
])

# 2.Calculate the total transactions per branch.
totalPerBranch = transactions.sum(axis=1)
print("\n Total Transactions Per Branch:\n", totalPerBranch)

# 3. Identify the branch with the highest total transactions
highestBranch = np.argmax(totalPerBranch) + 1
print("\n Highest Total Transactions Per Branch:\n", highestBranch)

# 4.Compute the average monthly transaction volume across all branches
avgmonthly = transactions.mean()
print("\n Average Monthly Transactions for all branches:\n", avgmonthly)

# 5. Reshape the array to a 3x8 format
reshaped = transactions.reshape(3, 8)
print("The reshaped array is: ", reshaped)

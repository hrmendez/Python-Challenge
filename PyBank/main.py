import os
import csv
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company.
# You will give a set of financial data called budget_data.csv
# The dataset is composed of two columns: `Date` and `Profit/Losses`
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

#Creating the Path
csvpath = os.path.join(".", 'Resources', 'budget_data.csv')
# Creating lists to store values
total_months = []
total_profit_losses = []
change_profit_losses = []
# Open budget_data.csv on read mode.
with open(csvpath,newline="", encoding="utf-8") as budget_data:
    # Storing contents of budget_data.csv
   csvreader = csv.reader(budget_data,delimiter=",")
   # Remove header
   header = next(csvreader)
   # Iterate through rows.
   for row in csvreader:
       total_months.append(row[0])
       total_profit_losses.append(int(row[1]))
   # Iterate through the profit_losses list.
   for i in range(len(total_profit_losses)-1):
       # Take the difference between two months and append to monthly profit change
       change_profit_losses.append(total_profit_losses[i+1]-total_profit_losses[i])
# Pulling the Greatest Increase
max_increase_value = max(change_profit_losses)
max_increase_month = change_profit_losses.index(max(change_profit_losses)) + 1
# Pulling the Greatest Decrease
max_decrease_value = min(change_profit_losses)
max_decrease_month = change_profit_losses.index(min(change_profit_losses)) + 1
# Print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: $ {sum(total_profit_losses)}")
print(f"Average Change: {round(sum(change_profit_losses)/len(change_profit_losses),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} $ {(str(max_increase_value))}")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} $ {(str(max_decrease_value))}")

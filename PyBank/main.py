 #import and path

import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

# lists
month = []
profit_loss = []
change_in_rev = []
previous_revenue = 0

# open
with open(bank_csv) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	#remove header
	csv_header = next(csvfile)

	# iterate through rows
	for row in csvreader:
		# add to columns (month)
		month.append(row[0])
		# profit_loss - had to change int and float to address string value (-)
		profit_loss.append(int(float(row[1])))
		# keep track of change
		revenue = int(float(row[1]))
		change = revenue - previous_revenue
		change_in_rev.append(change)
		previous_revenue = revenue

	
	# Total months
	num_months = len(profit_loss)
	# total_profit
	total_profit = sum(profit_loss)
	# revenue change (remove original value, and reduce monthly change by 1)
	revenue_change = (sum(change_in_rev)-int(change_in_rev[0])) / (len(change_in_rev)-1)
	# greatest increase - define max profit, find the row index, apply to month list
	greatest_increase = max(change_in_rev)
	greatest_inc_index = change_in_rev.index(greatest_increase)
	greatest_inc_date = month[greatest_inc_index]
	# greatest decrease - define min profit, find row index, apply to month list
	greatest_decrease = min(change_in_rev)
	greatest_dec_index = change_in_rev.index(greatest_decrease)
	greatest_dec_date = month[greatest_dec_index]

# printing output
print(f"Financial Analysis")
print(f"---------------------------------------------")
print(f"Total Months: {str(num_months)}")
print(f"Total: ${str(total_profit)}")
print(f"Average Change: ${str(round(revenue_change))}")
print(f"Greatest Increase In Profits: {greatest_inc_date} (${str(greatest_increase)})")
print(f"Greatest Decrease In Profits: {greatest_dec_date} (${str(greatest_decrease)})")

# create a text file of above
with open(os.path.join("Analysis", "FinAnalysis.txt"), "w") as f:
	f.write(f"Financial Analysis\n")
	f.write(f"-------------------------------------------\n")
	f.write(f"Total Months: {str(num_months)}\n")
	f.write(f"Total: ${str(total_profit)}\n")
	f.write(f"Average Change: ${str(round(revenue_change))}\n")
	f.write(f"Greatest Increase In Profits: {greatest_inc_date} (${str(greatest_increase)})\n")
	f.write(f"Greatest Decrease In Profits: {greatest_dec_date} (${str(greatest_decrease)})\n")


	




	

	






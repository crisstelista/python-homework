import csv
from pathlib import Path

input_file = Path("budget_data.csv")
output_file = "output.txt"
number_of_months = []
overall_profit = []
revenue_change = []

with open(input_file, 'r') as budget:
    csvreader = csv.reader(budget, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        number_of_months.append(row[0])
        overall_profit.append(int(row[1]))
    for value in range(1, len(overall_profit)):
        revenue_change.append(overall_profit[value] - overall_profit[value-1])

max_increase_amount = max(revenue_change)
max_decrease_amount = min(revenue_change)
max_increase_month = revenue_change.index(max(revenue_change)) + 1
max_decrease_month = revenue_change.index(min(revenue_change)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(number_of_months)}")
print(f"Total: ${sum(overall_profit)}")
print(f"Average Change: ${round(sum(revenue_change) / len(revenue_change), 2)}")
print(f"Greatest Increase in Profits: {number_of_months[max_increase_month]} (${(str(max_increase_amount))})")
print(f"Greatest Decrease in Profits: {number_of_months[max_decrease_month]} (${(str(max_decrease_amount))})")


with open(output_file, "w") as file:
    file.write("Financial Analysis \n")
    file.write("---------------------------- \n")
    file.write(f"Total Months: {len(number_of_months)} \n")
    file.write(f"Total: ${sum(overall_profit)} \n")
    file.write(f"Average Change: ${round(sum(revenue_change) / len(revenue_change), 2)} \n")
    file.write(f"Greatest Increase in Profits: {number_of_months[max_increase_month]} (${(str(max_increase_amount))}) \n")
    file.write(f"Greatest Decrease in Profits: {number_of_months[max_decrease_month]} (${(str(max_decrease_amount))}) \n")
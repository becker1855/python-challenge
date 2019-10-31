import os
import csv
py_bank = os.path.join("budget_data.csv")
with open(py_bank, newline='') as csvfile:
    budgetsheet = csv.reader(csvfile,delimiter=',')
    budgetheader = next(budgetsheet)
    totalmonths = 0
    budgettotal = 0
    firstmonth = 0
    maxnumber = 0 
    maxmonth = 0 
    minnumber = 0
    minmonth = 0
    for row in budgetsheet:
        totalmonths += 1
        budgettotal += int(row[1])
        lastmonth = (row[1])
        if firstmonth == 0:
                firstmonth = (row[1])
        if int(row[1]) > maxnumber:
                maxnumber = int(row[1])
                maxmonth = str(row[0])
        if int(row[1]) < minnumber:
                minnumber = int(row[1])
                minmonth = str(row[0])
        yearchange = (int(lastmonth) - int(firstmonth))/85
print ("Financial Analysis")
print ("----------------------------")
print(f"total months: {totalmonths}")
print(f"total:{budgettotal}")
print(f"Average Change: ${format(yearchange,'.2f')}")
print(f"Greatest Increase in Profits: {maxmonth} ${maxnumber}")
print(f"Greatest Decrease in Profits: {minmonth} ${minnumber}")

output_path = os.path.join("pybankdone.csv")
with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Financial Analysis'])
        csvwriter.writerow(["----------------------------"])
        csvwriter.writerow([f"total months: {totalmonths}"])
        csvwriter.writerow([f"total:{budgettotal}"])
        csvwriter.writerow([f"Average Change: ${format(yearchange,'.2f')}"])
        csvwriter.writerow([f"Greatest Increase in Profits: {maxmonth} ${maxnumber}"])
        csvwriter.writerow([f"Greatest Decrease in Profits: {minmonth} ${minnumber}"])
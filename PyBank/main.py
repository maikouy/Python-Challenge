#Import file/ open the file to CHANGE 
import os
import csv

#path to collect data from the Resource folder
budget_data = os.path.join("Resources", "budget_data.csv")

# The list used to store 

months = []
profits = [] 
total_profits = []
prof_loss = []
net_total = 0
total_months = 0


#Open CSV by importing it via module
#csvreader- used a csv module to make a reader. This reader is going to read from the csv file. Csvfile is the nickname I give the file once open.
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
#Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csvreader}")

    #begin to loop        
    for row in csvreader:
        
        months.append(row[0])
        profits.append(int(row[1]))
   
        #print(len(months))
        #print(profits)
    
        #Calculate net total:
        prof_loss = int(row[1])
        net_total = net_total + prof_loss
        #print(net_total)
        
    profits_change = []   

    for i in range(len(profits)-1):
        profits_change.append(profits[i+1] - profits[i])
        #print(profits_change)
                                
    #calculate average revenue change
    profits_average = sum(profits_change) / len(profits_change)
    print(profits_average)

    #find greatest increase in profits
    greatest_increase = max(profits_change)
    print(greatest_increase)   
    x = profits_change.index(greatest_increase)
    print(x)
    greatest_month = months[x]
    greatest_month_and_one = months[x + 1]
    #you have to add 'one' since the number 24 includes the headers, so x is the row above the greatest increase.
    print(greatest_month_and_one)

    #find the greatest decrease in losse
    greatest_decrease = min(profits_change)
    print(greatest_decrease)
    t = profits_change.index(greatest_decrease)
    print(t)
    decrease_month = months[t]
    decrease_month_and_one = months[t + 1]
    #you have to add 'one' since the number 24 includes the header, so t is the row above the greatest decrease.
    print(decrease_month_and_one)


#Analysis

print(f"Financial Analysis")
print(f"----------------------------------------------")
print(f"Total Months:"  +  str(len(months))) 
print(f"Total: $" + str(net_total))
print(f"Average: $" + str(profits_average))
print(f"Greatest Increase in Profits:" + str(greatest_month_and_one) + "(" + "$" + str(greatest_increase) + ")")
print(f"Greatest Decrease in Profits:" + str(decrease_month_and_one) + "(" + "$" + str(greatest_decrease) + ")") 

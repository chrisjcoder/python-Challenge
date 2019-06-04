#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
#You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
#(Thankfully, your company has rather lax standards for accounting so the records are simple.)
#
#Your task is to create a Python script that analyzes the records to calculate each of the following

import os
import csv


from decimal import Decimal, ROUND_05UP, ROUND_HALF_UP


budget_csv = os.path.join("Resources", "budget_data.csv")
#
tot=0
net=[]#**
dev=[]#**

with open(budget_csv,newline="") as csvBudget:
    csvreader=csv.reader(csvBudget,delimiter=",")
    next(csvreader, None)  # skip the headers
    min_max = list(csvreader)#**creating a list from csvreader 
    min_max.sort#** trying to sort list by date( not sure if this actually works)
    
    for row in min_max:
        tot=tot+1 #**The total number of months included in the dataset
        net.append(int(row[1]))#** in this list I gather all values in the profit/loss column

    for i in range(1,len(net)):
        dev.append(net[i]-net[i-1])#** add to list all profit/loss changes by each day
        
#    print(sum(dev)/tot)
#    x=(sum(dev))/tot
# use this to convert average change to a currency format with 2 decimals  
    cents = Decimal('0.01')
    avgChg=Decimal(sum(dev)/(tot-1)).quantize(cents, ROUND_HALF_UP)
    

    
   # print(round(decimal(sum(dev))/(tot),2))#**average change of profit/loss
#    print(int(tot))#total number of months
#    print(sum(net))# sum of profit/loss 
#    
#
    # now it's in memory, so we can reuse it
    #get entire row of min and max values profit/loss and the date
    profit= max(min_max, key=lambda row: int(row[1]))
    loss= min(min_max, key=lambda row: int(row[1]))
#    print(profit[0])
#    print(profit[1])
#    print(loss[0])
#    print(loss[1])
    
#- Replicate the to terminal and file

    print("Financial Analysis")
    print(".......................................")
    print("Total Months: "+ str(tot))
    print("Total: $"+ str(sum(net)))
    print("Average Change: $" + str(avgChg))
    print("Greatest Increase in Profits: "+ profit[0] +" " +"($"+ profit[1]+")")
    print("Greatest Decrease in Profits: "+ loss[0] +" " +"($"+ loss[1]+")")

 # wrting a function to write contents to file
def main():
    f=open("FinancialAnalysis.txt","w+")
    f.write("Financial Analysis"+ "\r\n")
    f.write("......................................."+ "\r\n")
    f.write("Total Months: "+ str(tot)+ "\r\n")
    f.write("Total: $"+ str(sum(net))+ "\r\n")
    f.write("Average Change: $" + str(avgChg)+ "\r\n")
    f.write("Greatest Increase in Profits: "+ profit[0] +" " +"($"+ profit[1]+")"+ "\r\n")
    f.write("Greatest Decrease in Profits: "+ loss[0] +" " +"($"+ loss[1]+")")
    f.close
    
if __name__ == "__main__":
    main()



# Here are all your options for rounding:
# This one offers the most out of the box control
# ROUND_05UP       ROUND_DOWN       ROUND_HALF_DOWN  ROUND_HALF_UP
# ROUND_CEILING    ROUND_FLOOR      ROUND_HALF_EVEN  ROUND_UP

#our_value = decimal.("-2288.1976744186045")
#output = Decimal(our_value.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
#
#print(output)




#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#    
#    # Specify the file to write to
#output_path =open("FinancialAnalysis.txt","w+")
# #os.path.join("..", "output", "FinacialAnalysis.txt")
#
## Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w') as results:
#
#    # Initialize csv.writer
#    csvwriter = csv.writer(results)
#
#    # Write the first row (column headers)
#    csvwriter.writerow("hello" + profit[0])
#
#    # Write the second row
#    csvwriter.writerow("goodbye" + loss[0])
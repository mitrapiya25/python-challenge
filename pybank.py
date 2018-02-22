import csv
import os
import sys
import getopt
import re

print ("Number of arguments: "+ str(len(sys.argv)) +" arguments.")
print ("Argument List: " + str(sys.argv))
print (" remainders : " + str(sys.argv[1]))
NumOfFiles = int(sys.argv[1])
months_revenue=[]
for i in range(1,(NumOfFiles+1)):
    inputfile = "budget_data_" + str(i) +".csv"
    print("Input " + inputfile)
    input_path = os.path.join("Homework",inputfile)
    with open(input_path,newline='',encoding="utf8") as csvinpfile:
       csvreader = csv.reader(csvinpfile,delimiter=',')
       for revenueinp in csvreader:
           months_revenue.append(revenueinp)

totalMonths = 0
totalRev = 0
monthlyRevChange = 0
PrevMonthRev =0
GreatestIncrease = 0
GreatestDecrease =0
dt ="Date"
for row in months_revenue:
  if row[0] == dt:
     continue
  else:
    monthlyRevChange =  int(row[1])- PrevMonthRev
    totalMonths = totalMonths+1
    totalRev = totalRev + int(row[1])
    PrevMonthRev = int(row[1])
    if monthlyRevChange > 0 and monthlyRevChange > GreatestIncrease:
       GreatestIncrease = monthlyRevChange
       GreatestIncreaseMonth = row[0]
    elif monthlyRevChange < 0 and monthlyRevChange < GreatestDecrease:
       GreatestDecrease = monthlyRevChange
       GreatestDecreaseMonth = row[0]

print("Total Month included in the dataset is " + str(totalMonths)) 
print("Total revenue generated over the period is " + str(totalRev))  
print(" Greatest Increase in Revenue  :" +  GreatestIncreaseMonth + "(" +  str(GreatestIncrease ) + ")")
print(" Greatest Decrease in Revenue  :" +  GreatestDecreaseMonth + "(" +  str(GreatestDecrease ) + ")") 

output_path = os.path.join("Homework","Finalresult.txt")
textfile = open(output_path, 'w') 
textfile.write("Total Month included in the dataset is " + str(totalMonths) + "\n") 
textfile.write("Total revenue generated over the period is " + str(totalRev) + "\n")  
textfile.write(" Greatest Increase in Revenue  :" +  GreatestIncreaseMonth + "(" +  str(GreatestIncrease ) + ")"  + "\n")
textfile.write(" Greatest Decrease in Revenue  :" +  GreatestDecreaseMonth + "(" +  str(GreatestDecrease ) + ")"  + "\n") 
textfile.close()   

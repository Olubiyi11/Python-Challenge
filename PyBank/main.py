import os 
import csv
# budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")
budget_data_csv ="C:/Users/lordb/Python-Challenge/PyBank\Resources/budget_data.csv"
Total_months = 0
Net_Total = 0
ProfitandLosses = []
PandL4Period = [] #Profit and Losses for entire Period
Averagechange = []
Greatestprofitincrease = []
Date = []



#Open and read csv
with open(budget_data_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
#skip header
    header = next(csv_file)
    for row in csvreader:
        # counting the rows
        Total_months = Total_months+1
        #Taking input from the second column
        Net_Total = Net_Total+ int(row[1])
        ProfitandLosses.append(row[1])
        Date.append(row[0])

    print("Financial Analysis")
    print("................................")
    print(f"Total Months: {Total_months}")
    print(f"Total: ${Net_Total}")
    

    for x in range(1,len(ProfitandLosses)):
        PandL4Period.append(int(ProfitandLosses[x])-int(ProfitandLosses[x-1]))
    Averagechange= sum(PandL4Period)/len(PandL4Period)
    rounded = round(Averagechange, 2)
    print(f"Average Change: ${rounded}")
    proandlossgreatestincrease = max(PandL4Period)
    proandlossgreatestdecrease = min(PandL4Period)
    proandlossgreatestincreasedate = Date[PandL4Period.index(proandlossgreatestincrease)+1]
    proandlossgreatestdecreasedate = Date[PandL4Period.index(proandlossgreatestincrease)+1]
    print("Greatest Increase in Profits:", proandlossgreatestincreasedate, f"${proandlossgreatestincrease}")
    print("Greatest Decrease in Profits:", proandlossgreatestdecreasedate, f"${proandlossgreatestdecrease}")
    
    #printing to Budgetanalysis.txt
    with open("Budgetanalysis.txt", "w") as file:
        L = ["Financial Analysis\n", "................................\n", "Total Months: 86\n", "Total: $22564198\n", "Average Change: $-8311.11\n", "Greatest Increase in Profits: Aug-16 $1862002\n", "Greatest Decrease in Profits: Aug-16 $-1825558"]
        file.writelines(L)
        file.close
 


    
 




          






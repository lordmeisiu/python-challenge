import os
import csv

#csvfile = os.path.join(".","Resources","budget_data.csv") #get csv file path
#csvfile = "C:\\Users\\mcael\\gw\\homework\\03-Python\\python-challenge\\PyBank\\Resources\\budget_data.csv"
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
path = os.path.dirname(os.path.abspath(__file__))
csvfile = path + "\\Resources\\budget_data.csv"
csvfile_1 = path + "\\analysis\\analysis.txt"

#csvfile_1 = os.path.join("","analysis","analysis.txt") # path for text file
#csvfile_1 = "C:\\Users\\mcael\\gw\\homework\\03-Python\\python-challenge\\PyBank\\analysis\\analysis.txt"
with open(csvfile_1,'w') as analysis_output:
    with open(csvfile, encoding = 'utf') as budget_csv: #assign variable to csv file
        csvreader = csv.reader(budget_csv, delimiter=",") #read in budget_data and seperate using commas
        print(csvreader)  

        header = next(csvreader) #header takes first row so need data to start on next row
        totalmonthcount = 0 
        budget_1 = [] 
        totalbudget = 0
        month_1 = [] 

        for row in csvreader:
            totalmonthcount+=1
            budget_1.append(row[1])
            month_1.append(row[0])

        for x in budget_1:
            totalbudget+= float(x) #Total data SUM   
        bt = round(totalbudget,) #stores total budget amount that goes to txt file
        profitchange = round((float(budget_1[len(budget_1) -1]) - float(budget_1[0]))/float(len(budget_1)-1),2)

        first_num = 0
        second_num = 0
        profits_rev = []
        for i in budget_1:
            second_num = second_num + 1 
            if(second_num < len(budget_1)):
                first_1 = budget_1[first_num]
                second_1 = budget_1[second_num]
                profits_sub = float(second_1)-float(first_1)
                profits_rev.append(profits_sub)
                first_num = first_num + 1
            else:
                0
            
            max_num = round(max(profits_rev),)
            min_num = round(min(profits_rev),)
            month_min = profits_rev.index(min_num) + 1
            month_max = profits_rev.index(max_num) + 1
            m1 = month_1[month_max]
            m2 = month_1[month_min]

    print('analysis')
    print('------------------------------')
    print(f'total months: {totalmonthcount}')
    print(f'total: ${round((totalbudget),)}')
    print(f'average change: ${profitchange}')
    print(f'greatest increase in profits: {m1} (${max_num})')
    print(f'greatest decrease in profits: {m2} (${min_num})')
        
    out_1 = f'analysis\n------------------------------\ntotal months: {totalmonthcount}'
    out_2 = f'\ntotal: ${totalbudget}\naverage change: ${profitchange}'
    out_3 = f'\ngreatest increase in profits: {m1} (${max_num})\ngreatest decrease in profits: {m2} (${min_num})'
    analysis_output.write(out_1)
    analysis_output.write(out_2)
    analysis_output.write(out_3)
analysis_output.close()
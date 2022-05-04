"""
KMITL - 1416521 Introduction to Algorithm Final Project

This Python program sort:
"Date with Time" using "Insertion sort"
"Subject name" and "Student name" using "Quick sort"
"Subject code" using "Bubble sort"
and "Search & Delete duplicates" using "Linear search"
of the exam table.

Code with ❤︎ by Piyawud Koonmanee, Intouch Wangtrakoondee, Thanin Katanyutapant
"""

import pandas as pd
from tabulate import tabulate       # To pretty print dataframe 

####### Initial data #######
data = {'subjectCode': [1416301, 1416521, 9106507, 1416304, 1006505, 1416301],
          'subjectName': ['Differential Equations','Intro to Algorithms','Sensor Technology','Feedback Control','Thinking Critically','Differential Equations'],
          'dates': ['02 Dec 2021','09 Dec 2021','29 Nov 2021','29 Nov 2021','02 Dec 2021','02 Dec 2021'],
          'startTime': ['9:45','9:30','13:30','9:30','9:30','9:45'],
          'endTime': ['12:45','12:30','16:30','12:30','12:30','12:45'],
          'studentName': ['Intouch','Non','First','Mhing','Tong','Intouch'],
          'lecturer': ['Dr. Wipoo','Dr. Anakkapon','Dr. Teerayut','Dr. Pitikate','Dr. Bruce','Dr. Wipoo'],
          'examRoom': ['HM406','HM302','HM504','Online Exam','Online Exam','HM406']
        }

df = pd.DataFrame(data)
############################

### -- Customize data -- ###
# Insert
df.loc[6] = [5724679, 'Valorant', '22 Apr 2021','15:30','18:30','Intouch','Dr. Thanin','Online Exam']
df.loc[7] = [3678912, 'Teamfight Tactics', '01 Jan 2021','8:00','18:00','Tong','Dr. Lapin','Online Exam']
df.loc[8] = [4002154, 'How to Get A in Algorithm', '18 Nov 2021','12:00','16:00','Micro','Dr. Anakkapon','Online Exam']
df.loc[9] = [7542585, 'Advanced English', '26 Oct 2021','14:00','16:00','Micro','Dr. Wangtrakoondee','HMR6S']
df.loc[10] = [4002154, 'How to Get A in Algorithm', '18 Nov 2021','12:00','16:00','Micro','Dr. Anakkapon','Online Exam']
df.loc[11] = [4152150, 'Algorithm is Fun', '23 Nov 2021','10:00','12:00','Yuu','Dr. Anakkapon','Online Exam']
df.loc[12] = [4002153, 'Food is love', '23 Nov 2021','10:00','12:00','Yuu','Dr. Kimchi','Online Exam']

# Edit 
df.loc[6,'studentName'] = 'Mhing'

# Delete
df.drop(11, inplace = True) # drop row

### -- End of Customize data -- ###

df.reset_index(drop = True, inplace = True) # reset index - required for the algorithm to work


### -- Remove duplicate using linear search -- ###
def delDupe(df):
    to_remove = []

    # search for duplicate row #
    for i in range(df.shape[0]): # Iterate through all rows
        for j in range(i+1,df.shape[0]): # same thing except row at index i
            if (df.loc[i] == df.loc[j]).all(): # Check if all elements in rows i and row j are equal
                to_remove.append(j) # Store what to remove in a list
                break

    # remove duplicate row #
    for i in to_remove: # Iterate through the list and remove the value
        df.drop(i, inplace = True)
    df.reset_index(drop = True, inplace = True) # reset index - required for other algorithm to work


### -- Quick Sort student name and subject name -- ###
# Convert character to ASCII
def quanName(text):
    # Initialize the 2 arrays
    fullnum = []
    # Create the ascii array used to store name as number
    count = 0
    for i in text: # This will need to be changed to accomodate data frame
        ascii = []
        for j in text[count]:
            ascii.append(ord(j))
        if ascii[0] >= 65 and ascii[0] <= 90: # Condition for capital letters
            ascii[0] += 32
        # Convert ascii to a comparable values
        multi = 1
        for k in ascii:
            ascii[multi - 1] = k / (5 ** multi) # This is the control number, too high and it can't sort long names, to low and it can't accurately  sort
            multi += 1
        # Store sum of ascii to fullnum
        sum = 0
        for l in ascii:
            sum += l
        fullnum.append(sum)
        # Incease count
        count += 1
    return fullnum

# Create partition for Quick sort algorithm
def partition(text, arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            b, c = df.iloc[i].copy(), df.iloc[j].copy() # Swap row of dataframe
            df.iloc[i], df.iloc[j] = c, b # Swap row of dataframe

    arr[i + 1], arr[high] =  arr[high], arr[i + 1]

    b, c = df.iloc[i+1].copy(), df.iloc[high].copy() # Swap row of dataframe
    df.iloc[i+1], df.iloc[high] = c, b # Swap row of dataframe
    return (i + 1)

# Main Quick sort function
def quickSort(text, arr, low, high):
    if len(arr) == 1:
        return text
    if low < high:
        pi = partition(text, arr, low, high)

        quickSort(text, arr, low, pi - 1)
        quickSort(text, arr, pi + 1, high)

# Main alphabet sort function
def sortLetter(name):
    qName = quanName(name)
    low = 0
    high = len(qName) - 1
    quickSort(name, qName, low, high)

### -- Insetion sort date with time -- ###
# Convert date into current day in a year (0-365)
def sortDate(df):

    month_list = [("Jan",31),("Feb",28),("Mar",31),("Apr",30),("May",31),("Jun",30),
                  ("Jul",31),("Aug",31),("Sep",30),("Oct",31),("Nov",30),("Dec",31)]

    # Split the date into a list #
    for i in range(df.shape[0]): # Iterate through all rows
        split_dates = []
        tmp = ''
        passed_days_month = 0

        # Split date on space #
        for char in df.loc[i,'dates']:
            if char == ' ':
                split_dates.append(tmp)
                tmp = ''
            else:
                tmp += char
        if tmp:
            split_dates.append(tmp)
        
        ## Convert date to int ##
        for j in range(len(month_list)): # Iterate through 12 months list
            split_dates[0], split_dates[2] = int(split_dates[0]), int(split_dates[2]) # Convert day and year
            if split_dates[1] == month_list[j][0]: # Convert month
                split_dates[1] = j+1
                
                ## Count day passed ##
                for k in range(split_dates[1]): # Iterate from January till month j+1
                    passed_days_month += month_list[k][1] # Total days from January till the end of that month
                total_days = passed_days_month - ((month_list[j][1]) - split_dates[0]) # Subtract to find current day

        df.loc[i,'tmpDays'] = total_days # Store it in respective row in temporary column

    ## Insertion sort of date ##
    # Split the time into a list #
    for i in range(1,(df.shape[0])):
        next_val = df.loc[i,'tmpDays']
        j = i-1 # current row
        while j >= 0 and next_val < df.loc[j,'tmpDays']: # Check if current value is greather than next value
            b, c = df.iloc[j+1].copy(), df.iloc[j].copy() # Swap row
            df.iloc[j+1], df.iloc[j] = c, b # Swap row
            j = j-1

    ## Time sort while keeping date sort ##
    for i in range(df.shape[0]): # Iterate through all rows
        split_time = []
        tmp = ''

        ## Split time on colon ##
        for char in df.loc[i,'startTime']:
            if char == ':':
                split_time.append(tmp)
                tmp = ''
            else:
                tmp += char

        # Convert time to int #
        if tmp:
            split_time.append(tmp)
        split_time = int("".join(split_time)) # Join the list
        df.loc[i,'tmpTime'] = split_time # Store it in respective row in temporary column

    ## Insertion sort of time ##
    for i in range(1,(df.shape[0])):
        next_val = df.loc[i,'tmpTime']
        j = i-1 # current row
        while j >= 0 and next_val < df.loc[j,'tmpTime']: # Check if current value is greather than next value
            if df.loc[j,'tmpDays'] == df.loc[i,'tmpDays']: # Check if it is on the same date, otherwise then no need to sort
                b, c = df.iloc[j+1].copy(), df.iloc[j].copy() # Swap
                df.iloc[j+1], df.iloc[j] = c, b # Swap
            j = j-1

    df.drop(['tmpDays','tmpTime'],axis = 1,inplace = True) # drop temporary column


### -- Bubble sort on subject code -- ###
def sortCode(df):
    for i in range(df.shape[0],-1,-1): # Iterate through all rows
        for m in range(1,i,1):
            if df.loc[m-1,'subjectCode'] > df.loc[m,'subjectCode']: # Check if previous value is greater than current value
                b, c = df.iloc[m-1].copy(), df.iloc[m].copy() # Swap
                df.iloc[m-1], df.iloc[m] = c, b # Swap

################## Calling Function ##################
print("Original Dataframe:")
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False)) # Print table

print("\nAfter deleting Duplicates:")
delDupe(df)
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False)) # Print table

print("\nAfter sorting by Subject Code:")
sortCode(df)
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False)) # Print table

print("\nAfter sorting by Date:")
sortDate(df)
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False)) # Print table

print("\nAfter sorting by Student Name:")
sortLetter(df.loc[:,'studentName'])
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False)) # Print table

print("\nAfter sorting by Subject Name:")
sortLetter(df.loc[:,'subjectName'])
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False)) # Print table
######################################################
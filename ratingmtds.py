### Created on Mon Apr 11 18:53:10 2022

# @author: Ofe Segun

# importing necessary libraries
```
import pandas as pd  
import numpy as np
import random as rd
```
# First Method

df = pd.read_excel('Exce.xlsx', sheet_name="Sheet1") # importing the excel sheet
bab = df.values.tolist() # Put the data in a list
#print(bab)
# Next, we summed over the rating for each columns by taking each list 
# and the corresponing column values and put the sum in to a list 
torank=[sum([bab[j][i] for j in range(len(bab))]) for i in range(len(bab[0]))] # list of ratings corresponding to the research area
#print(torank) 
names=df.columns # This is the names of each columns (Research Areas)
chart =[[n] for n in names] # To create list with list for each research area in other to take in their rankings for each ranking method 
indy=list(range(len(names)))# index of the names
rankindex = [na for _, na in sorted(zip(torank, indy))] # This is bring the ranks in neg and the index of the names together 
chart=[chart[j]+[rankindex[j]+1] for j in range(len(chart))] # This line is to update the rankings in the chart table
order = [names[j] for j in rankindex] 
 


# Next we do the Ranked Pair Method


B=[] # This is to make a matrix with the ranking. 
for i in range(len(bab[0])): 
    row = []
    for j in range(len(bab[0])):
        bb =len([b for b in bab[0:] if b[i]<b[j]]) # this line is to compute the number of times each research ranking won the others 
        gg=bb-len([b for b in bab[0:] if b[j]<b[i]]) # this line correspond to the number of times each research ranking lose to the others
        row +=[gg]
    B+=[row] # The list correspond to the a list with the ranking for each research area over the other research area for example, for the second entry in the first list, AT beats DG 12 times. The second represent DG. The first element -12 tells us that DG lose to AT 12 times
#print(B)
posi =[] # This line is to count the number of positive ranking in the list corresponding to each research
names = df.columns # To Pull out the names of the research from the list bab
indy=list(range(len(names)))
# The next lines of code is to put the ranks with the names of the research area
for l in B:# Pull out each list from B
    count=0
    for k in l: # Pull out each elements in the list
        if k>0: # Check if element is positive
            count+=1 # count increases by 1
    posi+=[count] # Add count to posi
neg = [-g for g in posi]
rankindex = [na for _, na in sorted(zip(neg, indy))] # This is bring the ranks in neg and the index of the names together 
chart=[chart[j]+[rankindex[j]+1] for j in range(len(chart))] # This line is to update the rankings in the chart table
order = [names[j] for j in rankindex]
  


# Next we renormalized the columns with mean 0 and std 1 and used ranked pair for the ranking


import sklearn # We import modules that help with standard scaling (mean 0 and standard deviation 1)
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
df = pd.read_excel('Exce.xlsx', sheet_name="Sheet1") # Read in excel sheet from it source
std_scaler = StandardScaler() # to scale the data to mean 0 and std 1
# fit and transform the data
df1 = pd.DataFrame(std_scaler.fit_transform(df), columns=df.columns )# sclaing putting the data in a dataframe
#print("The standard deviation of the column Algebraic Topology is:" ,df1['Algebraic Topology'].std()) # The next two lines is to confirm that the 
# transformed data has mean zero and standard deviation 1 columnwise
#print("The mean of the column Algebraic Topology is:" ,df1['Algebraic Topology'].mean())


bab = df1.values.tolist() # Put the dataframe into a list
B=[] # This is to make a matrix with the ranking. 
for i in range(len(bab[0])): 
    row = []
    for j in range(len(bab[0])):
        bb =len([b for b in bab[0:] if b[i]<b[j]]) # this line is to compute the number of times each research ranking won the others 
        gg=bb-len([b for b in bab[0:] if b[j]<b[i]]) # this line correspond to the number of times each research ranking lose to the others
        row +=[gg]
    B+=[row] # The list correspond to the a list with the ranking for each research area over the other research area
#print(B)
posi =[] # This line is to count the number of positive ranking in the list corresponding to each research
names = df.columns # To Pull out the names of the research areas from the dataframe df
indy=list(range(len(names)))
# The next lines of code is to put the ranks with the names of the research area
for l in B:# Pull out each list from B
    count=0
    for k in l: # Pull out each elements in the list
        if k>0: # Check if element is positive
            count+=1 # count increases by 1
    posi+=[count] # Add count to posi
neg = [-g for g in posi]
rankindex = [na for _, na in sorted(zip(neg, indy))] # This is bring the ranks in neg and the index of the names together 
chart=[chart[j]+[rankindex[j]+1] for j in range(len(chart))] # This line is to update the rankings in the chart table
order = [names[j] for j in rankindex] 
#print("The rank for the winners is from first to last is: ", order)




# We renormalized the rows with mean 0 and std 1 and used ranked pair for the ranking


transposed_df = df.T # We transposed the data df
std_scaler = StandardScaler()
# fit and transform the data
transposed_df_std = pd.DataFrame(std_scaler.fit_transform(transposed_df), columns=transposed_df.columns)
#print(df_std.head(5))

#print(transposed_df_std[0].std()) # The next two lines is to confirm that the 
# transformed data has mean zero and standard deviation 1 rowwise
#print(transposed_df_std[0].mean())
dfT= transposed_df_std.T
df2 = pd.DataFrame(std_scaler.fit_transform(dfT), columns=df.columns) # sclaing putting the data in a dataframe

bab = df2.values.tolist()
B=[] # This is to make a matrix with the ranking. 
for i in range(len(bab[0])): 
    row = []
    for j in range(len(bab[0])):
        bb =len([b for b in bab[0:] if b[i]<b[j]]) # this line is to compute the number of times each research ranking won the others 
        gg=bb-len([b for b in bab[0:] if b[j]<b[i]]) # this line correspond to the number of times each research ranking lose to the others
        row +=[gg]
    B+=[row] # The list correspond to the a list with the ranking for each research area over the other research area
#print(B)
posi =[] # This line is to count the number of positive ranking in the list corresponding to each research
names = df.columns # To Pull out the names of the research areas from the dataframe df
indy=list(range(len(names)))
# The next lines of code is to 
for l in B:# Pull out each list from B
    count=0
    for k in l: # Pull out each elements in the list
        if k>0: # Check if element is positive
            count+=1 # count increases by 1
    posi+=[count] # Add count to posi
neg = [-g for g in posi]
rankindex = [na for _, na in sorted(zip(neg, indy))] # This is bring the ranks in neg and the index of the names together 
chart=[chart[j]+[rankindex[j]+1] for j in range(len(chart))] # This line is to update the rankings in the chart table
order = [names[j] for j in rankindex] 
#print("The rank for the winners is from first to last is: ", order) 



# We renormalized the rows with mean 0 and std 1 and used the first method for the ranking


bab = df2.values.tolist() # Put the data in a list
# Next, we summed over the rating for each columns and put it in to a list in 
torank=[sum([bab[j][i] for j in range(len(bab))]) for i in range(len(bab[0]))] # list of ratings corresponding to the research area
#print(torank) 
names=df.columns
indy=list(range(len(names)))
rankindex = [na for _, na in sorted(zip(torank, indy))] # This is bring the ranks in neg and the index of the names together 
chart=[chart[j]+[rankindex[j]+1] for j in range(len(chart))] # This line is to update the rankings in the chart table
order = [names[j] for j in rankindex] 
#print("The rank for the winners is from first to last is: ", order)


        
        
# We renormalized the columns with mean 0 and std 1, removed outliers and ranked pair for the ranking

df1 = pd.DataFrame(std_scaler.fit_transform(df), columns=df.columns )# sclaing putting the data in a dataframe
#print("The standard deviation of the column Algebraic Topology is:" ,df1['Algebraic Topology'].std()) # The next two lines is to confirm that the 
# transformed data has mean zero and standard deviation 1 columnwise
#print("The mean of the column Algebraic Topology is:" ,df1['Algebraic Topology'].mean())


# Next we remove outliers from the data
bab = df1.values.tolist() # to put the data into a list

for i in range(len(bab)): # to pick each list in the list 
    for j in range(len(bab[0])): # to pick each element corresponding to a research in each column
        if bab[i][j]>3: # 3 is the standard number for outliers in data
            bab[i][j]= "" # to fill in and empty "" if the number is greater than 3 
#print("It is ",bab) # This is just to see the outcome of the for loop

 

B=[] # This is to make a matrix with the ranking. 
for i in range(len(bab[0])): 
    row = []
    for j in range(len(bab[0])):
        bb =len([b for b in bab[0:] if type(b[i])==float and type(b[j])==float and b[i]<b[j]]) # this line is to compute the number of times each research ranking won the others 
        gg=bb-len([b for b in bab[0:] if type(b[i])==float and type(b[j])==float and b[j]<b[i]]) # this line correspond to the number of times each research ranking lose to the others
        row +=[gg]
    B+=[row] # The list correspond to the a list with the ranking for each research area over the other research area
#print(B)
posi =[] # This line is to count the number of positive ranking in the list corresponding to each research
names = df.columns # To Pull out the names of the research areas from the dataframe df
indy=list(range(len(names)))
# The next lines of code is to 
for l in B:# Pull out each list from B
    count=0
    for k in l: # Pull out each elements in the list
        if k>0: # Check if element is positive
            count+=1 # count increases by 1
    posi+=[count] # Add count to posi
neg = [-g for g in posi]
rankindex = [na for _, na in sorted(zip(neg, indy))] # This is bring the ranks in neg and the index of the names together 
chart=[chart[j]+[rankindex[j]+1] for j in range(len(chart))] # This line is to update the rankings in the chart table
order = [names[j] for j in rankindex] 
#print("The rank for the winners is from first to last is: ", order)


# Next we make a chart with all the six ranking method and the ranks for each fields. 
colnam=['Fields','FM', 'RP', 'RCRP', 'RRRP', 'RRFM', 'RCORP'] # this is a list of the names of columns with different ranking methods 

dfg = pd.DataFrame(chart, columns=colnam ) # To make a dataframe showing the ranking of all six methods
#print("1-Highest Rated Field,..., 7-Lowest Rated Field")
#print(dfg)

#print("Full name of the different methods of ranking used in the above table ")

#print("FM-First Method ")
#print("RP-Ranked Paired")
#print("RCRP-Renormalized Columns and Ranked Paired")
#print("RRRP-Renormalized Rows and Ranked Paired")
#print("RRFM-Ranked Rows and First Method")
#print("RCORP-Renormalized Column, Outliers removed and Ranked Paired")
#print("From the result above, renormalizing column-wise changes the ranking using ranked pairs")









import tkinter as tkr # The next four lines are to import packages needed for the program
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
import random as rd


# import required modules
import tkinter as tkr
from PIL import ImageTk, Image

from tkinter import *
import pandas as pd
  
# Create an instance of tkinter frame
window = Tk()
window.title("Rating Of Favorite Math Research Areas Using Six Rating Methods") # To display title (Goal) of the code 
lbl = tkr.Label(window,text="Ratings: 1-Highest Rated Field,..., 7-Lowest Rated Field", font=("Times New Roman", 13), bg='black', fg='white') # To explain the rating
lbl.grid(column=0,row=9, columnspan=7)
lbl = tkr.Label(window,text="FM-First Method ", font=("Times New Roman", 13), fg='black') # To explain the rating methods since it is abbreviated
lbl.grid(column=0,row=10, columnspan=10)
lbl = tkr.Label(window,text="RP-Ranked Paired", font=("Times New Roman", 13), bg='#458B00', fg='white') # To explain the rating
lbl.grid(column=0,row=11, columnspan=10)
lbl = tkr.Label(window,text="RCRP-Renormalized Columns and Ranked Paired", font=("Times New Roman", 13), fg='black') # To explain the rating
lbl.grid(column=0,row=12, columnspan=10)
lbl = tkr.Label(window,text="RRRP-Renormalized Rows and Ranked Paired", font=("Times New Roman", 13), bg='#458B00', fg='white') # To explain the rating
lbl.grid(column=0,row=13, columnspan=10)
lbl = tkr.Label(window,text="RRFM-Renormalized Rows and First Method", font=("Times New Roman", 13), fg='black') # To explain the rating
lbl.grid(column=0,row=14, columnspan=10)
lbl = tkr.Label(window,text="RCORP-Renormalized Column, Outliers removed and Ranked Paired", font=("Times New Roman", 13), bg='#458B00', fg='white') # To explain the rating
lbl.grid(column=0,row=15, columnspan=10)
# Set the size of the tkinter window
window.geometry("950x400")
window['background']='#6495ED' # To add a background colour to the window
  

  
# Extract number of rows and columns
n_rows = dfg.shape[0]
n_cols = dfg.shape[1]
  
# Extracting columns from the data and
# creating text widget with some
# background color
column_names = dfg.columns
i=0
for j, col in enumerate(column_names):
    text = Text(window, width=16, height=1, bg = "#9BC2E6")
    text.grid(row=i,column=j)
    text.insert(INSERT, col)
      
  
# adding all the other rows into the grid
for i in range(n_rows):
    for j in range(n_cols):
        text = Text(window, width=16, height=1)
        text.grid(row=i+1,column=j)
        text.insert(INSERT, dfg.loc[i][j])
        
#img1=Image.open("dg.png")
#img=ImageTk.PhotoImage(img1)
#panel=tkr.Label(window, image=img)
#panel.grid(column=0, row=18)
  
window.mainloop()

#References
# https://www.statology.org/transpose-data-frame-in-r/ # Helpful in transpose data frame 
#https://www.journaldev.com/45109/normalize-data-in-python # helpful to give insight to renormalizing dataset
#https://www.geeksforgeeks.org/python-tkinter-how-to-display-a-table-editor-in-a-text-widget/?ref=rp #GUI
#https://www.webucator.com/article/python-color-constants-module/ # Choosing Colors


### Created on Mon Apr 11 18:53:10 2022

# @author: Ofe Segun

# importing necessary libraries
import pandas as pd  
import numpy as np
import random as rd

# First Method

df = pd.read_excel('Exce.xlsx', sheet_name="Sheet1") # importing the excel sheet
bab = df.values.tolist() # Put the data in a list

# Next, we summed over the rating for each columns by taking each list 
# and the corresponding column values and put the sum into a list 

torank = [sum([bab[j][i] for j in range(len(bab))]) for i in range(len(bab[0]))]

names = df.columns
chart = [[n] for n in names]
indy = list(range(len(names)))

rankindex = [na for _, na in sorted(zip(torank, indy))]

chart = [chart[j] + [rankindex[j] + 1] for j in range(len(chart))]

order = [names[j] for j in rankindex]




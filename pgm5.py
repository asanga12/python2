import pandas as pd 
pd.set_option('display.width' ,55)

df =  pd.DataFrame({'A' : [0,0,0,0,0,1,1],
'B':[1,2,3,5,4,2,5],
'C':[5,3,4,1,1,2,3]})

adesc= df.groupby('A').describe()
print(adesc)

stacked=adesc.stack()
print(stacked)
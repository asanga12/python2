import pandas  as pd 
names = ['Bob','Asa', 'Jack', 'jin']
grades =[57,89,65,57]
GradeList= zip(names,grades)
df = pd.DataFrame( data =GradeList, columns= ['Names','Grades'])
df.to_csv('test.csv',index=False,header=True,sep=':')
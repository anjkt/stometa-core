import pandas as pd

df =  pd.read_csv('datasheet.csv',sep="~")
df2 = pd.DataFrame(columns=['a','b','c','d','e','f'])
for index, row in df.iterrows():
    a= row['Area']
    b= row['Yeild']
    c = a*b #crop Amount
    d = (a*3)+(c*2)/5 #Expected Amount
    e = 100-(a/b*(d-c)/100,2)
    f = c/d
    g = c/d
    h = (e+(f*100))/2
    g = (f*3+(g*100)*1+h*1)/5
    df2 = pd.Series({'Area':a, 'Yeild':b,'Crop Amount:'c,'Expecting Amount:'d,'Fertility:'e,'Efficiency:'f,'Quality:'h,'Credit Score:'i})

print(df2)

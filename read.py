import pandas as pd

df =  pd.read_csv('teraterm.csv',sep="~")
df2 = pd.DataFrame(columns=['a','b','c','d','e','f','g','h'])
for index, row in df.iterrows():
	#Main Algo
    a= row['Area']
    b= row['Yeild']
    c = a*b #crop Amount
    d = (a*3)+(c*2)/5 #Expected Amount
    e = 100-(a/b*(d-c)/100)
    f = c/d
    g = (e+(f*100))/2
    h = (e*3+(f*100)*1+g*1)/5
    df2 = pd.Series({'Area':a, 'Yeild':b,'Crop Amount':c,'Expecting Amount':d,'Fertility':e,'Efficiency':f,'Quality':g,'Credit Score':h})

print(df2)

# print(df)
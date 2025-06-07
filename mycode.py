import pandas as pd
import os

# This is the data that we have 
dic = {
    "Name": ["Aarav", "Isha", "Rohan", "Priya", "Neha"],
    "City": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Pune"],
    "Salary": [75000, 82000, 91000, 68000, 77000]
}

df = pd.DataFrame(dic)
df.loc[len(df)]=["Subrat","Dehradun",81000]
# Here we will create a folder named data, that will have our csv file of the above data

os.makedirs("Data",exist_ok=True)

path = os.path.join("Data",'sample_dataset.csv')

df.to_csv(path,index=False)


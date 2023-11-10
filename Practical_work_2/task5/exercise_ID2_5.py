import csv
import json
import msgpack
import os.path
import pandas as pd
import pickle

df = pd.read_csv('Alzheimer_s_Disease_and_Healthy_Aging_Data.csv')
df = df[["YearStart", "LocationDesc", "Stratification1", "Stratification2", "Data_Value_Alt",
         "Low_Confidence_Limit", "High_Confidence_Limit"]]

#print(df.dtypes)

df["YearStart"] = df["YearStart"].astype(object)
df["Low_Confidence_Limit"] = df["Low_Confidence_Limit"].replace('.', 'nan').astype(float)
df["High_Confidence_Limit"] = df["High_Confidence_Limit"].replace('.', 'nan').astype(float)

My_dict = dict()

for row in df:
    test_dict = dict()
    if df[row].dtypes in (int, float):
        test_dict["max_value"] = df[row].max()
        test_dict["min_value"] = df[row].min()
        test_dict["avg_value"] = df[row].mean()
        test_dict["sum_value"] = df[row].sum()
        test_dict["std_value"] = df[row].std()
    else:
        for elem in df[row]:
            if ("value_count " + str(elem)) in test_dict:
                test_dict["value_count " + str(elem)] += 1
            else:
                test_dict["value_count " + str(elem)] = 0

    My_dict[row] = test_dict

with open('result_5.json', 'w') as file_json:
    file_json.write(json.dumps(My_dict))

with open('result_5.msgpack', "wb") as file_msgpack:
    file_msgpack.write(msgpack.dumps(My_dict))

with open("result_5.pkl", "wb") as file_pkl:
    file_pkl.write(pickle.dumps(My_dict))

result_df = pd.DataFrame().from_dict(My_dict)
result_df.to_csv("result_5.csv")

ends = ('5.csv', '5.json', '5.msgpack', '5.pkl')
for file in os.scandir():
    if file.name.endswith(ends):
        print(file.name, os.path.getsize(file))





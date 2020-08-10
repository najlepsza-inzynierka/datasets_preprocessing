import os
import pandas as pd


# load dataset
raw_data_dir = os.path.join(os.path.dirname(os.getcwd()), "data_raw")
file_name = "acute_inflammations.csv"
file_path = os.path.join(raw_data_dir, file_name)
dataset = pd.read_csv(file_path, sep="\t")

# temperature has decimal comma in "temperature" column and is string, change it to decimal dot and to float
dataset["temperature"] = dataset["temperature"].str.replace(",", ".").astype("float")

# all other features (and classes) are yes/no strings, change them to true/false booleans
string_to_boolean = lambda string: True if string == "yes" else False
dataset.iloc[:, 1:] = dataset.iloc[:, 1:].applymap(string_to_boolean)

# save results
cleaned_data_dir = os.path.join(os.path.dirname(os.getcwd()), "data_cleaned")
result_file_path = os.path.join(cleaned_data_dir, file_name)
dataset.to_csv(path_or_buf=result_file_path, index=False)


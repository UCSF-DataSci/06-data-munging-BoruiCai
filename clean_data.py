import pandas as pd
import argparse

#function to drop missing value
def drop_missing_value(file):
    #drop all rows with missing value
    file.dropna(inplace = True)
    return file

# function to fix category value's typo
def fix_category_value(file):
   # change all the value we want to change
    typo = {
        'high_income_typo': 'high_income',
        'low_income_typo': 'low_income',
        'lower_middle_income_typo': 'lower_middle_income',
        'upper_middle_income_typo': 'upper_middle_income'
    }
    file['income_groups'] =file['income_groups'].replace(typo)
    return file

# function to drop unreal year
def drop_year(file):
    # keep the file less or equal than 2024
    return file[file['year']<= 2024] 

# function to drop duplicate rows
def drop_duplicate_row(file):
    file.drop_duplicates(inplace=True)
    return file

# function to change data type into correct type
def change_data_type(file):
    typedic ={
        'gender': 'int',
        'year' : 'int',
        'population' : 'int'
    }
    return file.astype(typedic)

# function to drop outlier which is above 99th quantile
def drop_outlier(file):
    q = file["population"].quantile(0.99)
    return file[file['population'] < q]



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="inputname")
    parser.add_argument("output_file", type=str, help="output_name")

    args = parser.parse_args()
    # read the file into panda dataframe, and apply functions
    file =pd.read_csv(args.input_file)
    file = drop_missing_value(file)
    file = fix_category_value(file)
    file = drop_year(file)
    file = drop_duplicate_row(file)
    file = change_data_type(file)
    file = drop_outlier(file)

    file.to_csv(args.output_file, index=False)
    print("success!")



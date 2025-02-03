import pandas as pd

# Define the target symbols
target_symbols = ["‰", "‘", "‡"]

# Function to read and filter data
def read_and_filter(file_path, encoding, delimiter=","):
    data = pd.read_csv(file_path, encoding=encoding, delimiter=delimiter)
    filtered_data = data[data["symbol"].isin(target_symbols)]
    return filtered_data

# Read and filter data from the three files
data1 = read_and_filter("data1.csv", encoding="cp1252")
data2 = read_and_filter("data2.csv", encoding="utf-8")
data3 = read_and_filter("data3.txt", encoding="utf-16", delimiter="\t")

# Combine all filtered data
combined_data = pd.concat([data1, data2, data3])

# Convert the value column to numeric (in case of string encoding issues)
combined_data["value"] = pd.to_numeric(combined_data["value"], errors="coerce")

# Sum values for the target symbols
total_sum = combined_data["value"].sum()

print(f"The total sum of values associated with the symbols is: {total_sum}")
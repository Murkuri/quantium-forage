import os
import pandas as pd

def tabulate_sales(data : str):
    # List to hold csv entries
    entries = []

    # Loop through directory and read information if it's a csv
    for filename in os.listdir(data):
        if filename.endswith(".csv"):
            # Create a dataframe from the given file and append to the entries list
            entry = pd.read_csv(os.path.join(data, filename))
            entries.append(entry)

    # Join the individual data frames
    df = pd.concat(entries)

    # Filter data frame values based on the product column to ensure entries consist of pink morsel
    df = df[df['product'] == 'pink morsel']

    # Append a new column to the dataframe where values are derived from the price * quantity
    df['sales'] = df.apply(lambda x: float(x['price'][1:]) * x['quantity'], axis=1)

    # Cull the product, quantity and price columns from the data frame and rearrange in desired format
    # product | quantity | price | date | region | sales ==> date | region | sales
    df = df.drop(columns=["product", "quantity", "price"])
    # date | region | sales ==> sales | date | region
    df = df.iloc[:, [2,0,1]]

    # Covert dataframe into output csv
    out = "tabulated_sales.csv"
    df.to_csv(out, index=False)
    pass

if __name__ == '__main__':
    directory = "data"
    tabulate_sales(directory)



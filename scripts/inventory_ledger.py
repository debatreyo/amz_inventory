def converter(raw_path):
    """
    raw_path: File path of Amazon summary (day-wise) inventory ledger report.
              File should be in `.csv` format.
              
    clean_name: Name of the cleaned, grouped dataset to be created (in same folder location).
                Eg. IL_XYZ_Oct_24_Mar_25_Grouped.csv
    """
    # import dependecies
    import pandas as pd
    import os

    # load inventory ledger report as dataframe
    raw_data = pd.read_csv(raw_path)

    # data processing
    raw_data["Date"] = pd.to_datetime(raw_data["Date"], format="%m/%d/%Y") # processed format = yyyy-mm-dd
  
    raw_data_subset = raw_data[raw_data["Disposition"] == "SELLABLE"][["Date", "ASIN", "MSKU", "Title", "Starting Warehouse Balance", "Customer Shipments", "Ending Warehouse Balance"]]
    data_grouped = raw_data_subset.groupby(by=["Date", "ASIN"]).agg({"Starting Warehouse Balance":"sum", "Customer Shipments":"sum", "Ending Warehouse Balance":"sum"}).reset_index()

    data_grouped["year"] = data_grouped["Date"].dt.year
    data_grouped["month"] = data_grouped["Date"].dt.month
    data_grouped["day"] = data_grouped["Date"].dt.day

    # Build output file name
    file_dir = os.path.dirname(raw_path)
    file_name = os.path.splitext(os.path.basename(raw_path))[0]
    new_file_name = file_name + "_Grouped.csv"
    file_path = os.path.join(file_dir, new_file_name)

    data_grouped.to_csv(file_path, index=False)
    
    print(f"Grouped data saved to {file_path}")

if __name__ == "__main__":
    raw_path = input("Enter raw file path as raw string: \n")
    converter(raw_path=raw_path)

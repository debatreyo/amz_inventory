# Amazon Inventory Ledger Converter

Transform Amazon’s dense Inventory Ledger report into a **clean**, **daily-level dataset** that’s ready for analysis in Python, Google Sheets, or Excel.

## ✨ Why Use This?
Amazon’s Inventory Ledger is a goldmine of insights — but its **native format is unwieldy**.
Each day’s stock movements can be split into multiple rows across all warehouses, making quick analysis difficult.

**This converter**:
Filters to only `SELLABLE` inventory.
Aggregates data to **daily totals per ASIN**.
Keeps only key columns for planning & visualization.
Saves a new `_Grouped.csv` file for easy use.

## 📦 How to Use
Save your Amazon Inventory Ledger report as a .csv file.

Run the script:
```
python inventory_ledger.py
```

Enter the **full file path** when prompted.
The cleaned, grouped file will be saved in the same folder with `_Grouped.csv` appended to the name.

### 🛠 Example Output Columns
|Columns|Meaning|
|:---:|:---:|
|`Date`|Date in `YYYY-MM-DD` format|
|`ASIN`|Amazon Product Identifier|
|`Starting Warehouse Balance`|Stock position at beginning of dat|
|`Customer Shipments`|Units sold/shipped out to fulfil customer sales|
|`Ending Warehouse Balance`|Stock postion at end of the day|
|`Year`, `Month`, `Day`|Date split out for easier filtering in Spreadsheets|

---

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from src.core.excel_processor import ExcelProcessor
from src.core.type_detector import DataTypeDetector
from src.core.format_parser import FormatParser
from src.core.data_storage import FinancialDataStore

if __name__ == "__main__":
    file_paths = [
        "data/sample/KH_Bank.XLSX",
        "data/sample/Customer_Ledger_Entries_FULL.xlsx"
    ]

    # Initialize classes
    processor = ExcelProcessor()
    detector = DataTypeDetector()
    parser = FormatParser()
    store = FinancialDataStore()

    processor.load_files(file_paths)

    for path, xl in processor.workbooks.items():
        for sheet in xl.sheet_names:
            df = xl.parse(sheet)
            cleaned_df = pd.DataFrame()
            column_types = {}

            print(f"\n File: {path},  Sheet: {sheet}")

            for col in df.columns:
                col_type = detector.detect_column_type(df[col])
                column_types[col] = col_type

                if col_type == "date":
                    cleaned_df[col] = df[col].apply(parser.parse_date)
                elif col_type == "number":
                    cleaned_df[col] = df[col].apply(parser.parse_amount)
                else:
                    cleaned_df[col] = df[col]  # Keep string as-is

                print(f"  → {col} → {col_type}")

            # Use filename+sheet as dataset name
            dataset_name = f"{os.path.basename(path)} | {sheet}"
            store.add_dataset(dataset_name, cleaned_df, column_types)

    # -----------------------------
    #  Phase 4: Sample Queries
    # -----------------------------

    print("\n Sample Range Query:")
    for name in store.data:
        if "Amount" in store.data[name].columns:
            try:
                filtered = store.query_by_range(name, "Amount", 1000, 10000)
                print(f"\nDataset: {name}, Rows: {len(filtered)} in Amount range 1K–10K")
                print(filtered.head())
            except Exception as e:
                print(f" Could not query Amount in {name}: {e}")

    print("\n Sample Group & Aggregate:")
    for name in store.data:
        if "Customer Name" in store.data[name].columns and "Amount" in store.data[name].columns:
            try:
                agg = store.group_and_aggregate(name, "Customer Name", "Amount")
                print(f"\nDataset: {name}")
                print(agg.head())
            except Exception as e:
                print(f" Could not aggregate in {name}: {e}")

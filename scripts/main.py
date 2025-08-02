import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.excel_processor import ExcelProcessor

if __name__ == "__main__":
    file_paths = [
        "data/sample/KH_Bank.XLSX",
        "data/sample/Customer_Ledger_Entries_FULL.xlsx"
    ]

    processor = ExcelProcessor()
    processor.load_files(file_paths)
    processor.get_sheet_info()

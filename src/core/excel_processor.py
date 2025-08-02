import pandas as pd

class ExcelProcessor:
    def __init__(self):
        self.workbooks = {}

    def load_files(self, paths: list[str]):
        for path in paths:
            try:
                xl = pd.ExcelFile(path)
                self.workbooks[path] = xl
                print(f"[✓] Loaded: {path}")
            except Exception as e:
                print(f"[✗] Error loading {path}: {e}")

    def get_sheet_info(self):
        for path, xl in self.workbooks.items():
            print(f"\n File: {path}")
            for sheet in xl.sheet_names:
                df = xl.parse(sheet)
                print(f"   Sheet: {sheet}")
                print(f"     → Rows: {df.shape[0]}, Columns: {df.shape[1]}")
                print(f"     → Columns: {df.columns.tolist()}")

import re
from datetime import datetime
import pandas as pd

class FormatParser:
    def __init__(self):
        pass

    def parse_amount(self, value: str) -> float | None:
        if pd.isna(value): return None
        if isinstance(value, (int, float)): return float(value)

        try:
            str_val = str(value).replace(" ", "").replace(",", "").replace("₹", "").replace("$", "").replace("€", "")

            # Handle negative in parentheses (e.g., (1,200.00))
            if '(' in str_val and ')' in str_val:
                str_val = "-" + str_val.replace("(", "").replace(")", "")

            # Handle trailing negatives (e.g., 1234.56-)
            if str_val.endswith('-'):
                str_val = '-' + str_val[:-1]

            # Handle abbreviations like 1.2M, 3K
            if str_val.endswith(('K', 'M', 'B')):
                multiplier = {'K': 1_000, 'M': 1_000_000, 'B': 1_000_000_000}
                return float(str_val[:-1]) * multiplier[str_val[-1]]

            return float(str_val)
        except:
            return None

    def parse_date(self, value: str) -> datetime | None:
        if pd.isna(value): return None
        if isinstance(value, datetime): return value

        try:
            # Excel serial date
            if str(value).isdigit() and int(value) > 40000:
                return datetime(1899, 12, 30) + pd.to_timedelta(int(value), unit='D')

            # Quarter format
            if "Q" in str(value).upper():
                match = re.match(r'Q([1-4])[- ]?(\d{2,4})', str(value).upper())
                if match:
                    q, year = int(match.group(1)), int(match.group(2))
                    year = 2000 + int(year) if len(str(year)) == 2 else int(year)
                    return datetime(year, (q - 1) * 3 + 1, 1)

            return pd.to_datetime(value, errors='coerce')
        except:
            return None

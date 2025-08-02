import pandas as pd
import re
from dateutil.parser import parse

class DataTypeDetector:
    def __init__(self):
        self.formats_checked = {}

    def detect_column_type(self, series):
        non_null_values = series.dropna().astype(str)
        if len(non_null_values) == 0:
            return 'empty'

        # Check for date
        date_confidence = self._check_dates(non_null_values)
        if date_confidence > 0.6:
            return 'date'

        # Check for number
        number_confidence = self._check_numbers(non_null_values)
        if number_confidence > 0.6:
            return 'number'

        return 'string'

    def _check_dates(self, values):
        match_count = 0
        for val in values[:30]:  # sample first 30 non-null values
            try:
                parse(val, fuzzy=False)
                match_count += 1
            except:
                continue
        return match_count / len(values[:30])

    def _check_numbers(self, values):
        pattern = re.compile(r'^-?[\$\€\₹]?[0-9,\.]+[MBK]?$')
        match_count = 0
        for val in values[:30]:
            if pattern.match(val.replace(" ", "")):
                match_count += 1
        return match_count / len(values[:30])

class FinancialDataStore:
    def __init__(self):
        self.data = {}
        self.metadata = {}

    def add_dataset(self, name, df, column_types):
        self.data[name] = df
        self.metadata[name] = column_types

    def query_by_range(self, name, column, min_val, max_val):
        """Return rows where column value is between min and max."""
        df = self.data[name]
        if column in df.columns:
            return df[(df[column] >= min_val) & (df[column] <= max_val)].copy()
        else:
            raise KeyError(f"Column '{column}' not found in dataset '{name}'")

    def group_and_aggregate(self, name, group_col, agg_col):
        """Group by one column and sum another."""
        df = self.data[name]
        if group_col in df.columns and agg_col in df.columns:
            return df.groupby(group_col, dropna=True)[agg_col].sum().sort_values(ascending=False)
        else:
            raise KeyError(f"One or both columns not found: '{group_col}', '{agg_col}'")

# 📊 Financial Data Parser – Phase 1

This project is part of a multi-phase system designed to parse and process financial data from Excel spreadsheets. In **Phase 1**, we focus on:

- Reading Excel files (even with multiple sheets)
- Extracting and displaying structured metadata
- Laying the foundation for more intelligent parsing in later stages

---

## 📁 Project Structure

```
financial-data-parser/
├── data/
│   └── sample/                         # Sample Excel files
│       ├── KH_Bank.XLSX
│       └── Customer_Ledger_Entries_FULL.xlsx
├── src/
│   └── core/
│       ├── __init__.py
│       └── excel_processor.py         # Class that handles Excel parsing
├── scripts/
│   └── main.py                        # Script to run Phase 1
├── tests/                             # (Empty for now – used in later phases)
├── requirements.txt                   # Python dependencies
└── README.md
```

---

## 🎯 Phase 1 Objectives

| Feature                          | Status |
|----------------------------------|--------|
| Load multiple Excel files        | ✅     |
| Handle multiple sheets           | ✅     |
| Display sheet names              | ✅     |
| Display number of rows/columns   | ✅     |
| Display column headers           | ✅     |

---

## 🧠 How It Works

### `ExcelProcessor` (in `src/core/excel_processor.py`)

This class provides methods to:

- Load Excel files using `pandas.ExcelFile`
- Extract sheet names
- Get the shape (rows × columns) of each sheet
- List all column headers

### `main.py` (in `scripts/main.py`)

Runs the processor on two provided Excel files:
- `KH_Bank.XLSX`
- `Customer_Ledger_Entries_FULL.xlsx`

---

## 🧪 Sample Output

```
[✓] Loaded: data/sample/KH_Bank.XLSX
[✓] Loaded: data/sample/Customer_Ledger_Entries_FULL.xlsx

📄 File: data/sample/KH_Bank.XLSX
  🗂️ Sheet: Sheet1
     → Rows: 1221, Columns: 56
     → Columns: ['GroupHeader.MessageIdentification', ..., 'AdditionalTransactionInformation']

📄 File: data/sample/Customer_Ledger_Entries_FULL.xlsx
  🗂️ Sheet: Customer Ledger Entries
     → Rows: 5505, Columns: 44
     → Columns: ['Posting Date', 'VAT Date', ..., 'Document Subtype']
```

---

## 🚀 How to Run

### 1. Install Requirements

Make sure Python 3.10+ is installed.

```bash
pip install -r requirements.txt
```

### 2. Place Data

Put the Excel files inside this folder:

```
data/sample/
├── KH_Bank.XLSX
└── Customer_Ledger_Entries_FULL.xlsx
```

### 3. Run the Project

```bash
python scripts/main.py
```

If you face a module import error, run with:

```bash
$env:PYTHONPATH="."
python scripts/main.py
```

---

## 📦 Dependencies

- `pandas` – Excel file reading and DataFrame operations
- `openpyxl` – Engine for `.xlsx` file compatibility

Listed in `requirements.txt`.

---

## 📌 Next Phases (Planned)

This project is divided into 4 phases:

| Phase | Description                                         |
|-------|-----------------------------------------------------|
| 1     | ✅ Excel metadata extraction                         |
| 2     | 🔜 Data type detection (dates, numbers, strings)     |
| 3     | 🔜 Format parsing (amounts, dates, currencies)       |
| 4     | 🔜 Optimized data storage & querying                 |

---


## 🤝 Contributing

Found a bug or improvement idea? Feel free to fork and submit a pull request!

---

## 📬 Contact

Maintained by [Bilal Aslam](mailto:bilal.aslam.338658@gmail.com)  
Feel free to reach out for collaboration or questions.

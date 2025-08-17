# 📊 Financial Data Parser & Excel Reconciliation Project (Phases 1 to 5)

This repository contains a complete 5-phase project: financial Excel parsing (Phases 1–4) and Excel sheet reconciliation & subset sum analysis (Phase 5).

## Project Phases

| Phase | Feature                                                  | Status |
|-------|----------------------------------------------------------|--------|
| 1     | Excel loading + metadata extraction                      | ✅ Done |
| 2     | Data type detection (date, number, string, empty)        | ✅ Done |
| 3     | Format parsing (amounts, Excel serials, Q1 2024, etc.)  | ✅ Done |
| 4     | Storage & querying (range filter, grouping, aggregation)| ✅ Done |
| 5     | Excel Sheet Reconciliation & Subset Sum Analysis        | ✅ Done |

---

## 📁 Folder Structure

```
financial-data-parser/
├── data/sample/
│ ├── KH_Bank.XLSX
│ ├── Customer_Ledger_Entries_FULL.xlsx
│ ├── Sheet1_Transactions.xlsx
│ └── Sheet2_Targets.xlsx
├── scripts/
│ ├── main.py
│ └── reconcile.py
├── src/core/
│ ├── init.py
│ ├── excel_processor.py
│ ├── type_detector.py
│ ├── format_parser.py
│ ├── data_storage.py
│ └── sheet_reconciler.py
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

### 🔹 Phase 1 – ExcelProcessor

Reads Excel files and extracts:
- Sheet names
- Rows × columns
- Column headers

> 📄 File: `src/core/excel_processor.py`

---

### 🔹 Phase 2 – DataTypeDetector

For each column, detects if it contains:
- 📅 Dates
- 💰 Numbers
- 🔤 Strings
- ⛔ Empty (null)

> 📄 File: `src/core/type_detector.py`

---

### 🔹 Phase 3 – FormatParser

Normalizes data using:
- Amount parsing (`$1,234.56`, `1.2M`, `₹1,23,456`, `(2,000)`)
- Date parsing (`12/31/2023`, `Q1 2024`, `44927`)

> 📄 File: `src/core/format_parser.py`

---

### 🔹 Phase 4 – FinancialDataStore

Stores parsed data and enables:
- Range queries (e.g., `Amount` between 1K–10K)
- Grouping and aggregation (e.g., `sum(Amount)` by `Customer Name`)

> 📄 File: `src/core/data_storage.py`

---

## 🧪 Sample Output

```
[✓] Loaded: data/sample/KH_Bank.XLSX
[✓] Loaded: data/sample/Customer_Ledger_Entries_FULL.xlsx

📄 File: KH_Bank.XLSX | Sheet1
  → Statement.CreationDateTime → number
  → Statement.Entry.BookingDate.Date → number
  → Statement.Entry.Amount.Value → number

📄 File: Customer_Ledger_Entries_FULL.xlsx | Customer Ledger Entries
  → Posting Date → date
  → Amount → number
  → Customer Name → string

🔍 Sample Range Query:
Dataset: Customer_Ledger_Entries_FULL.xlsx | Customer Ledger Entries
Rows: 1071 in Amount range 1K–10K

📊 Sample Aggregation:
Customer Name
Bonafarm-Bábolna Takarmány Kft.    1.4B
Agrifirm Magyarország Zrt.         883M
```

---

## 🚀 How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Place Excel Files

```
data/sample/
├── KH_Bank.XLSX
└── Customer_Ledger_Entries_FULL.xlsx
```

### 3. Run the Script

```bash
python scripts/main.py
```

✅ If import error occurs, use:

```bash
$env:PYTHONPATH="."
python scripts/main.py
```

---

## 📦 Dependencies

- `pandas` – Excel and data operations
- `openpyxl` – `.xlsx` reading support
- `python-dateutil` – Flexible date parsing
- `re` – Regex for format detection

All are listed in `requirements.txt`.

---

## ✨ Features at a Glance

✅ Multi-sheet Excel support  
✅ Dynamic column type detection  
✅ Amount & date format normalization  
✅ Query & group cleaned data  
✅ Clean modular code (`ExcelProcessor`, `DataTypeDetector`, `FormatParser`, `FinancialDataStore`)

---

## 📬 Contact

Maintained by **Bilal Aslam**  
📧 [bilal.aslam.338658@gmail.com](mailto:bilal.aslam.338658@gmail.com)  
🌐 [github.com/bforbilal2003](https://github.com/bforbilal2003)

---

## 🤝 Contributing

Feel free to fork, star, raise an issue, or submit a pull request.  
This project is open to ideas for expanding:
- More intelligent parsers
- API-based financial enrichment
- Database integrations (e.g., SQLite, PostgreSQL)

---

## 🏁 Final Words

This repo is a complete demonstration of data engineering skills applied to unstructured financial Excel files — transforming messy, raw data into structured, queryable datasets.

Built with ❤️ by Bilal Aslam.

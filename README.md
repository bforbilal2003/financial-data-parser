# 📊 Financial Data Parser – Complete Project (Phases 1 to 4)

This is a complete 4-phase project that parses financial Excel files to extract, clean, classify, and store structured tabular data.

The project is modular, scalable, and supports:
- 📁 Loading multi-sheet Excel files  
- 🧠 Auto-detecting column types (dates, numbers, strings)  
- 🔎 Parsing amounts and dates into clean formats  
- 💾 Storing cleaned datasets for querying and aggregation

---

## 🚦 Project Phases

| Phase | Feature                                                  | Status |
|-------|----------------------------------------------------------|--------|
| 1     | Excel loading + metadata extraction                      | ✅ Done |
| 2     | Data type detection (date, number, string, empty)        | ✅ Done |
| 3     | Format parsing (amounts, Excel serials, Q1 2024, etc.)   | ✅ Done |
| 4     | Storage & querying (range filter, grouping, aggregation) | ✅ Done |

---

## 📁 Folder Structure

```
financial-data-parser/
├── data/
│   └── sample/
│       ├── KH_Bank.XLSX
│       └── Customer_Ledger_Entries_FULL.xlsx
├── scripts/
│   └── main.py
├── src/
│   └── core/
│       ├── __init__.py
│       ├── excel_processor.py      # Phase 1
│       ├── type_detector.py        # Phase 2
│       ├── format_parser.py        # Phase 3
│       └── data_storage.py         # Phase 4
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

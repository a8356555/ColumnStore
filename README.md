# ColumnarStore: A Python Implementation of Columnar Storage

This is an educational implementation of a column-oriented storage engine, inspired by modern OLAP databases like Apache Parquet, ORC, and ClickHouse.

---

## 🧱 Architecture Overview

**Columnar Storage Engine** is composed of:

- **ColumnStore**: Manages multiple segments, each representing a columnar block.
- **Segment**: Stores data in column-oriented format (each column as a file).
- **Encoders**: Apply compression (e.g., Run-Length Encoding, Dictionary Encoding).
- **Metadata**: Stores column statistics like `min`, `max`, and `nulls` for pruning.

---

## ✅ Version Progress

### ✅ Version 1 – Basic Columnar Engine

- `ColumnStore`
  - `insert(record_dict)`
  - `read(filter_column=None, min=None, max=None)`
- `Segment`
  - Each column written to its own file (`col_name.col`)
- Plain data (no compression)

---

### 🔁 Version 2 – Filtering and Min/Max Pruning

- Add `min/max` metadata per column file
- Add range scan using metadata (skip reading irrelevant column files)

---

### ⚡ Version 3 – Compression and Encoding

- Add support for:
  - **RLE** (Run-Length Encoding)
  - **Dictionary Encoding**
  - **Delta Encoding** for numeric columns
- Store encoded binary format per column

---

### 🧵 Version 4 – Append and Merge

- Support appending new segments (immutable)
- Add compaction/merge of segments
- Add bloom filters for fast `WHERE` clause support

---

## 🛠️ How to Use

```python
from column_store import ColumnStore

cs = ColumnStore("data/segment1")

cs.insert({"name": "Alice", "age": 30})
cs.insert({"name": "Bob", "age": 25})
cs.insert({"name": "Alice", "age": 35})

print(cs.read(filter_column="age", min=30))  # Only returns Alice (30, 35)
```

## 📂 Directory Structure

    columnar_store/
    │
    ├── column_store.py      # ColumnStore class
    └── tests/
        ├── test_column_store.py


## 🌱 Branches
- `feature/v1-basic-column-store`: Insert/read in plain column files
- `feature/v2-range-scan`: Min/max metadata, filter support
- `feature/v3-encoding`: Add RLE, dictionary, delta encoding
- `feature/v4-merge-and-index`: Bloom filters, segment merge


## 🧪 Testing
```bash
pytest tests/
```

## 🔮 Future Work
SQL parser

gRPC / REST query API

Zstd/Snappy compression

Predicate pushdown optimization

Segment cache

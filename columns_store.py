from typing import List, Dict

class ColumnStore:
    def __init__(self):
        self.columnar_data = {}  # col: value_list
        self.row_count = 0

    def write(self, record_dict):
        for col, val in record_dict.items():
            if col not in self.columnar_data:
                self.columnar_data[col] = []
            self.columnar_data[col].append(val)

    def read(self, filter_column=None, min=None, max=None) -> List[Dict]:
        result = []
        if filter_column is None:  # return all rows as dict
            row_count = len(next(iter(self.columnar_data.values())))
            for row_id in range(row_count):
                row = {}
                for col, value_list in self.columnar_data.items():
                    row[col] = value_list[row_id]
                result.append(row)
        elif filter_column not in self.columnar_data:
            raise ValueError(f"Filter Column {filter_column} not found")
        else:
            filtered_column_data = self.columnar_data[filter_column]
            filtered_indices = [
                i for i, val in enumerate(filtered_column_data)
                if (min is None or val >= min) and (max is None or val <= max)
            ]
            row_count = len(filtered_indices)
            for row_id in filtered_indices:
                row = {}
                for col, value_list in self.columnar_data.items():
                    row[col] = value_list[row_id]
                result.append(row)
        return result


from typing import List, Dict
from column_segment import ColumnSegment

class ColumnStore:
    def __init__(self):
        self.columnar_data = {}  # col: value_list
        self.row_count = 0

    def write(self, record_dict):
        for col, val in record_dict.items():
            if col not in self.columnar_data:
                column_segment = ColumnSegment(column_name=col)
                self.columnar_data[col] = column_segment
            else:
                column_segment = self.columnar_data[col]
            column_segment.write(val)
        self.row_count += 1

    def read(self, filter_column=None, min=None, max=None) -> List[Dict]:
        result = []
        if filter_column is None:  # return all rows as dict
            for row_id in range(self.row_count):
                result.append(self.read_row(row_id))
        elif filter_column not in self.columnar_data:
            raise ValueError(f"Filter Column {filter_column} not found")
        else:
            filtered_column_data = self.columnar_data[filter_column].read_all()
            filtered_indices = [
                i for i, val in enumerate(filtered_column_data)
                if (min is None or val >= min) and (max is None or val <= max)
            ]
            row_count = len(filtered_indices)
            for row_id in filtered_indices:
                result.append(self.read_row(row_id))
        return result

    def read_row(self, row_id):
        row = {}
        for col, column_segment in self.columnar_data.items():
            row[col] = column_segment.read(row_id)
        return row

    def flush(self):
        for col, column_segment in self.columnar_data.items():
            column_segment.flush()

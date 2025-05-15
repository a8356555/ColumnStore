import pickle

class ColumnSegment:
    def __init__(self, column_name, id=0):
        self.column_name = column_name
        self.data = []
        self.id = id

    def write(self, val):
        self.data.append(val)

    def flush(self):
        file_path = f"{self.column_name}_{self.id}.col"
        with open(file_path, 'wb') as f:
            pickle.dump(self.data, f)
        self.data = []
        self.id += 1

    def load(self, id=None):
        id = id or self.id
        file_path = f"{self.column_name}_{self.id}.col"
        with open(file_path, 'rb') as f:
            self.data = pickle.load(f)

    def read(self, row_id):
        return self.data[row_id]

    def read_all(self):
        return self.data

    def __len(self):
        return len(self.data)

import json
import os

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "data.json")

def get_matrix():
    data_instances = []
    with open(DATA_FILE, "r") as f:
        matrix = json.load(f)
        for matrix_title in matrix:
            data_instances.append(Matrix(matrix_title))

        return data_instances

class Matrix:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def _get_matrix(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_matrix(self, matrix):
        with open(DATA_FILE, "w") as f:
            json.dump(matrix, f, indent=4)

    def add_to_matrix(self):
        matrix = self._get_matrix()

        if self.title not in matrix:
            matrix.append(self.title)
            self._write_matrix(matrix)
            return True
        else:
            print(f"The metadata {self.title} is already registed.")
            return False

    def remove_from_matrix(self):
        matrix = self._get_matrix()

        if self.title in matrix:
            matrix.remove(self.title)
            self._write_matrix(matrix)

if __name__ == "__main__":
    m = Matrix("pmcGsE4u3b")
    m.remove_from_matrix()
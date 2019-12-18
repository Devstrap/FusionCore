from PySide2 import QtWidgets, QtCore
from matrix import Matrix, get_matrix

class App(QtWidgets.QWidget):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("Matrix")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setup_ui()
        self.setup_connections()
        self.populate_meta()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_metaTitle = QtWidgets.QLineEdit()
        self.btn_addMatrix = QtWidgets.QPushButton("Add")
        self.lw_matrix = QtWidgets.QListWidget()
        self.btn_removeMatrix = QtWidgets.QPushButton("Delete")

        self.main_layout.addWidget(self.le_metaTitle)
        self.main_layout.addWidget(self.btn_addMatrix)
        self.main_layout.addWidget(self.lw_matrix)
        self.main_layout.addWidget(self.btn_removeMatrix)

    def setup_connections(self):
        self.btn_addMatrix.clicked.connect(self.add_matrix)
        self.le_metaTitle.returnPressed.connect(self.add_matrix)
        self.btn_removeMatrix.clicked.connect(self.remove_matrix)

    def populate_meta(self):
        self.lw_matrix.clear()
        matrix = get_matrix()
        for matrix in matrix:
            lw_item = QtWidgets.QListWidgetItem(matrix.title)
            lw_item.setData(QtCore.Qt.UserRole, matrix)
            self.lw_matrix.addItem(lw_item)

    def add_matrix(self):
        matrix_title = self.le_metaTitle.text()
        if not matrix_title:
            return False

        matrix = Matrix(title=matrix_title)
        result = matrix.add_to_matrix()
        if result:
            lw_item = QtWidgets.QListWidgetItem(matrix.title)
            lw_item.setData(QtCore.Qt.UserRole, matrix)
            self.lw_matrix.addItem(lw_item)
            self.le_metaTitle.setText("")

    def remove_matrix(self):
        for selected_item in self.lw_matrix.selectedItems():
            matrix = selected_item.data(QtCore.Qt.UserRole)
            matrix.remove_from_matrix()
            self.lw_matrix.takeItem(self.lw_matrix.row(selected_item))

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
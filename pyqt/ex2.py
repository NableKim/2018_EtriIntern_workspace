from PyQt4.QtGui import *

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        # Label, Edit, Button
        lblName = QLabel("Name")
        editName = QLineEdit()
        btnOk = QPushButton("OK")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(editName)
        layout.addWidget(btnOk)

        # Set layout on a MyDialog
        self.setLayout(layout)

# app
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()

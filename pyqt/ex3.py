from PyQt4.QtGui import *

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        # Label, Edit, Button
        lblName = QLabel("Name")
         # 생성자가 아닌 다른 메소드에서 위젯을 사용하기 위해서는
         #"self.위젯객체"와 같이 self를 붙여 인스턴스 변수로 만듦
        self.editName = QLineEdit()
        btnOk = QPushButton("OK")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(self.editName)
        layout.addWidget(btnOk)

        # Set layout on a MyDialog
        self.setLayout(layout)

        btnOk.clicked.connect(self.btnOkClicked)

    def btnOkClicked(self):
        name = self.editName.text()
        QMessageBox.information(self, "Info", name) # params : 부모 위젯, 박스 타이틀, 메세지

# app
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()

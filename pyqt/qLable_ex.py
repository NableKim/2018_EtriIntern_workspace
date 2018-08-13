from PyQt4.QtGui import *

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        label = QLabel()

        # 레이블에 텍스트 쓰기
        #label.setText("Normal")
        label.setText("<a href='https://www.google.com'>www.google.com</a>")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label)

        # Set layout on a MyDialog
        self.setLayout(layout)


# app
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()

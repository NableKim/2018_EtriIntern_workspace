from PyQt4.QtGui import *

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        ed = QLineEdit()

        ed.setText("홍길동")  #텍스트 쓰기
        text = ed.text()    #텍스트 읽기

        # # Watermark로 텍스트 표시
        # ed.setPlaceholderText("이름을 입력하시오")

        # # 텍스트 모두 선택
        # ed.selectAll()

        # 에디트는 읽기 전용으로
        ed.setReadOnly(True)
        #
        # # Password 스타일 에디트
        # ed.setEchoMode(QLineEdit.Password)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(ed)

        # Set layout on a MyDialog
        self.setLayout(layout)


# app
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()

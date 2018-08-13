import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# 메인윈도우
    # 메인 메뉴, 툴바, 하단 상태바 등을 가짐
    # 많은 복잡한 GUI 프로그램에서 종종 쓰임

class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # 윈도우 특성 설정
        self.setWindowTitle('내 윈도우')  # 윈도우 타이클 지정
        self.setGeometry(600, 600, 400, 400)  # 윈도우 위치/크기 설정
        self.setWindowIcon(QIcon('사진이미지.png'))  # 아이콘 지정
        self.statusBar().showMessage('준비')  # 상태바

        # 버튼1 추가
        btn1 = QPushButton('메시지 버튼', self)
        btn1.setToolTip('이 버튼을 누르면 <b>메시지 박스</b>가 나옴')
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 50)
        btn1.clicked.connect(self.btnClicked)

        # 종료 버튼 추가
        btnQuit = QPushButton('종료', self)
        btnQuit.move(50, 100)
        btnQuit.clicked.connect(QCoreApplication.instance().quit)

        # 윈도우 화면에 표시
        self.show()

    def btnClicked(self):
        QMessageBox.information(self, "버튼", "버튼 클릭!")


def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

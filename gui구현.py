import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QToolTip, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
try:
    import Tkinter as tk
except:
    import tkinter as tk




class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MyApp)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

# 이 부분 숙지가 미흡함.




class MyApp(tk.Frame):

  def __init__(self, master):
      tk.Frame.__init__(self, master)
      super().__init__()
      self.initUI()
      self.setWindowTitle('My First Application')
      self.resize(1700, 1550)
     
      QToolTip.setFont(QFont('SansSerif', 10))
      self.setToolTip('This is a <b>QWidget</b> widget')
      #툴팁 설정
      
      
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('web.png'))
      
      #아이콘 설정


      self.setWindowTitle('장애인들을 위한 편의시설 탐색기')
      self.setGeometry(500, 900, 900, 500)
      #프로그램 타이틀 설정
     
      
      pixmap = QPixmap('배경화면.jpg')
      pixmap = pixmap.scaledToHeight(500)
      pixmap = pixmap.scaledToWidth(900)
      lbl_img = QLabel()
      lbl_img.setPixmap(pixmap)
      lbl_size = QLabel("이용해 주셔서 감사합니다")
      lbl_size.setAlignment(Qt.AlignCenter)
      vbox = QVBoxLayout()
      vbox.addWidget(lbl_img)
      vbox.addWidget(lbl_size)
      self.setLayout(vbox)
      self.center()
      #배경화면 이미지 구현
      

      tk.Btn1(self, text="Go to page one",
                  command=lambda: master.switch_frame(commandpage)).pack()
      
      #btn1.setCheckable(True)
      #btn1.toggle()
      #btn1.move(360, 300)
      #btn1.resize(200, 100)
      #btn1.setToolTip('<b>환영합니다!</b>') #툴팁 구현
      #시작하기 버튼
      
      self.show()
  def center(self):
      wr = self.frameGeometry()
      re = QDesktopWidget().availableGeometry().center()
      wr.moveCenter(re)
      self.move(wr.topLeft())
      
      
 
      
      
      
class commandpage(tk.Frame):
    
    def __init__(self):
      super().__init__()
      self.initUI()

    def initUI(self):
      self.setWindowTitle('My First Application')
      self.resize(1700, 1550)
      
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('web.png'))
      
      #아이콘 설정


      self.setWindowTitle('장애인들을 위한 편의시설 탐색기')
      self.setGeometry(500, 900, 900, 500)
      #프로그램 타이틀 설정
     
      
      pixmap = QPixmap('배경화면.jpg')
      pixmap = pixmap.scaledToHeight(500)
      pixmap = pixmap.scaledToWidth(900)
      lbl_img = QLabel()
      lbl_img.setPixmap(pixmap)
      lbl_size = QLabel("이용해 주셔서 감사합니다")
      lbl_size.setAlignment(Qt.AlignCenter)
      vbox = QVBoxLayout()
      vbox.addWidget(lbl_img)
      vbox.addWidget(lbl_size)
      self.setLayout(vbox)
      self.center()
      #배경화면 이미지 구현
      
      
      combo = Combobox(tk())
      combo['values'] = ("1","2","3","4","5","6","7","8","9")
      combo.current(1)
      combo.grid(column=0, row=0)
      
      combo = Combobox(tk())
      combo['values'] = ("1호선","2호선","3호선","4호선","5호선","6호선","7호선","8호선","9호선")
      combo.current(1)
      combo.grid(column=0, row=0)
      
      inputt = Entry(tk(), width=20)
      inputt.grid(column=0, row=3)
      
      click = Button(window, text="확인", command) #이 부분에서 이벤트를 발생시켜야 함
      click.grid(column=1, row=2)

      # 선택창 구현
      
      
      self.show()
      



class mappage(tk.Frame):
    
    def __init__(self):
      super().__init__()
      self.initUI()

    def initUI(self):
      self.setWindowTitle('My First Application')
      self.resize(1700, 1550)
      
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('web.png'))
      
      #아이콘 설정


      self.setWindowTitle('장애인들을 위한 편의시설 탐색기')
      self.setGeometry(500, 900, 900, 500)
      #프로그램 타이틀 설정
     
      
      pixmap = QPixmap('배경화면.jpg')
      pixmap = pixmap.scaledToHeight(500)
      pixmap = pixmap.scaledToWidth(900)
      lbl_img = QLabel()
      lbl_img.setPixmap(pixmap)
      lbl_size = QLabel("이용해 주셔서 감사합니다")
      lbl_size.setAlignment(Qt.AlignCenter)
      vbox = QVBoxLayout()
      vbox.addWidget(lbl_img)
      vbox.addWidget(lbl_size)
      self.setLayout(vbox)
      self.center()
      #배경화면 이미지 구현
      
      self.show()      


    
    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())
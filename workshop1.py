import PyQt5.QtWidgets as qtw
from mo import Ui_MainWindow

class main_window(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(). __init__()
        self.setupUi(self)

        self.send_Button.clicked.connect(self.add_message)
        
    def add_message(self):
        name= self.lineEdit_2.text()
        msg=self.lineEdit.text()
        date=self.lineEdit_3.text()
        whole_text= name + ":" + msg + ":" + date
        message = qtw.QLabel()
        message.setText(whole_text)
        self.message_list.addWidget(message)
app=qtw.QApplication([])
application_window = main_window()
application_window.show()
app.exec()
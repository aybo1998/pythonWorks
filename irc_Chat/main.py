from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import socket
import string
import time 
from ircdesign import Ui_Form   

class boxChat(QWidget,Ui_Form):
	def __init__ (self):
		QWidget.__init__(self)
		self.setupUi(self)
		self.sendButton.clicked.connect(self.send)
		self.testModeBot()
		self.botMode.stateChanged.connect(self.testModeBot)
		
		self.th = ThreadClass()
		self.th.start()
		self.connect(self.th,SIGNAL('tiup'),self.upchat)
		
	def upchat (self,i):
		if len(i.strip())==0:
			pass
		else:
			self.chatBox.appendPlainText(str(i))
	def testModeBot(self):
		#this function return if the mode bot activate or no 
		global stateBotMod
		stateBotMod = self.botMode.isChecked()
		return stateBotMod
	def send(self):
		if len(str(self.lineSend.text()).strip()) == 0 :
			pass
		else :
			if self.lineSend.text() == '/NAMES':
				s.send("NAMES %s \r\n" % CHANNEL)
				self.lineSend.clear()
			else :
				s.send("PRIVMSG %s : %s\r\n" % (CHANNEL,self.lineSend.text()))
				self.chatBox.appendPlainText('<'+NICK+'> : '+self.lineSend.text())
				self.lineSend.clear()
			
	
class ircSettings(QWidget,Ui_Form):
	def __init__(self):
		QWidget.__init__(self)

		# widget of settings irc chat
		self.resize (280,230)
		self.setMaximumSize (280,230)
		self.setMinimumSize  (280,230)
		self.setWindowTitle('Settings of irc chat')
		self.labelServerName = QLabel(text='Server name : ')
		self.labelChannelName = QLabel(text='Channel Name : ')
		self.labelNickname = QLabel(text='Nickname : ')
		self.labelRealName = QLabel(text='Real name : ')
		self.lineServerName = QLineEdit()
		self.lineServerName.setText('irc.freenode.net')
		self.lineChannelName = QLineEdit()
		self.lineChannelName.setText('#gnulug.tn')
		self.lineNickname = QLineEdit()
		self.lineNickname.setText('chatIRC')
		self.lineRealName = QLineEdit()
		self.lineRealName.setText('chatIRC')
		# layout of the label and lineEdit
		self.grid=QGridLayout()
		self.grid.addWidget(self.labelServerName,0,0)
		self.grid.addWidget(self.labelChannelName,1,0)
		self.grid.addWidget(self.labelNickname,2,0)
		self.grid.addWidget(self.labelRealName,3,0)
		self.grid.addWidget(self.lineServerName,0,1)
		self.grid.addWidget(self.lineChannelName,1,1)
		self.grid.addWidget(self.lineNickname,2,1)
		self.grid.addWidget(self.lineRealName,3,1)
		
		#buttons 
		self.buttonBox = QDialogButtonBox(self)
		self.buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
		self.buttonBox.resize(174,34)
		self.buttonBox.accepted.connect(self.connect)
		self.buttonBox.rejected.connect(exit)
		
		# layout of the widget(layout of the label and lineEdit + Buttons)
		self.layout = QVBoxLayout(self)
		self.layout.addLayout(self.grid)
		self.layout.addWidget(self.buttonBox)
	def connect(self):
		global HOST
		HOST = self.lineServerName.text() 
		global PORT
		PORT = 6667
		global NICK
		NICK = self.lineNickname.text()
		global IDENT
		IDENT = self.lineNickname.text()
		global REALNAME
		REALNAME = self.lineRealName.text()
		global CHANNEL
		CHANNEL = self.lineChannelName.text()
		global readbuffer
		readbuffer = ""
		if len(HOST) == 0 or len(NICK) == 0 or len(REALNAME) == 0 or len(CHANNEL) == 0 :
			QMessageBox.warning(self,'Warning','Please fill the spacese')
		else:
			#if you complite the form the Box of chat open
			self.close()
			self.box=boxChat()
			self.box.show()



class ThreadClass(QThread):
	def __init__(self,parent=None):
		super(ThreadClass,self).__init__(parent)
	
	def run(self):
		global s
		s=socket.socket( )
		s.connect((HOST, PORT))
		s.send("NICK %s\r\n" % NICK)
		s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
		s.send("JOIN %s\r\n" % CHANNEL)
		global readbuffer
		global va
		
		while 1:
			readbuffer=readbuffer+s.recv(1024)
			temp=string.split(readbuffer, "\n")
			readbuffer=temp.pop( )
			for line in temp:
				va =''
				msg = line
				line=string.rstrip(line)
				line=string.split(line)
				print msg
				if(line[0]=="PING"):
					s.send("PONG %s\r\n" % line[1])
				elif(line[1]=="PRIVMSG"):
					msOfpepole = ' '.join(line[3:])[1:]
					va = '<'+line[0][1:int(line[0].find('!'))]+'> : '+ msOfpepole
					listFun = ['help','time','date']
					if stateBotMod==True:
						if "".join(msOfpepole.split()) == NICK+':time':
							t = time.localtime()
							t = 'The time is :'+str(t.tm_hour)+':'+str(t.tm_min)
							s.send("PRIVMSG %s : %s\r\n" % (CHANNEL,t))
							va +='\n'+'<'+NICK+'> : '+t
						elif "".join(msOfpepole.split()) == NICK+':date':
							t = time.localtime()
							t = 'The time is :'+str(t.tm_mday)+'/'+str(t.tm_mon)+'/'+str(t.tm_year)
							s.send("PRIVMSG %s : %s\r\n" % (CHANNEL,t))
							va +='\n'+'<'+NICK+'> : '+t
						elif "".join(msOfpepole.split()) == NICK+':help':
							s.send("PRIVMSG %s : %s\r\n" % (CHANNEL," - ".join(listFun)))
							va +='\n'+'<'+NICK+'> : '+" - ".join(listFun)
				elif(line[1]=="JOIN" or line[1]=="QUIT"):
					s.send("NAMES %s\r\n" % CHANNEL)
			self.emit(SIGNAL('tiup'),str(va))
	
class main():
	def __init__(self):
		app = QApplication(sys.argv)
		w = ircSettings()
		w.show()
		app.exec_()
		
if __name__=='__main__':
	
	main()
	

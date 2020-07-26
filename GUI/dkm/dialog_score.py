# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_score.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb0 = QtWidgets.QComboBox(Dialog)
        self.cb0.setObjectName("cb0")
        self.cb0.addItem("")
        self.horizontalLayout.addWidget(self.cb0)
        self.cb1 = QtWidgets.QComboBox(Dialog)
        self.cb1.setObjectName("cb1")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.horizontalLayout.addWidget(self.cb1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lw1 = QtWidgets.QListWidget(Dialog)
        self.lw1.setObjectName("lw1")
        self.horizontalLayout_3.addWidget(self.lw1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lw2 = QtWidgets.QListWidget(Dialog)
        self.lw2.setObjectName("lw2")
        self.horizontalLayout_3.addWidget(self.lw2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.scorelabel = QtWidgets.QLabel(Dialog)
        self.scorelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scorelabel.setObjectName("scorelabel")
        self.gridLayout.addWidget(self.scorelabel, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #self.pushButton.clicked.connect(self.calculate)     #To use the method 'calculate' as slot for clicked signal emitted by 'pushbutton'
        
        import sqlite3      #To get name from database 
        conn = sqlite3.connect('cricket.db')
        sql="select name from teams"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            self.cb0.addItem(row[0])        
        conn.close()
        
        self.pushButton.clicked.connect(self.calculate)     #To use the method 'calculate' as slot for clicked signal emitted by 'pushbutton'
        
        
      
   
   
        
        

    
    def calculate(self):
        import sqlite3
        conn = sqlite3.connect('cricket.db')
        team=self.cb0.currentText()
        self.lw1.clear()
        sql1="select players, value from teams where name='"+team+"';"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        #-----------------------------------------------------------------------print (row[0])
        selected=row[0].split(',')
        #-----------------------------------------------------------------------print (selected)
        self.lw1.addItems(selected)
        teamttl=0
        self.lw2.clear()
        match=self.cb1.currentText()
        
        for i in range(self.lw1.count()):
            ttl, batscore, bowlscore, fieldscore=0,0,0,0
            nm=self.lw1.item(i).text()
            #table=conn("select * from matches inner join stats on matches.players=stats.players")
            #cursor=conn(table)
            cursor=conn.execute("select * from match_stats where players='"+nm+"';")     
            row=cursor.fetchone()
            #print (row)
            #batscore=row[1]
            #print(type(batscore))
            batscore=int(row[1]/2)
            if batscore>=50: batscore+=5        #Rule for Batting:- Additional 5 points for half century
            if batscore>=100: batscore+=10      ##Rule for Batting:- Additional 10 points for century
            if row[1]>0:
                sr=row[13]/row[3]
                if sr>=80 and sr<100: batscore+=2       #Batting rule: 2 points for strike rate (runs/balls faced) of 80-100
                if sr>=100:batscore+=4      #batting rule: Additional 4 points for strike rate>100
            batscore=batscore+row[3]    #1 point for hitting a boundary (four)
            batscore=batscore+2*row[4]      #2 points for over boundary (six)
            #print ("batting score=", batscore)
            bowlscore=row[8]*10         #bowling rule: 10 points for each wicket
            if row[8]>=3: bowlscore=bowlscore+5         #Bowling rule: Additional 5 points for three wickets per innings
            if row[8]>=5: bowlscore=bowlscore=bowlscore+10      #Bowling rule: 10 points for each wicket
            if row[7]>0:
                er=6*row[7]/row[5]
                #print ("eco:",er)
                if er<=2: bowlscore=bowlscore+10        #BOwLing rule: 10 points for economy rate less than 2
                if er>2 and er<=3.5: bowlscore=bowlscore+7      #BOWLING rule: 7 points for economy rate between 2 and 3.5
                if er>3.5 and er<=4.5: bowlscore=bowlscore+4    #Bowling rule: 4 points for economy rate (runs given per over) between 3.5 and 4.5
            fieldscore=(row[9]+row[10]+row[11])*10          #Fielding Rule:- 10 points each for catch/stumping/run out  
            ttl=batscore+bowlscore+fieldscore
            self.lw2.addItem(str(ttl))
            teamttl=teamttl+ttl
        
#        teamttl=1000
        self.scorelabel.setText(str(teamttl))



    



#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "<b>Evaluating the Performance of Fantasy Team</b>"))
        self.cb0.setItemText(0, _translate("Dialog", "Select Team"))
        self.cb1.setItemText(0, _translate("Dialog", "Select Match"))
        self.cb1.setItemText(1, _translate("Dialog", "Match1"))
        self.cb1.setItemText(2, _translate("Dialog", "Match2"))
        self.cb1.setItemText(3, _translate("Dialog", "Match3"))
        self.cb1.setItemText(4, _translate("Dialog", "Match4"))
        self.cb1.setItemText(5, _translate("Dialog", "Match5"))
        self.label_2.setText(_translate("Dialog", "<b>Players</b>"))
        self.label.setText(_translate("Dialog", "<b>Score</b>"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))
        self.scorelabel.setText(_translate("Dialog", "00"))









#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------




if __name__ == "__main__":
    import sqlite3
    conn=sqlite3.connect('cricket.db')
#    print('Opened database successfully!!!')    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.e1 = QtWidgets.QLineEdit(self.centralwidget)
        self.e1.setObjectName("e1")
        self.horizontalLayout_11.addWidget(self.e1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        self.e2 = QtWidgets.QLineEdit(self.centralwidget)
        self.e2.setObjectName("e2")
        self.horizontalLayout_11.addWidget(self.e2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.e3 = QtWidgets.QLineEdit(self.centralwidget)
        self.e3.setObjectName("e3")
        self.horizontalLayout_11.addWidget(self.e3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.e4 = QtWidgets.QLineEdit(self.centralwidget)
        self.e4.setObjectName("e4")
        self.horizontalLayout_11.addWidget(self.e4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_2.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_2.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_2.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_2.addWidget(self.rb4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setObjectName("list1")
        self.verticalLayout.addWidget(self.list1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setObjectName("btn1")
        self.verticalLayout.addWidget(self.btn1)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.l1 = QtWidgets.QLineEdit(self.centralwidget)
        self.l1.setObjectName("l1")
        self.horizontalLayout_3.addWidget(self.l1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setObjectName("list2")
        self.verticalLayout_4.addWidget(self.list2)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setObjectName("btn2")
        self.verticalLayout_4.addWidget(self.btn2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionInstruction = QtWidgets.QAction(MainWindow)
        self.actionInstruction.setObjectName("actionInstruction")
        self.actionRule = QtWidgets.QAction(MainWindow)
        self.actionRule.setObjectName("actionRule")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionInstruction)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionRule)
        self.menuHelp.addSeparator()
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #MainWindow.customContextMenuRequested.connect(self.context_menu)        #To connect the Cus.Cont.MenuReq. signal

# To connect the ctg method to radio button!!!                
        self.rb1.toggled.connect(self.ctg)
        self.rb2.toggled.connect(self.ctg)
        self.rb3.toggled.connect(self.ctg)
        self.rb4.toggled.connect(self.ctg) 
        
# Declaration of class attributes
        self.bat=0
        self.bow=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0
        self.retranslateUi(MainWindow)
        
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)       #To triggred signAL emitted by the 'Manage Team' menu *for menufunction() as a event handler
        
        self.list1.itemDoubleClicked.connect(self.removelist1)      #These two methods are used as event handlers for itemDoubleClicked signal of List1 and List2 respectivily
        self.list2.itemDoubleClicked.connect(self.removelist2)
        
        self.menuHelp.triggered[QtWidgets.QAction].connect(self.helpfunction)       #'helpfunction' as a event handler triggred signal emmitted by the 'Help' menu
        
    
               
      
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------          

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "<b>Welcome to Fantasy Cricket game!</b>"))
        self.label.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.label_2.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.label_3.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.label_4.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.label_9.setText(_translate("MainWindow", "<h3>Player Available</h3>"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOW"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.btn1.setText(_translate("MainWindow", "Available Points : 1000"))
        self.label_10.setText(_translate("MainWindow", "<h3>Selected Players</h3>"))
        self.label_6.setText(_translate("MainWindow", "Team name "))
        self.btn2.setText(_translate("MainWindow", "Points used : "))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))         #
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))      #
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEVALUATE_Team.setShortcut(_translate("MainWindow", "Alt+E")) #
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionInstruction.setText(_translate("MainWindow", "Instructions"))
        self.actionRule.setText(_translate("MainWindow", "Rules"))
        
   
    
    
 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    def menufunction(self, action):     #Event Handling:- To perform the selected option         ( *action=the action selected from menu)
        txt=(action.text())
        if txt=="NEW Team":        	## Reset the class attributes
            self.bat=0
            self.bow=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.list1.clear()
            self.list2.clear()
            self.l1.setText("")
            self.showstatus()
            text, ok = QtWidgets.QInputDialog.getText(MainWindow,  'Team Selector', 'Enter name of team:')
            if ok:
                self.l1.setText(str(text))
        if txt=='SAVE Team':
            # Iterate over the selected players list to create a string of player names separated by commas
            selected=""
            count=self.list2.count()
            for i in range(count):
                selected=selected+self.list2.item(i).text()
                if i<count-1:
                    selected=selected+","
            self.saveteam(self.l1.text(),selected,self.used)
        if txt=="OPEN Team":
        	# Reset the class attributes
            self.bat=0
            self.bow=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.list1.clear()
            self.list2.clear()
            self.l1.setText("")
            self.showstatus()
            self.openteam()
        if txt=="EVALUATE Team":
            from dialog_score import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()
            
            
            
            
    def helpfunction(self, action):         #Added menu functionality method for 'Help' section
        txt=(action.text())
        if txt=="Rules":
            from rule import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()    
        if txt=="Instructions":
            from instruction import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()

  
        

    def saveteam(self,nm,string,val):       #Function:- to add data of new team inside the database
        '''
        nm: Name of team
        string: List of players in team separated by commas
        val: Points used out of 1000
        '''
        if self.bat+self.bow+self.ar+self.wk!=11:       # If total players is not 11, show error pop-up
            self.showdlg("Insufficient players")
            return
        sql="INSERT INTO teams (name, players, value) VALUES ('"+nm+"','"+string+"','"+str(val)+"');"
        try:
            cur=conn.execute(sql)
            conn.commit()
            self.showdlg ("Team Saved successfully")
        except:
            self.showdlg ("error in operation")
            conn.rollback()

    

    def openteam(self):
        sql="select name from teams"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            teams.append(row[0])
        team, ok = QtWidgets.QInputDialog.getItem(MainWindow, "Team Selector",
                "Choose a team", teams, 0, False)
        if ok and team:
            self.l1.setText(team)
        sql1="select players, value from teams where name='"+team+"'"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')      # Separate player names by comma and store them in a list
        self.list2.addItems(selected)       # Populate list2 with the names of selected players
        self.used=row[1]
        self.avl=1000-int(row[1])
        count=self.list2.count()
        for i in range(count):      # Iterate over selected players to count number of players in each category
            player=self.list2.item(i).text()
            sql="select ctg from stats where players='"+player+"'"
            cur=conn.execute(sql)
            row=cur.fetchone()
#            ctgr=row[0]
#            if ctgr=="BAT":self.bat+=1
#            if ctgr=="BOW":self.bow+=1
#            if ctgr=="AR":self.ar+=1
#            if ctgr=="WK":self.wk+=1            
            
        self.showstatus()


    '''
    def context_menu(MainWindow):       #Event Handling for Context menu on right click to show pop-up window
        MainWindow.menu = QtWidgets.QMenu()
        MainWindow.menu.addAction("Profile")
        MainWindow.menu.triggered[QtWidgets.QAction].connect(MainWindow.profile)
        MainWindow.menu.exec_(QtGui.QCursor.pos())
    '''       

        
    def fillList(self,ctgr):        #methods:- Populate list1 with players of given category *ctgr=Category of players
        if self.l1.text()=='':      # If name of team is not already selected, show error pop-up
            self.showdlg("Enter name of team")
            return
        self.list1.clear()
        cursor = conn.execute("SELECT players from stats where ctg='"+ctgr+"'")
        for row in cursor:
            selected=[]
            for i in range(self.list2.count()):
                selected.append(self.list2.item(i).text())
            if row[0] not in selected:self.list1.addItem(row[0])


    def ctg(self):      # Event Handling for radio button:-
        ctgr=''
        if self.rb1.isChecked()==True:ctgr='BAT'
        if self.rb2.isChecked()==True:ctgr='BOW'
        if self.rb3.isChecked()==True:ctgr='AR'
        if self.rb4.isChecked()==True:ctgr='WK'
       	
        self.fillList(ctgr)
  
    
    def criteria(self,ctgr, item):      #To check for criterion for each category and show appropriate error pop-up
        msg=''
        if ctgr=="BAT" and self.bat>=5:msg="Batsmen not more than 5"        #ctgr=category of player
        if ctgr=="BOW" and self.bow>=5:msg="bowlers not more than 5"
        if ctgr=="AR" and self.ar>=3:msg="Allrounders not more than 3"
        if ctgr=="WK" and self.wk>=1:msg="Wicketkeepers not more than 1"
        if msg!='' or self.avl<=0:
            
            msg = 'You have exhausted your points'
            self.showdlg(msg)
            return False
        
        if ctgr=="BAT":self.bat+=1
        if ctgr=="BOW":self.bow+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1
        cursor = conn.execute("SELECT players,value from stats where players='"+item.text()+"'")
        row=cursor.fetchone()
        self.avl=self.avl-int(row[1])
        self.used=self.used+int(row[1])
        return True
    
            
    def showstatus(self):       #Functionality:- Show the available and used points 
        self.e1.setText(str(self.bat))
        self.e2.setText(str(self.bow))
        self.e3.setText(str(self.ar))
        self.e4.setText(str(self.wk))
        self.btn1.setText("Points Available : {}".format(self.avl))
        self.btn2.setText("Points Used : {}".format(self.used))

        
    def removelist1(self, item):        #Event Handling:- to remove players from list1 and add them to list2
        ctgr=''
        if self.rb1.isChecked()==True:ctgr='BAT'
        if self.rb2.isChecked()==True:ctgr='BOW'
        if self.rb3.isChecked()==True:ctgr='AR'
        if self.rb4.isChecked()==True:ctgr='WK'
        ret=self.criteria(ctgr, item)
        if ret==True:                         
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item.text())
            self.showstatus()

                         
    def showdlg(self, msg):     #Function: Show the dialog box with message
        Dialog = QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Please Select Team")
        ret=Dialog.exec()                         


    def removelist2(self, item):        #Event Handling:- Remove Players from list2 and add them back to list1
        self.list2.takeItem(self.list2.row(item))
        
        cursor = conn.execute("SELECT players, value, ctg from stats where players='"+item.text()+"'")
        row=cursor.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.rb1.isChecked()==True:self.list1.addItem(item.text())
        if ctgr=="BOW":
            self.bow-=1
            if self.rb2.isChecked()==True:self.list1.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.rb3.isChecked()==True:self.list1.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.rb4.isChecked()==True:self.list1.addItem(item.text())
        self.showstatus()
	
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    import sqlite3
    conn=sqlite3.connect('cricket.db')
#    print('Opened database successfully!!!')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#=======================================================================================================================================================
#==========================================================================================================================================================================

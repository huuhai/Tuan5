# -*- coding: utf-8 -*-
from msvcrt import getch
from UserView import UserView
from Database import Database
from Menu_Display import Menu_Display


class Controller:
    userView = UserView()
    database = Database()
    menu_Display = Menu_Display()

    def signUp(self):
        self.userView.signUp()
        self.database.signUp(self.userView.username, self.userView.password, self.userView.fullname,
                             self.userView.birthday, self.userView.sex,
                             self.userView.address)

    def logIn(self):
        self.userView.logIn()
        self.database.logIn(self.userView.username, self.userView.password)

    def showMessageSent(self, username):
        self.menu_Display.notify_Ctr_N_Ctr_B()
        self.database.showMessageSent(username)

    def showMessageReceiver(self, username):
        self.menu_Display.notify_Ctr_N_Ctr_B()
        self.database.showMessageReceived(username)
        self.menu_Display.notify_Ctr_R()
        Ctr_R = ord(getch())
        if Ctr_R == 18:
            self.menu_Display.notify_ChoiceSendMessage()
            self.key_shortcut(username)

    def sendMessage(self, username):
        self.menu_Display.notify_ChoiceSendMessage()
        self.key_shortcut(username)

    def key_shortcut(self, username):
        Ctr_L = ord(getch())
        if Ctr_L == 12:
            print '\n'
            self.database.Ctr_L(username)
        else:
            self.userView.nhanTin()
            self.database.sendMessage(username, self.userView.receiver, self.userView.content)

    def editInfoFriend(self, username):
        self.userView.inputNameFriend()
        if self.database.check2(self.userView.editInfoFriend):
            if self.database.checkTableFriend(username, self.userView.editInfoFriend):
                self.database.showInfoFriend(username, self.userView.editInfoFriend)
                print '\t\t-----------SUA THONG TIN BAN BE-----------'
                self.userView.inputInfo()
                self.database.editInfoFriend(self.userView.editInfoFriend, self.userView.fullname,
                                             self.userView.birthday, self.userView.sex,
                                             self.userView.address)
            else:
                self.menu_Display.notifyFailEdit()
        else:
            self.menu_Display.notifyFailAccount()

    def listFriend(self, username):
        self.database.listFriend(username)

    def addFriend(self, username):
        self.userView.inputAddFriend()
        self.database.addFriend(username, self.userView.Friend)

    def block(self, username):
        self.userView.inputBlockFriend()
        self.database.block(username, self.userView.block)

    def showInfo(self, username):
        self.database.showInfo(username)

    def sortFriend(self, username):
        self.database.sortFriend(username)

    def sortFriendOfCity(self, username):
        self.database.sortFriendOfCity(username)

    def Ctr_L(self, username):
        self.menu_Display.notify_ChoiceSendMessage()
        # Hàm getch() sẽ nhận dạng phím mà bạn ấn vào và hàm ord() sẽ chuyển nó về mã ASCII
        self.key_shortcut(username)

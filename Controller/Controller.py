# -*- coding: utf-8 -*-
from msvcrt import getch
import os
from UserView import UserView
from Database import Database

# from User import User

userView = UserView()
database = Database()


class Controller:

    def signUp(self):
        # user = User()
        userView.dangKy()
        # database.signUp(user.username, user.password, user.fullname, user.birthday, user.sex, user.address)
        database.signUp(userView.username, userView.password, userView.fullname, userView.birthday, userView.sex,
                        userView.address)

    def logIn(self):
        userView.nhap()
        database.logIn(userView.username, userView.password)

    def showMessageSent(self, username):
        print '\n'
        os.system('cls')
        print '\n\nNhan Ctr+N de hien thi danh sach hoac nhan Ctr+B de tro ve MENU TIN NHAN !!!\n\n'
        database.showMessageSent(username)

    def showMessageReceiver(self, username):
        print '\n'
        os.system('cls')
        print '\nNhan Ctr+N de hien thi danh sach hoac nhan Ctr+B de tro ve MENU TIN NHAN !!!\n\n'
        database.showMessageReceived(username)
        print '\nNeu muon tra loi tin nhan thi nhan Ctr+R hoac an phim bat ky de thoat !!!\n\n'
        Ctr_R = ord(getch())
        if Ctr_R == 18:
            print '\n\nCo 2 cach de gui tin nhan:\n1. Nhap vao tai khoan nguoi nhan\n2. Bam truc tiep Ctr+L\n\n'
            print 'Nhap ten nguoi nhan: '
            Ctr_L = ord(getch())
            if Ctr_L == 12:
                print '\n\n'
                database.Ctr_L(username)
            else:
                userView.nhanTin()
                database.sendMessage(username, userView.receiver, userView.content)


    def sendMessage(self, username):
        print '\n\nCo 2 cach de gui tin nhan:\n1. Nhap vao tai khoan nguoi nhan\n2. Bam truc tiep Ctr+L\n\n'
        print 'Nhap ten nguoi nhan: '

        Ctr_L = ord(getch())
        if Ctr_L == 12:
            print '\n\n'
            database.Ctr_L(username)
        else:
            userView.nhanTin()
            database.sendMessage(username, userView.receiver, userView.content)


    def editInfoFriend(self, username):
        userView.editInfoFriend = raw_input('Nhap ten nguoi ban muon sua thong tin: ')
        if database.check2(userView.editInfoFriend):
            if database.checkTableFriend(username, userView.editInfoFriend):
                database.showInfoFriend(username, userView.editInfoFriend)
                print '\t\t-----------SUA THONG TIN BAN BE-----------'
                userView.fullname = raw_input('Nhap day du ho va ten: ')
                userView.birthday = raw_input('Ngay sinh: ')
                userView.sex = raw_input('Gioi tinh: ')
                userView.address = raw_input('Dia chi: ')
                database.editInfoFriend(userView.editInfoFriend, userView.fullname, userView.birthday, userView.sex,
                                        userView.address)
            else:
                print '\t\tChua ket ban. Ko the sua !!!\n'
        else:
            print '\t\tTai khoan ko ton tai hoac da bi xoa !!!\n'


    def listFriend(self, username):
        database.listFriend(username)


    def addFriend(self, username):
        userView.Friend = raw_input('Nhap ten ban be muon them: ')
        database.addFriend(username, userView.Friend)


    def block(self, username):
        userView.block = raw_input('Nhap ten ban be muon block: ')
        database.block(username, userView.block)


    def showInfo(self, username):
        database.showInfo(username)


    def sortFriend(self, username):
        database.sortFriend(username)


    def sortFriendOfCity(self, username):
        database.sortFriendOfCity(username)


    def Ctr_L(self, username):
        print '\nCo 2 cach de gui tin nhan:\n1. Nhap vao tai khoan nguoi nhan\n2. Bam truc tiep Ctrl+L de hien thi danh sach ban be\n\n'
        print 'Nhap ten nguoi nhan: '

        # Hàm getch() sẽ nhận dạng phím mà bạn ấn vào và hàm ord() sẽ chuyển nó về mã ASCII
        Ctr_L = ord(getch())
        if Ctr_L == 12:
            print(Ctr_L)
            # để dừng màn hình xem thôi
            # i = input()
            database.Ctr_L(username)
        else:
            userView.nhanTin()
            database.sendMessage(username, userView.receiver, userView.content)

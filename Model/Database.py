# -*- coding: utf-8 -*-
import sqlite3
import time
import os
from msvcrt import getch
import Menu


class Database:

    def connect_db(self):
        try:
            con = sqlite3.connect('DuLieu.db')
        except sqlite3.Error as e:
            print ("Error %s " % e.args[0])
        return con

    def signUp(self, username, password, fullname, birthday, sex, address):
        if self.check(username, password):
            print "\tTai khoan da ton tai. Vui long chon tai khoan khac !!!"
        else:
            try:
                conn_signUp = self.connect_db()
                conn_signUp.execute("INSERT INTO AccountInfo VALUES(?,?,?,?,?,?)",
                                    (username, password, fullname, birthday, sex, address))
                conn_signUp.commit()
                print '\n\t\t\tDang ky thanh cong !!!\n'
            except sqlite3.Error as e:
                print ("Error %s " % e.args[0])
            # finally:
            # if conn_signUp:
            # conn_signUp.close()

    def check(self, username, password):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT username, password FROM AccountInfo where username=? and password=?",
                        (username, password))

            rows = cur.fetchall()

            for row in rows:
                if row[0] == username and row[1] == password:
                    return True
                else:
                    return False

    def logIn(self, username, password):
        os.system('cls')
        menu = Menu.Menu()
        if self.check(username, password):
            menu.choice2(username, password)
        else:
            print 'Dang nhap ko thanh cong !!!\n'

    def showMessageSent(self, sender):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT receiver, content, TimeDate, seen FROM Message where sender=?", (sender,))

            rows = cur.fetchall()
            self.key_Shortcut(rows)

    def showMessageReceived(self, receiver):
        if self.checkReceiverMessage(receiver):
            self.updateSeenMessage(receiver)
            conn = self.connect_db()
            with conn:
                cur = conn.cursor()
                cur.execute("select sender, content, TimeDate from Message where receiver =?", (receiver,))

                rows = cur.fetchall()
                self.key_Shortcut(rows)
        else:
            print '\n\n\t\tChua nhan duoc tin nhan nao !!!\n\n'

    # phím tắt
    def key_Shortcut(self, rows):
        for row in rows:
            Ctr_key = ord(getch())
            if Ctr_key == 14:
                print row
            elif Ctr_key == 2:
                break

    def updateSeenMessage(self, receiver):
        conn = self.connect_db()
        conn.execute("update Message set seen ='da doc' where receiver=?", (receiver,))
        conn.commit()

    def checkReceiverMessage(self, receiver):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select distinct receiver from Message where receiver =?", (receiver,))

            rows = cur.fetchall()
            if self.return_Boolean(rows, receiver):
                return True
            else:
                return False

    def sendMessage(self, sender, receiver, content):
        localtime = time.asctime(time.localtime(time.time()))
        if not self.check2(receiver):
            print '\nTai khoan ko ton tai hoac da bi xoa !!!\n'
        else:
            if not self.checkBlock(receiver, sender):
                conn = self.connect_db()
                conn.execute("INSERT INTO Message(sender, receiver, content, TimeDate) VALUES (?,?,?,?)",
                             (sender, receiver, content, localtime))
                conn.commit()
                print '\n\t\tGui thanh cong !!!\n'
            else:
                print '\tKo the gui tin nhan. ' + receiver + ' da chan ban !!!'

    def checkBlock(self, username, block):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select blocked from Block where username=? and blocked=?", (username, block,))

            rows = cur.fetchall()
            if self.return_Boolean(rows, block):
                return True
            else:
                return False

    # kt dữ liệu nhập vào với database
    def return_Boolean(self, rows, tmp_Name):
        for row in rows:
            if row[0] == tmp_Name:
                return True
            else:
                return False

    def check2(self, username):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select username from AccountInfo where username =?", (username,))

            rows = cur.fetchall()
            if self.return_Boolean(rows, username):
                return True
            else:
                return False

    def checkTableFriend(self, username, Friend):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select friend from Friend where username =? and friend =?", (username, Friend))

            rows = cur.fetchall()
            if self.return_Boolean(rows, Friend):
                return True
            else:
                return False

    def showInfoFriend(self, username, Friend):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute(
                "select AccountInfo.fullname,AccountInfo.birthday,AccountInfo.sex,AccountInfo.address,Friend.TimeDate "
                "from AccountInfo,Friend "
                "where AccountInfo.username=Friend.friend and Friend.username=? and Friend.friend=?",
                (username, Friend))

            rows = cur.fetchall()
            self.printData(rows)

    def editInfoFriend(self, Friend, fullname, birthday, sex, address):
        conn = self.connect_db()
        conn.execute("update AccountInfo set fullname=?, birthday=?, sex=?, address=? where username=?",
                     (fullname, birthday, sex, address, Friend))
        conn.commit()
        print '\t\tUpdate thanh cong !!!\n'

    def listFriend(self, username):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select id, friend, TimeDate from Friend where username=? order by TimeDate desc", (username,))

            rows = cur.fetchall()
            self.printData(rows)

    def printData(self, rows):
        for row in rows:
            print row

    def addFriend(self, username, Friend):
        localtime = time.asctime(time.localtime())
        if not self.check2(Friend):
            print '\t\tTai khoan ko ton tai hoac da bi xoa !!!\n'
        else:
            if not self.checkTableFriend(username, Friend):
                conn = self.connect_db()
                conn.execute("INSERT INTO Friend (username, friend, TimeDate) VALUES (?,?,?)",
                             (username, Friend, localtime))
                conn.commit()
                print '\n\t\t\tThem thanh cong !!!\n'
            else:
                print '\n\tKo the them. Tai khoan nay da nam trong danh sach ban be !!!\n'

    def block(self, username, block):
        if not self.check2(block):
            print '\nTai khoan ko ton tai hoac da bi xoa !!!\n'
        else:
            if not self.checkBlock(username, block):
                conn = self.connect_db()
                conn.execute("insert into Block(username, blocked) values (?,?)", (username, block,))
                conn.commit()
                print '\n\t\tBlock thanh cong !!!\n'
            else:
                print '\n\tKo the Block. Tai khoan nay da bi block truoc do !!!\n'

    def showInfo(self, username):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select * from AccountInfo where username =?", (username,))

            rows = cur.fetchall()
            self.printData(rows)

    def sortFriend(self, username):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select distinct Friend.friend, Friend.TimeDate from Friend, Message "
                        "where Friend.username=? and Friend.username=Message.sender and Friend.friend=Message.receiver "
                        "order by Message.TimeDate desc", (username,))

            rows = cur.fetchall()
            self.printData(rows)

    def sortFriendOfCity(self, username):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select Friend.id, Friend.friend, AccountInfo.address "
                        "from Friend, AccountInfo "
                        "where Friend.username=? and Friend.friend=AccountInfo.username "
                        "order by address asc, friend asc", (username,))

            rows = cur.fetchall()

            self.printData(rows)

    def checkID(self, id):
        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select id, friend from Friend where id=?", (id,))

            rows = cur.fetchall()

            for row in rows:
                if row[0] == int(id):
                    print 'Gui tin nhan den: ' + row[1]
                    return True
                else:
                    return False

    def Ctr_L(self, username):
        self.listFriend(username)
        id = raw_input('Nhap ID de gui tin nhan: ')
        if self.checkID(id):
            content = raw_input('Noi dung tin nhan: ')
            self.sendMessage_Ctr_L(id, content)
        else:
            print '\tNhap sai ID hoac tai khoan ko ton tai !!!\n'

    def sendMessage_Ctr_L(self, id, content):
        username = None
        Friend = None

        conn = self.connect_db()
        with conn:
            cur = conn.cursor()
            cur.execute("select username, friend from Friend where id=?", (id,))

            rows = cur.fetchall()
            for row in rows:
                username = row[0]
                Friend = row[1]

            self.sendMessage(username, Friend, content)

import os

class Menu_Display:

    def menu_Display1(self):
        print "\t\t\t+==============MENU=============+"
        print "\t\t\t|                               |"
        print "\t\t\t|\t1. Dang ky\t\t|"
        print "\t\t\t|\t2. Dang nhap\t\t|"
        print "\t\t\t|\t3. Thoat\t\t|"
        print "\t\t\t|                               |"
        print "\t\t\t+===============================+"

    def menu_Main(self):
        print "\t\t+===================MENU MAIN===================+"
        print "\t\t|                                               |"
        print "\t\t|\t1. Muc tin nhan\t\t\t\t|"
        print "\t\t|\t2. Them ban\t\t\t\t|"
        print "\t\t|\t3. Danh sach ban be\t\t\t|"
        print "\t\t|\t4. Block\t\t\t\t|"
        print "\t\t|\t5. Hien thi thong tin tai khoan\t\t|"
        print "\t\t|\t6. Thong tin ban be\t\t\t|"
        print "\t\t|\t7. Thoat\t\t\t\t|"
        print "\t\t|                                               |"
        print "\t\t+===============================================+"


    def menu_Message(self):
        print "\t\t+=================MENU TIN NHAN=================+"
        print "\t\t|                                               |"
        print "\t\t|\t1. Hien thi cac tin nhan da gui\t\t|"
        print "\t\t|\t2. Hien thi cac tin nhan da nhan\t|"
        print "\t\t|\t3. Gui tin nhan\t\t\t\t|"
        print "\t\t|\t4. Thoat\t\t\t\t|"
        print "\t\t|                                               |"
        print "\t\t+===============================================+"

    def menu_InfoFriend(self):
        print "\t\t========THONG TIN BAN BE========="
        print "\t\t|                               |"
        print "\t\t|\t1. Sua thong tin\t|"
        print "\t\t|\t2. Gui tin nhan\t\t|"
        print "\t\t|\t3. Thoat\t\t|"
        print "\t\t|                               |"
        print "\t\t================================="

    def menu_ListFriend(self):
        print "\t=========================DANH SACH BAN BE========================"
        print "\t|                                                               |"
        print "\t|\t1. Hien thi danh sach ban be\t\t\t\t|"
        print "\t|\t2. Sap xep ban be theo thoi gian gui, nhan tin nhan\t|"
        print "\t|\t3. Sap xep ban be theo thanh pho\t\t\t|"
        print "\t|\t4. Thoat\t\t\t\t\t\t|"
        print "\t|                                                               |"
        print "\t================================================================="

    def notify_Ctr_N_Ctr_B(self):
        print '\n'
        os.system('cls')
        print '\n\nNhan Ctr+N de hien thi danh sach hoac nhan Ctr+B de tro ve MENU TIN NHAN !!!\n\n'

    def notify_ChoiceSendMessage(self):
        print '\n\nCo 2 cach de gui tin nhan:\n1. Nhap vao tai khoan nguoi nhan\n2. Bam truc tiep Ctr+L\n\n'
        print 'Nhap ten nguoi nhan: '

    def notify_Ctr_R(self):
        print '\nNeu muon tra loi tin nhan thi nhan Ctr+R hoac an phim bat ky de thoat !!!\n\n'

    def notifyFailAccount(self):
        print '\t\tTai khoan ko ton tai hoac da bi xoa !!!\n'

    def notifyFailEdit(self):
        print '\t\tChua ket ban. Ko the sua !!!\n'

from Controller import Controller
from Menu_Display import Menu_Display
import os

menu_Display = Menu_Display()
controller = Controller()


class Menu:

    def choice1(self):
        # menu_Display = Menu_Display()
        # controller = Controller()
        while True:
            menu_Display.menu_Display1()
            chosse1 = raw_input('\tNhap vao lua chon: ')
            if chosse1 == '1':
                controller.signUp()
                # break
            elif chosse1 == '2':
                os.system('cls')
                controller.logIn()
                # break
            elif chosse1 == '3':
                print 'Da thoat !!!'
                break
            else:
                raw_input('Chon sai. An Enter de chon lai !!!')

    def choice2(self, username, password):
        while True:
            menu_Display.menu_Main()
            chosse2 = raw_input('\tNhap vao lua chon: ')
            if chosse2 == '1':
                os.system('cls')
                self.choice3(username)
            elif chosse2 == '2':
                controller.addFriend(username)
            elif chosse2 == '3':
                os.system('cls')
                self.choice5(username)
            elif chosse2 == '4':
                controller.block(username)
            elif chosse2 == '5':
                controller.showInfo(username)
            elif chosse2 == '6':
                os.system('cls')
                self.choice4(username)
            elif chosse2 == '7':
                os.system('cls')
                break
            else:
                raw_input('Chon sai. An Enter de chon lai !!!')

    def choice3(self, username):
        while True:
            menu_Display.menu_Message()
            chosse3 = raw_input('\tNhap vao lua chon: ')
            if chosse3 == '1':
                controller.showMessageSent(username)
            elif chosse3 == '2':
                controller.showMessageReceiver(username)
            elif chosse3 == '3':
                controller.sendMessage(username)
            elif chosse3 == '4':
                os.system('cls')
                break
            else:
                raw_input('Chon sai. An Enter de chon lai !!!')

    def choice4(self, username):
        while True:
            menu_Display.menu_InfoFriend()
            chosse4 = raw_input('\tNhap vao lua chon: ')
            if chosse4 == '1':
                controller.editInfoFriend(username)
            elif chosse4 == '2':
                #controller.Ctr_L(username)
                controller.Ctr_L(username)
                controller.sendMessage(username)
            elif chosse4 == '3':
                os.system('cls')
                break
            else:
                raw_input('Chon sai. An Enter de chon lai !!!')

    def choice5(self, username):
        while True:
            menu_Display.menu_ListFriend()
            chosse5 = raw_input('\tNhap vao lua chon: ')
            if chosse5 == '1':
                controller.listFriend(username)
            elif chosse5 == '2':
                controller.sortFriend(username)
            elif chosse5 == '3':
                controller.sortFriendOfCity(username)
            elif chosse5 == '4':
                os.system('cls')
                break
            else:
                raw_input('Chon sai. An Enter de chon lai !!!')

from User import User
import os

class UserView(User):

    def nhap(self):
        User.username = raw_input('Nhap username: ')
        User.password = raw_input('Nhap password: ')

    def dangKy(self):
        User.username = raw_input('Nhap username: ')
        User.password = raw_input('Nhap password: ')
        User.fullname = raw_input('Nhap day du ho va ten: ')
        User.birthday = raw_input('Nhap ngay, thang, nam sinh(dd/mm/yyyy): ')
        User.sex = raw_input('Nhap gioi tinh: ')
        User.address = raw_input('Nhap dia chi: ')

    def nhanTin(self):
        User.receiver = raw_input()
        User.content = raw_input('Noi dung tin nhan: ')

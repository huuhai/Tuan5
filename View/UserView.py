from User import User


class UserView(User):

    def logIn(self):
        User.username = raw_input('Nhap username: ')
        User.password = raw_input('Nhap password: ')

    def inputInfo(self):
        User.fullname = raw_input('Nhap day du ho va ten: ')
        User.birthday = raw_input('Nhap ngay, thang, nam sinh(dd/mm/yyyy): ')
        User.sex = raw_input('Nhap gioi tinh: ')
        User.address = raw_input('Nhap dia chi: ')

    def signUp(self):
        self.logIn()
        self.inputInfo()

    def nhanTin(self):
        User.receiver = raw_input()
        User.content = raw_input('Noi dung tin nhan: ')

    def inputNameFriend(self):
        User.editInfoFriend = raw_input('Nhap ten nguoi ban muon sua thong tin: ')

    def inputAddFriend(self):
        User.Friend = raw_input('Nhap ten ban be muon them: ')

    def inputBlockFriend(self):
        User.block = raw_input('Nhap ten ban be muon block: ')

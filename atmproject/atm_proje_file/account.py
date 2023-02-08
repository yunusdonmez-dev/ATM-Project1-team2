from PyQt5.QtWidgets import *
from Ui_account import Ui_accountScreen
from Ui_balance import Ui_balanceScreen 
from Ui_insert import Ui_insertScreen
from Ui_withdraw import Ui_withdrawScreen
from Ui_statament import Ui_statementScreen
from Ui_login import Ui_loginScreen
from ui_loginAdmin import Ui_loginAdmin   # for admin
from ui_accountAdmin import Ui_accountAdmin # for admin


import json
import os


class LoginPage(QMainWindow):

    
    def __init__(self):
        super().__init__()
        
        self.loginform = Ui_loginScreen()       
        self.loginform.setupUi(self)
        self.openaccountpage = AccountPage()
        self.loginform.enter_button_2.clicked.connect(self.returnLoginAdmin)
        self.loginform.enter_button.clicked.connect(self.enter)
       


    def returnLoginAdmin(self):
        self.loginReturnForm= LoginAdminPage()
        self.hide()
        self.loginReturnForm.show()


    def enter(self):
        global user,password
        self.id = self.loginform.idnum_edit.text()
        self.password = self.loginform.password_edit.text()
        user = self.id
        password = self.password
        fileloc = os.getcwd()
        
        with open(f"{fileloc}\\atmproject\\atm_proje_file\\data2.json") as f:
            data = json.load(f)
            users = data["customers"]
            for i in users:
                if i["id"] == self.id:
                    if i["password"] == self.password:
                        self.hide()
                        self.openaccountpage.show()
                            
class AccountPage(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.account_page_form = Ui_accountScreen()
        self.account_page_form.setupUi(self)
        self.account_page_form.check_button.clicked.connect(self.balance)
        self.account_page_form.insert_button.clicked.connect(self.insert)
        self.account_page_form.withdraw_button.clicked.connect(self.withdraw)
        self.account_page_form.statement_button.clicked.connect(self.statement)

    
         
                    
    def balance(self):
        self.open_balance_page = BalancePage()
        self.hide()
        self.open_balance_page.show()

    def insert(self):
        self.open_insert_page = InsertPage()
        self.hide()
        self.open_insert_page.show()
            
        print(user)



    def withdraw(self):
        self.open_withdraw_page = WithdrawPage()
        self.close()
        self.open_withdraw_page.show()
    def statement(self):
        self.open_statement_page = StatementPage()
        self.close()
        self.open_statement_page.show()
    


class BalancePage(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.checkbalance = Ui_balanceScreen()
        self.checkbalance.setupUi(self)
        self.checkbalance.return1_button.clicked.connect(self.donus)

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()
class InsertPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.insert_money = Ui_insertScreen()
        
        self.insert_money.setupUi(self)
        self.insert_money.return2_button.clicked.connect(self.donus)
        fileloc = os.getcwd()
        with open(f"{fileloc}\\atmproject\\atm_proje_file\\data2.json") as f:
            data = json.load(f)
            users = data["customers"]
            for i in users:
                if i["id"] == user:
                    self.insert_money.balance2_label.setText(i["balance"])
        # with open(f"{fileloc}\\atmproject\\atm_proje_file\\data2.json",'a') as f:
        #     data = json.dump(f)
        #     users = data["customers"]
        #     for i in users:
        #         if i["id"] == user:
        #             in_money = self.insert_money.insert_edit.text()
                    
        #             i["balance"] = "balance degisti"

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()
    
class WithdrawPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.withdraw_money = Ui_withdrawScreen()
        self.withdraw_money.setupUi(self)
        self.withdraw_money.return3_button.clicked.connect(self.donus)
    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()     
class StatementPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statement_user = Ui_statementScreen()
        self.statement_user.setupUi(self)
        self.statement_user.return4_button.clicked.connect(self.donus)
    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()
        


# Admin Screen

class LoginAdminPage(QWidget):  # klas olusturdugumuzda bunu QT designer daki (QWidget) sinifin alt sinifi yapiyoruz.
    def __init__(self) -> None:  
        super().__init__()
        self.loginForm= Ui_loginAdmin()      #bu ve alttaki kod ile nesne yaratip sonra ana modulunu(self ile) cagiriyoruz.
        self.loginForm.setupUi(self)
        self.loginForm.labelErrorMessage.hide()
        self.loginForm.pushButtonLogin.clicked.connect(self.AccountAdminOpen) # login tiklanirsa AccountOpen modulunu calistiracak.
        
     
   
    def AccountAdminOpen(self):

        user_name = self.loginForm.lineEditUser.text()
        user_pass = self.loginForm.lineEditPassword.text()  
        
        
        if user_name =="Yakup" and user_pass =="1234":   # bu gecici olarak yazilan bir kod. daha sonra data dan alacagiz.
            self.accountForm= AccounAdminPage()
            self.close()   
            self.accountForm.show()   # simdi login de sartlari soracak eger dogruysa diger arayuzu burada gosterecektir.
            
        else :
            self.loginForm.labelErrorMessage.setText(F" {user_name} User Name or  User Password is incorrect! Try Again ")
            self.loginForm.labelErrorMessage.show()
                
        
    
class AccounAdminPage(QWidget):  
    def __init__(self) -> None:
        super().__init__()
        
        # ornek ve ana modul calistiriliyor
        self.accounderForm= Ui_accountAdmin()
        self.accounderForm.setupUi(self)
        self.accounderForm.pushButtonReturn.clicked.connect(self.returnLoginAdmin)


    def returnLoginAdmin(self):
        self.loginReturnForm= LoginAdminPage()
        self.hide()
        self.loginReturnForm.show()
from PyQt5.QtWidgets import *
from Ui_account import Ui_accountScreen
from Ui_balance import Ui_balanceScreen 
from Ui_insert import Ui_insertScreen
from Ui_withdraw import Ui_withdrawScreen
from Ui_statament import Ui_statementScreen
from Ui_login import Ui_loginScreen
import json
import os


class LoginPage(QMainWindow):

    
    def __init__(self):
        super().__init__()
        
        self.loginform = Ui_loginScreen()       
        self.loginform.setupUi(self)
        self.openaccountpage = AccountPage()
        self.loginform.enter_button.clicked.connect(self.enter)
       

    def enter(self):
        global user,password
        self.id = self.loginform.idnum_edit.text()
        self.password = self.loginform.password_edit.text()
        user = self.id
        password = self.password
        
        with open(r"C:\Users\yunus\OneDrive\Desktop\atmproject\database\data2.json") as f:
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

        with open(r"C:\Users\yunus\OneDrive\Desktop\atmproject\database\data2.json") as f:
            data = json.load(f)
            users = data["customers"]
            for i in users:
                if i["id"] == user:
                    self.insert_money.balance2_label.setText(i["balance"])
        with open(r"C:\Users\yunus\OneDrive\Desktop\atmproject\database\data2.json",'a') as f:
            data = json.load(f)
            users = data["customers"]
            for i in users:
                if i["id"] == user:
                    in_money = self.insert_money.insert_edit.text()
                    
                    i["balance"] = "balance degisti"

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
        
            
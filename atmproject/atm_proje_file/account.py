from PyQt5.QtWidgets import *
from Ui_account import Ui_accountScreen
from Ui_balance import Ui_balanceScreen 
from Ui_insert import Ui_insertScreen
from Ui_withdraw import Ui_withdrawScreen
from Ui_statament import Ui_statementScreen
from Ui_login import Ui_loginScreen
from ui_loginAdmin import Ui_loginAdmin   # for admin
from ui_accountAdmin import Ui_accountAdmin # for admin
import datetime

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
            for self.i in users:
                if str(self.i["id"]) == self.id:
                    if self.i["password"] == self.password:
                        self.hide()
                        self.openaccountpage.show()
                        self.login_log()
                        
                        break
    def login_log(self):
        with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json") as f:
            self.data = json.load(f)
            # self.users = self.data["customers"]
            self.data["customers"][self.i["id"]-1]["login_log"] += f"Customer {user} logged in at {datetime.datetime.now()}-" 
                 
        with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json",'w') as f:
            json.dump(self.data , f, indent=4)                    
        
                          
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
        with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json") as f:
            self.data = json.load(f)
            self.users = self.data["customers"]
            for self.i in self.users:
                 if str(self.i["id"]) == user:
                    self.checkbalance.balance_label.setNum(self.i["balance"])

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()
class InsertPage(LoginPage,QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.insert_money = Ui_insertScreen()
        
        self.insert_money.setupUi(self)
        self.insert_money.return2_button.clicked.connect(self.donus)
        
        
    
        with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json") as f:
            self.data = json.load(f)
            self.users = self.data["customers"]
            for self.i in self.users:
                print(self.i["name"])
                if str(self.i["id"]) == user:
                    self.insert_money.balance2_label.setNum(self.i["balance"])
                    self.insert_money.enter2_button.clicked.connect(self.add_money)
                    break 
        
        

    def add_money(self):
        with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json") as f:
            self.data = json.load(f)
            self.users = self.data["customers"]
            self.data["customers"][self.i["id"]-1]["balance"] += int(self.insert_money.insert_edit.text())
            self.insert_money.balance2_label.setNum(self.data["customers"][self.i["id"]-1]["balance"])
            self.data["customers"][self.i["id"]-1]["money_activities"] += f"Customer {user} inserted {int(self.insert_money.insert_edit.text())} $ at {datetime.datetime.now()}-"     
        
        with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json",'w') as f:
            json.dump(self.data , f, indent=4)

        

        

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()
    
class WithdrawPage(LoginPage,QMainWindow):
    from account import LoginPage

    def __init__(self):
        super().__init__()
        self.withdraw_money = Ui_withdrawScreen()
        self.withdraw_money.setupUi(self)
        self.withdraw_money.return3_button.clicked.connect(self.donus)

        with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json") as f:
            self.data = json.load(f)
            self.users = self.data["customers"]
            for self.i in self.users:
                 if str(self.i["id"]) == user:
                    self.withdraw_money.balance3_label.setNum(self.i["balance"])
                    # self.withdraw_money.balance3_label.setNum(self.data["customers"][self.i["id"]-1]["balance"])
                    self.withdraw_money.enter_button.clicked.connect(self.take_money)
                    break
    def take_money(self):
        
        if self.i["balance"]  >= int(self.withdraw_money.withdraw_edit.text()) :
            self.withdraw_money.messsage2_button.setText("")
            with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json") as f:
                self.data = json.load(f)
                self.users = self.data["customers"]
                self.data["customers"][self.i["id"]-1]["balance"] -= int(self.withdraw_money.withdraw_edit.text())
                self.withdraw_money.balance3_label.setNum(self.data["customers"][self.i["id"]-1]["balance"]) 

                self.data["customers"][self.i["id"]-1]["money_activities"] += f"Customer {user} withrawed {int(self.withdraw_money.withdraw_edit.text())} $ at {datetime.datetime.now()}-"  
                with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json",'w') as f:
                    json.dump(self.data , f, indent=4)
                
                
                
                    
        else :
            self.withdraw_money.messsage2_button.setText("Insufficient Fund")
            print("insufficient fund")
            
            
                     

                    


    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()     
class StatementPage(LoginPage,QMainWindow):
    def __init__(self):
        super().__init__()
        self.statement_user = Ui_statementScreen()
        self.statement_user.setupUi(self)
        self.statement_user.return4_button.clicked.connect(self.donus)
        with open(f"{os.getcwd()}\\atmproject\\atm_proje_file\\data2.json") as f:
            self.data = json.load(f)
            self.statement_user.logins_label.setText(self.data["customers"][int(user)-1]["login_log"])
            self.statement_user.date_label.setText(self.data["customers"][int(user)-1]["register_log"])
            self.statement_user.aktivites_label.setText(self.data["customers"][int(user)-1]["money_activities"])
            self.statement_user.check_label.setText(str(self.data["customers"][int(user)-1]["balance"])+" $")
            

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
        
        fileloc = os.getcwd()
        with open(f"{fileloc}\\atmproject\\atm_proje_file\\data.json") as f:
            data = json.load(f)
            users = data["bank"]
            
            for i in users:
                if i["name"] == user_name:
                    if i["password"] == user_pass:
                        self.hide()
                        # self.openaccountpage.show()   # bu gecici olarak yazilan bir kod. daha sonra data dan alacagiz.
                        self.accountForm= AccounAdminPage()
                        self.close()   
                        self.accountForm.show()   # simdi login de sartlari soracak eger dogruysa diger arayuzu burada gosterecektir.
            
                    else :
                        self.loginForm.labelErrorMessage.setText(F" {user_name} User Name or  User Password is incorrect! Try Again ")
                        self.loginForm.labelErrorMessage.show()
                
        
    
class AccounAdminPage(QWidget):  
    fileloc = os.getcwd()
    print(fileloc)
    def __init__(self) -> None:
        super().__init__()
        
        # ornek ve ana modul calistiriliyor
        self.accounderForm= Ui_accountAdmin()
        self.accounderForm.setupUi(self)
        self.accounderForm.pushButtonReturn.clicked.connect(self.returnLoginAdmin)
        self.accounderForm.pushButtonSuffix.clicked.connect(self.write_json)
        
    def write_json(self):

        fileloc = os.getcwd()
        

        with open(f"{fileloc}\\atmproject\\atm_proje_file\\data2.json") as json_file:
            data = json.load(json_file)
            temp = data["customers"]
            y = {
            "id": len(temp)+1,
            "name": self.accounderForm.lineEditName.text(),
            "surname":self.accounderForm.lineEditSurname.text(),
            "balance":int(self.accounderForm.lineEditBalans.text()),
            "e-mail" : self.accounderForm.lineEditEmail.text(),
            "tax-number" :int(self.accounderForm.lineEditTax.text()),
            "password" : self.accounderForm.lineEditPassword.text() ,
            "login_log" : "",
            "money_activities" : "",
            "register_log" : f"Customer {len(temp)+1} registered at {datetime.datetime.now()}"           
            }
            temp.append(y)

        with open(f"{fileloc}\\atmproject\\atm_proje_file\\data2.json",'w') as f:
            json.dump(data , f, indent=4)
                



    def returnLoginAdmin(self):
        self.loginReturnForm= LoginAdminPage()
        self.hide()
        self.loginReturnForm.show()
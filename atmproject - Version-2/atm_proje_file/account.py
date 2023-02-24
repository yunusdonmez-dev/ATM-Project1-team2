'''
This is an Atm app that can hold users information and allows them make money activities. 

'''





from PyQt5.QtWidgets import *
from Ui_account import Ui_accountScreen
from Ui_balance import Ui_balanceScreen 
from Ui_insert import Ui_insertScreen
from Ui_withdraw import Ui_withdrawScreen
from Ui_Change_customer_datails import Ui_MainWindow2
from Ui_transfer import Ui_transfer
from Ui_admin_choice import Ui_MainWindow1
from Ui_See_bank_details import Ui_MainWindow

from Ui_login import Ui_loginScreen
from ui_loginAdmin import Ui_loginAdmin   # for admin
from ui_accountAdmin import Ui_accountAdmin # for admin
from Ui_statement import Ui_statementScreen
import datetime
import time

import json
import os

__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

class LoginPage(QMainWindow):
    '''
    login page of the app where user can enter 
    '''
    
    
    def __init__(self):
        super().__init__()
        
        self.loginform = Ui_loginScreen()       
        self.loginform.setupUi(self)
        self.openaccountpage = AccountPage()
        self.loginform.enter_button_2.clicked.connect(self.returnLoginAdmin)
        self.loginform.enter_button.clicked.connect(self.enter)
        self.loginform.id_label2.hide()
    

    def returnLoginAdmin(self):
        self.loginReturnForm= LoginAdminPage()
        self.hide()
        self.loginReturnForm.show()


    def enter(self):
        global user,password
        try :
            self.id = int(self.loginform.idnum_edit.text())-100000
            self.password = self.loginform.password_edit.text()
        
            user = str(self.id)
            password = self.password
            fileloc = os.getcwd()
            
            with open(os.path.join(__location__, 'data2.json')) as f:
                self.data = json.load(f)
                self.users = self.data["customers"]
            
                if self.users[int(user)-1]["id"] == int(user)+100000:
                    if str(self.users[int(user)-1]["password"]) == str(password):
                        self.hide()
                        self.openaccountpage.show()
                        self.login_log()
        except :
            self.loginform.id_label2.show()
            self.loginform.id_label2.setText("Wrong name or password !!!")
           
                              
                        
    def login_log(self):
        
        with open(os.path.join(__location__, 'data2.json')) as f:
            self.data = json.load(f)
            # self.users = self.data["customers"]
            self.data["customers"][int(user)-1]["login_log"].append(f"--Logged in at {datetime.datetime.now()}#")
                 
        with open(os.path.join(__location__, 'data2.json','w')) as f:
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
        self.account_page_form.return_button.clicked.connect(self.go_login)
        self.account_page_form.btn_edit_info.clicked.connect(self.edit_info)
        self.account_page_form.insert_button_2.clicked.connect(self.transfer)

    def transfer(self):
        self.transferform = Transferpage()
        self.close()
        self.transferform.show()
        
    def edit_info(self):
        self.editform = Editpage()
        self.close()
        self.editform.show()
    
    def go_login(self):
        self.loginform = LoginPage()
        self.close()
        self.loginform.show()

    
         
                    
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

class Transferpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.transfer_money = Ui_transfer()
        self.transfer_money.setupUi(self)
        self.transfer_money.return3_button.clicked.connect(self.donus)
        self.transfer_money.lbl_error_credit.hide()
        self.transfer_money.lbl_error_customerid.hide()
        self.transfer_money.lbl_error_limit.hide()
        self.transfer_money.lbl_error_valid_amount.hide()
        self.transfer_money.lbl_succesfull.hide()

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()

    
class Editpage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editinfo = Ui_MainWindow()
        self.editinfo.setupUi(self)
        self.editinfo.return2_button.clicked.connect(self.donus)

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()

class BalancePage(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.checkbalance = Ui_balanceScreen()
        self.checkbalance.setupUi(self)
        self.checkbalance.return1_button.clicked.connect(self.donus)
        with open(os.path.join(__location__, 'data2.json')) as f:
            self.data = json.load(f)
            self.users = self.data["customers"]
            self.checkbalance.balance_label.setText(str(self.users[int(user)-1]["balance"]) + " €")

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
        self.insert_money.balance3_label.hide()
        
    
        with open(os.path.join(__location__, 'data2.json')) as f:
            self.data = json.load(f)
            self.users = self.data["customers"]
            
                
            self.insert_money.balance2_label.setText(str(self.users[int(user)-1]["balance"]) + " €")
            self.insert_money.enter2_button.clicked.connect(self.add_money)
            
        

    def add_money(self):

        try :
            assert (int(self.insert_money.insert_edit.text())/1).is_integer()
            with open(os.path.join(__location__, 'data2.json')) as f:
                self.data = json.load(f)
                self.users = self.data["customers"]
                self.data["customers"][int(user)-1]["balance"] += int(self.insert_money.insert_edit.text())
                self.insert_money.balance2_label.setText(str(self.users[int(user)-1]["balance"]) + " €")
                self.data["customers"][int(user)-1]["money_activities"].append(f"--Inserted {int(self.insert_money.insert_edit.text())} € at {datetime.datetime.now()}#")     
        
        
            with open(os.path.join(__location__, 'data2.json'),'w') as f:
                json.dump(self.data , f, indent=4)
            self.insert_money.balance3_label.show()
            self.insert_money.balance3_label.setText("Inserted succesfully ")
        except :
        
            self.insert_money.balance3_label.show()
            self.insert_money.balance3_label.setText("Please enter an number !!!")

        

    def donus(self):
        self.openaccountpage = AccountPage()
        self.close()
        self.openaccountpage.show()
    
class WithdrawPage(LoginPage,QMainWindow):
    

    def __init__(self):
        super().__init__()
        self.withdraw_money = Ui_withdrawScreen()
        self.withdraw_money.setupUi(self)
        self.withdraw_money.return3_button.clicked.connect(self.donus)

        with open(os.path.join(__location__, 'data2.json')) as f:

            self.data = json.load(f)
            self.users = self.data["customers"]
            self.withdraw_money.balance3_label.setText(str(self.users[int(user)-1]["balance"]) + " €")
            self.withdraw_money.enter_button.clicked.connect(self.take_money)
                    
    def take_money(self):
        
        try :
            assert (int(self.withdraw_money.withdraw_edit.text())/1).is_integer()

            if self.data["customers"][int(user)-1]["balance"]  >= int(self.withdraw_money.withdraw_edit.text()) :
                self.withdraw_money.messsage2_button.setText("")
                with open(os.path.join(__location__, 'data2.json')) as f:
                    self.data = json.load(f)
                    self.users = self.data["customers"]
                    self.data["customers"][int(user)-1]["balance"] -= int(self.withdraw_money.withdraw_edit.text())
                    self.withdraw_money.balance3_label.setText(str(self.users[int(user)-1]["balance"]) + " €") 

                    self.data["customers"][int(user)-1]["money_activities"].append(f"--Withrawed {int(self.withdraw_money.withdraw_edit.text())} $ at {datetime.datetime.now()}#") 
                    with open(os.path.join(__location__, 'data2.json'),'w') as f:
                        json.dump(self.data , f, indent=4)
                self.withdraw_money.messsage2_button.setText("Succesfully withdrawed")
                
                
                    
            else :
                self.withdraw_money.messsage2_button.setText("Insufficient Fund !!!")
                
        except :
            self.withdraw_money.messsage2_button.setText("Invalid amount !!!")
        
                     

                    


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
        self.statement_user.textBrowser.hide()
        self.statement_user.textBrowser_2.hide()
        
        # with open(os.path.join(__location__, 'data2.json')) as f:
        #     self.data = json.load(f)
        #     a = ''
        #     b = ''
        #     for i in self.data["customers"][int(user)-1]["login_log"]:
        #         a += f"{i} \n"
        #     self.statement_user.logins_label.setText(a)
        #     self.statement_user.date_label.setText(self.data["customers"][int(user)-1]["register_log"])
        #     for i in self.data["customers"][int(user)-1]["money_activities"]:
        #         b += f"{i} \n"
        #     self.statement_user.aktivites_label.setText(b)
        #     # self.statement_user.check_label.setText(str(self.data["customers"][int(user)-1]["balance"])+" $")
            

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
        self.loginForm.pushButtonLogin.clicked.connect(self.choice_menu)
        # self.loginForm.pushButtonLogin.clicked.connect(self.AccountAdminOpen) # login tiklanirsa AccountOpen modulunu calistiracak.
        self.loginForm.pushButtonLogin2.clicked.connect(self.go_customer_login)

    def choice_menu(self):
        self.choiceform = Choicepage()
        self.close()
        self.choiceform.show()


    def go_customer_login(self):
        self.loginform = LoginPage()
        self.close()
        self.loginform.show()

        
     
   
    # def AccountAdminOpen(self):

    #     user_name = self.loginForm.lineEditUser.text()
    #     user_pass = self.loginForm.lineEditPassword.text()  
        
        # fileloc = os.getcwd()
        # with open(f"{fileloc}\\atmproject\\atm_proje_file\\data.json") as f:
        #     data = json.load(f)
        #     users = data["bank"]
            
        #     for i in users:
        #         if i["name"] == user_name:
        #             if i["password"] == user_pass:
        #                 self.hide()
        #                 # self.openaccountpage.show()   # bu gecici olarak yazilan bir kod. daha sonra data dan alacagiz.
        #                 self.accountForm= AccounAdminPage()
        #                 self.close()   
        #                 self.accountForm.show()   # simdi login de sartlari soracak eger dogruysa diger arayuzu burada gosterecektir.
            
        #         else :
        #             self.loginForm.labelErrorMessage.setText(F" {user_name} User Name or  User Password is incorrect! Try Again ")
        #             self.loginForm.labelErrorMessage.show()
                




class Choicepage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.choiceform = Ui_MainWindow1()
        self.choiceform.setupUi(self)
        self.choiceform.btn_activities.clicked.connect(self.activities)
        self.choiceform.btn_change.clicked.connect(self.change)
        self.choiceform.btn_register.clicked.connect(self.register)
        self.choiceform.return2_button.clicked.connect(self.return_login)


    def return_login(self):
        self.loginform = LoginAdminPage()
        self.close()
        self.loginform.show()

    def register(self):
        self.accountForm= AccounAdminPage()
        self.close()   
        self.accountForm.show()

    def change(self):
        self.changepage = Changepage()
        self.close()
        self.changepage.show()

    
    def activities(self):
        self.activitypage = Activitypage()
        self.close()
        self.activitypage.show()


from Ui_Change_customer_datails import Ui_MainWindow2


class Changepage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.changeform = Ui_MainWindow2()
        self.changeform.setupUi(self)
        self.changeform.return2_button.clicked.connect(self.return_admin_choice)
    
    def return_admin_choice(self):
        self.choiceform = Choicepage()
        self.close()
        self.choiceform.show()
    



class Activitypage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.activityform = Ui_MainWindow()
        self.activityform.setupUi(self)
        self.activityform.return2_button.clicked.connect(self.returnLoginAdmin)

    def returnLoginAdmin(self):
        self.choiceform = Choicepage()
        self.close()
        self.choiceform.show()
    

class AccounAdminPage(QWidget):  
    
    def __init__(self) -> None:
        super().__init__()
        
        # ornek ve ana modul calistiriliyor
        self.accounderForm= Ui_accountAdmin()
        self.accounderForm.setupUi(self)
        self.accounderForm.pushButtonReturn.clicked.connect(self.return_admin_choice)
        self.accounderForm.pushButtonSuffix.clicked.connect(self.write_json)
        # self.accounderForm.pushButtonSuffix.clicked.connect(self.accoundCread)
        self.accounderForm.label.hide()


    def accoundCread(self):
        with open(os.path.join(__location__, 'data2.json')) as f:
            data = json.load(f)
            heades = data["customers"]
            row_index = 0
            for i in heades:
            #     for k in i :  # k benim sozlukteki key dir. i ise listedeki sozluktur.
                self.accounderForm.tableWidget.setItem(0,0,QTableWidgetItem(str(len(heades)+1)))  # i[k] bana sozlukteki key degerini veriyor.
                self.accounderForm.tableWidget.setItem(0,1,QTableWidgetItem(i["name"]))  # i[k] bana sozlukteki key degerini veriyor.
                self.accounderForm.tableWidget.setItem(0,2,QTableWidgetItem(i["surname"]))  # i[k] bana sozlukteki key degerini veriyor.
                self.accounderForm.tableWidget.setItem(0,5,QTableWidgetItem(str(i["balance"])))  # i[k] bana sozlukteki key degerini veriyor.
                self.accounderForm.tableWidget.setItem(0,3,QTableWidgetItem(i["e-mail"]))  # i[k] bana sozlukteki key degerini veriyor.
                self.accounderForm.tableWidget.setItem(0,4,QTableWidgetItem(str(i["tax-number"])))  # i[k] bana sozlukteki key degerini veriyor.
                self.accounderForm.tableWidget.setItem(0,6,QTableWidgetItem(i["password"]))  # i[k] bana sozlukteki key degerini veriyor.
                




    def write_json(self):
        
        with open(os.path.join(__location__, 'data2.json')) as json_file:
            data = json.load(json_file)
            temp = data["customers"]
            y = {
            "id": len(temp)+100001,
            "name": self.accounderForm.lineEditName.text(),
            "surname":self.accounderForm.lineEditSurname.text(),
            "balance":int(self.accounderForm.lineEditBalans.text()),
            "e-mail" : self.accounderForm.lineEditEmail.text(),
            "tax-number" :int(self.accounderForm.lineEditTax.text()),
            "password" : self.accounderForm.lineEditPassword.text() ,
            "login_log" : [],
            "money_activities" : [],
            "register_log" : f"Customer {len(temp)+100001} registered at {datetime.datetime.now()}"           
            }
            temp.append(y)
        try:
            assert len(self.accounderForm.lineEditPassword.text())>=6
            with open(os.path.join(__location__, 'data2.json'),'w') as f:
                json.dump(data , f, indent=4)
            
            self.accounderForm.label.setText("Account is created succesfully !")
            self.accounderForm.label.show()
            self.accoundCread()

            
        except :
            print("password must be at least 6 digits")
            self.accounderForm.label.show()


    def return_admin_choice(self):
        self.choiceform = Choicepage()
        self.close()
        self.choiceform.show()
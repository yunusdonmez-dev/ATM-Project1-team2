kullanicilar_sifreler = [['ali','12345',1000],['ahmet','qwerty',500],['zeynep','54321',5000]]


# f = open(r"C:\Users\yunus\OneDrive\Desktop\teamproject\database\example.txt",'w',encoding='utf-8')
# f.write("TeamProject\n")
# f.close()
class Newcustomer():
    totalCustomer = 0
    def __init__(self,name,email):
        self.name = name
        self.Id = Newcustomer.totalCustomer +1
        self.email = email
        self.password = input("Enter your password :\n")

    def save(self):
        with open(r"C:\Users\yunus\OneDrive\Desktop\teamproject\database\database.txt","a",encoding="utf-8") as f :
            f.write('\n'+self.name+','+ str(self.Id) +','+ self.email +','+ self.password)
custemer1 = Newcustomer("ali","yunusdonmeznl@gmail.com")
Newcustomer.save(custemer1)
custemer2 = Newcustomer("Furkan","furkidonmeznl@gmail.com")
Newcustomer.save(custemer2)

class Login(Newcustomer):
    def __init__(self, name, email):
       super().__init__(name, email)
       pass


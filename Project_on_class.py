class Womenclothing():

    def welcome(self,n,price):
        print("***********WELCOME TO WOMEN CLOTHING SHOPPING********")
        self.n = n
        self.price = price
       # n = int(input("Enter below barnds :1) for Indian Brand and 2) for Western Brand"))
       # price = int(input("Enter BELOW Price range: \n"
        #                  "1)700-1000 2)500-1100 3)1000 4)1000-1500 5)1500-2000"))

class Indian_Brands(Womenclothing):

    def W_brand(self):
     print("YOU ARE CHECKING COLLECTIONS IN W-BRAND")

    def Biba_brand(self):
     print("YOU ARE CHECKING COLLECTIONS IN BIBA-BRAND")

    def Aurelia_brand(self):
     print("YOU ARE CHECKING COLLECTIONS IN AURELIA-BRAND")

    def Globaldesi_brand(self):
     print("YOU ARE CHECKING COLLECTIONS GLOBALDESI-BRAND")

    def FabIndia_brand(self):
     print("YOU ARE CHECKING COLLECTIONS IN FABINDIA-BRAND")

class Western_Brands(Womenclothing):

    def Allensolly_brand(self):
     print("YOU ARE CHECKING COLLECTIONS IN ALLENSOLY-BRAND")

    def And_brand(self):
     print("YOU ARE CHECKING COLLECTIONS IN AND-BRAND")

    def HM_brand(self):
     print("YOU ARE CHECKING COLLECTIONS IN H&M-BRAND")

    def Globus_brand(self):
     print("YOU ARE CHECKING COLLECTIONS IN GLOBUS-BRAND")

    def Pega_brand(self):
     print("YOU ARE CHECKING COLLECTIONS IN PEGA-BRAND")

w = Womenclothing()
n = int(input("Enter below barnds :1) for Indian Brand and 2) for Western Brand"))
price = int(input("Enter BELOW Price range: \n"
                          "1)700-1000 2)500-1100 3)1000 4)1000-1500 5)1500-2000"))

w.welcome(n,price)
ind = Indian_Brands()

if n==1 and price == 1:
    ind.W_brand()
elif n == 1 and price == 2:
    ind.Aurelia_brand()
elif n == 1 and price == 3:
    ind.Biba_brand()
elif n == 1 and price == 4:
        ind.FabIndia_brand()
elif n == 1 and price == 5:
        ind.Globaldesi_brand()
elif n == 2 and price == 1:
        we = Western_Brands()
        we.Allensolly_brand()
elif n == 2 and price == 2:
        we = Western_Brands()
        we.Globus_brand()
elif n == 2 and price == 3:
        we = Western_Brands()
        we.Pega_brand()
elif n == 2 and price == 4:
        we = Western_Brands()
        we.And_brand()
elif n == 2 and price == 5:
        we = Western_Brands()
        we.HM_brand()
else:
        print("Enter price for below range only")

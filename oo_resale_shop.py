from computer import Computer

# "typing" is a library
# Computer is a local library

class ResaleShop:
    # What attributes will it need?
    
    # Notes:
    # First we are going to define what the attributes are and tell what type they are

    inventory : list 
    # Notes:
    # list is empty, but is set to empty in the constructor


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory=[]
    
    # We no longer need an itemID becuase each computer has its own attributes that are inheirent to it. We 
    # no longer need a number to identify it because we could say "the red one", or "the blue one" and not "1 " or "2" 
    # because the Computer now has identifiers for it that make the itemID unnecessary

#"new" instead of "buy" beacuse I was confusing it with "sell"
    def buy(self, c: Computer):
        self.inventory.append (c) 
        # Notes: 
        # pass in self and c because those are what we are going to use. put in the Computer 
        # class as well to specify that will be used. c is just a placeholder vairable that
        # will get overwritten with each new computer when it is called in main
      
        print("The computer with description ", c.description , "is inventoried!")
        # c now has all of the attributes of a Computer class and can be called as such
        

    def update_price(self, c: Computer, new_price: int):

        if c in self.inventory:
            c.price = new_price
            print("Price has been updated to ", c.price)
        else:
            print("Item", c, "not found. Cannot update price.")

         # psuedocode: we need the function to go into the inventory, find a specific item, if it is there
         # we can locate its price, and change that price
       
    def sell(self, c: Computer):
        if c in self.inventory:
            self.inventory.remove(c)
            print("Computer has been sold for ", c.price)
        else:
            print("Computer is not in the inventory")

#  psuedocode refurbish: we need to know how old the computer is, give it an updated os,
#  assign it a price based on this, and then add it to the inventory
    def refurbish(self, c : Computer, new_os: str):
        if c in self.inventory:
            if c.year_made < 2000:
                c.price = 0
            elif c.year_made < 2012:
                c.price = 250
            elif c.year_made < 2018:
                c.price = 550
            else:
                c.price = 1000
            
            if new_os is not None:
                c.operating_system=new_os
            print(c)
        else: print("computer not found")
    



def main():
    shop = ResaleShop()
    c = Computer("Mac Pro(Late 2013)","3.5 GHc 6-core Intel Xeon 5",1024, 64,"Mac OS Big Sur",2013, 1500)
    shop.buy(c)

    shop.sell(c)

    shop.refurbish(c, "Windows 10")

   
main()
    

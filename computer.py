class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
   
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity= hard_drive_capacity
        self.memory= memory
        self.operating_system= operating_system
        self.year_made= year_made
        self.price= price
    
    # Notes:
    # __str__ comes first because it is called as a function later and will 
    # print out all of the information for the computer that it is called for
    def __str__(self)-> str:
        return "Description: " + self.description + "\n" + "Processor: "+ self.processor_type + "\n" +"Hard Drive Capacity: "+ str(self.hard_drive_capacity) + "\n" +"Memory: "+ str(self.memory) + "\n" +"Operating System: "+ self.operating_system + "\n" +"Year: "+ str(self.year_made) + "\n" + "Price: "+ str(self.price) + "\n" 

    # What methods will you need?

def main():

    #add one computer with attributes in order of the ones in the class

    my_computer = Computer("Mac Pro(Late 2013)",
        "3.5 GHc 6-core Intel Xeon 5",
        1024, 64,
        "Mac OS Big Sur",
        2013, 1500)
    
    #test the class by adding a separate computer

    computer_2 = Computer("HP Envy 360",
        "Intel Core i5",
        1024, 64,
        "Windows 10",
        2021, 1000)
    
    #Call the function __str__ for both computers to have 
    #them print all of the attributes at once

    my_computer.__str__()
    computer_2.__str__()

main()

# NOTES: 
# OTHER METHODS FOR TESTING THE CLASS : NOT AS EFFICIENT

# A method to print things out one by one, not very efficient

#     print("desc:", my_computer.description)
#     print("Processor", my_computer.processor_type)
#     print("Hard Drive Capacity", my_computer.hard_drive_capacity)
#     print("memory", my_computer.memory)
#     #continue with this pattern to test the function
#     #another way is to make each value a variable

#A process to define each 

# def main():
#     desc= "Mac Pro(Late 2013)",
#     processor= "3.5 GHc 6-core Intel Xeon 5",
#     hdc= 1024, 
#     memory= 64,
#     os= "Mac OS Big Sur",
#     year= 2013, 
#     price= 1500

#     my_computer=Computer(desc, processor, hdc, memory, os, year, price)
#this is clunky, we want to be able to have  function that does all this at once


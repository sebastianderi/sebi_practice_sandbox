# overview:
    #1. going to define a class (or two), maybe some methods
    #2. going to instantiate some instances of that class
    #3. maybe play around with more class stuff

# resources:
    # 1. https://docs.python.org/3/tutorial/classes.html (good)
    # 2. https://www.w3schools.com/python/python_classes.asp (quick & dirty)

# define the class
class book:
    
    purpose = 'record-keeping'

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.year = int

    def info(self):
        print("BOOK INFO:")
        print("title: " + self.title)
        print("author: " + self.author)

# create and instance of the class
book1 = book("the bible", "god")
book1 # i guess this does nothing
book1.info()

print ("end")

print("THE NEEW THING")
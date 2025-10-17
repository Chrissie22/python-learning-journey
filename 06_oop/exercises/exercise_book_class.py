class Book:
    def __init__(self, title, authour):
        self.title = title
        self.author = authour
        self.is_checked_out = False
         
    def check_out(self):
        if self.is_checked_out == False:
            self.is_checked_out = True
            print(f" '{self.title}' has been checked out.")
        else:
            print(f" '{self.title}' is already checked out.")
            
    def check_in(self):
        if self.is_checked_out  == True:
            self.is_checked_out = False
            print(f" '{self.title}' has been checked in.")
        else:
            print(f" '{self.title}' was already checked in.")
            
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("Life of a Developer", "Christabel")

book1.check_out()
book1.check_out()
book1.check_in()
book1.check_in()
book2.check_out()
book2.check_out()
book2.check_in()
book2.check_in()


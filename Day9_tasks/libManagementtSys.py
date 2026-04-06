'''
Library Management System (Constructor & Inheritance)
A library stores information about books and digital books. Create a base class Book
with a constructor to initialize book details. Create a derived class EBook that adds file
size information.
'''
class Book():
    def __init__(self,author,pages):
      self.author=author
      self.pages= pages
     
class Ebook(Book):
    def __init__(self,author,pages,filesize):
         super().__init__(author,pages)
         self.filesize=filesize
    def details(self):
        print("Author of the book:",self.author)
        print("NUmber of pages:",self.pages)
        print("File Size:",self.filesize,"MB")

book_1=Ebook("Harsha",165,4)
book_1.details()

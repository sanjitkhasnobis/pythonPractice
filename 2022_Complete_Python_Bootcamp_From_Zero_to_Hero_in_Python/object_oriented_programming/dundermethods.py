

class book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    #Magic method/dunder method
    def __str__(self):
        print ("The {} is written by {}".format(self.title,self.author))

    def __len__(self):
        print("The no of pages of the book is {}".format(self.pages))

mybook = book("who am I","Oliver King",1200)
mybook.__str__()
mybook.__len__()
class Library:
    def __init__(self,name,list_of_books,location):
        self.booklist=list_of_books
        self.name=name
        self.location=location
        self.lendDict={}
    def displaybooks(self):
        print('We have the following books in our library:{self.name}')
        for book in self.booklist:
            print(book)
    def lendbook(self,book,):
        if book not in self.lendDict:
            print(f"Sorry we do not have the book at the moment")
        elif book in self.lendDict: 
            print('The book is already being used by{self.lenDit[book]}')
        else:
            self.lendDict[book]= user
            print('Lender-Book database has been updated.You can take the book now.')
    def addbook(self,book):
        self.booklist.append(book)
        print(f"{book} has been added to the booklist." )
    def returnbook(self,book):
        if book in self.lendDict:
            del self.lendDict[book]
            print('Book has been returned.')
        else:
            print('That book wasn`t borrowed fro us.')
if __name__ == "__main__":
    books= Library(['python','Rich Dad Poor Dad','Harry Portter','c++ Basics','Anatomy''let`s upskill'])
    user_name = input ('Welcome to the {books.name} library. Please choose an option:')
    while True:
         print(f"\n hello {user_name}, welcome to the {books.name} library. Please choose  an option:")
         print("1. Display books \n2. Lend book \n3. Add book \n4. Return book" )
         user_choice = input("Enter your choice to continue:")
         if user_choice not in ['1', '2', '3', '4','s']:
             print("Please enter a valid option.")
             continue
         if user_choice == '1':
             books.displaybooks()
         elif user_choice == '2':
                book = input("Enter the name of the book you want to lend: ")
                books.lendbook(user_name,book)
         elif user_choice == '3':
             book=input('Enter the name of the book you want to add:')
             books.addBook(book)
         elif user_choice == '4':
             book=input('Enter the name of the book you want to return:')
             books.returnbook(book)
         elif user_choice == '5':
             print(f'Thank you for using the library, {user_name}. Goodbye!')
             break        

        
              


                                   
                        

    
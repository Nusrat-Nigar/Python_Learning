class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return len(self.title)
    
book1 = Book('Harry Potter', "J.K Rowling")
book2 = Book('Kafan', 'Prem Chandra')
print(str(book1))
print(len(book1))

print(str(book2))
print(len(book2))

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Print information about an obejct. Similar to call and print an object.
    def __repr__(self):
        return f"Book(title='{self.title}, author='{self.author}, year={self.year})"
    
# Creating an instance of Book
WutheringHeights = Book("Wuthering Heights", "Emily Bronte", 1847)

#using repr method to get the string representation
print(repr(WutheringHeights))

print(WutheringHeights)



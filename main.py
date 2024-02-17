class Library:

    def __init__(self):
        self.file = open("books.txt", "a+")
        self.titles = []
        self.authors = []
        self.release_years = []
        self.pages = []

        import os
        if os.path.exists("books.txt"):
            # Read existing book records from the file and populate the lists
            with open("books.txt", "r") as control:
                for line in control:
                    parts = line.strip().split(", ")
                    self.titles.append(parts[0])
                    self.authors.append(parts[1])
                    self.release_years.append(parts[2])
                    self.pages.append(parts[3])

    def listBooks(self):
        print("List of Books:")
        print(f"There is {len(self.titles)} book(s)")
        print("-----------------------")
        for i in range(len(self.titles)):
            print("Title:", self.titles[i])
            print("Author:", self.authors[i])
            print("-----------------------")
        createMenu()


    def addBook(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_year = input("Enter the release year: ")
        page = input("Enter the number of pages: ")

        # Verileri listelere ekle
        self.titles.append(title)
        self.authors.append(author)
        self.release_years.append(release_year)
        self.pages.append(page)

        with open("books.txt", "a+") as file:
            file.write(title + ", " + author + ", " + release_year + ", " + page + "\n")

        createMenu()


    def removeBook(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        for i in range(len(self.titles)):
            if self.titles[i] == title_to_remove:
                del self.titles[i]
                del self.authors[i]
                del self.release_years[i]
                del self.pages[i]
                break

        with open("books.txt", "w") as file:
            for i in range(len(self.titles)):
                file.write(self.titles[i] + ", " + self.authors[i] + ", " + self.release_years[i] + ", " + self.pages[i] + "\n")

        createMenu()

def createMenu():
    print("***MENU***")
    print("1) List Books")
    print("2) Add Books")
    print("3) Remove Books")
    print("4) Please enter 'q' for exit")


lib = Library()
file = open("books.txt", "a+")
createMenu()
while True:
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        lib.listBooks()

    elif choice == "2":
        lib.addBook()

    elif choice == "3":
        lib.removeBook()

    elif choice.lower() == "q":
        print("Exiting the program.")
        break  # break the infinity loop
    else:
        print("Invalid choice. Please enter a valid option.")
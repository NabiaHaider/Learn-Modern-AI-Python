import json  # JSON module import kiya, file read/write ke liye

# Class ek blue print hota hai jisme data aur functions (methods) hote hain
class BookCollection:    
    """Books ka collection manage karne wali class"""

    def __init__(self):  
        """Naya book collection initialize karta hai, file se data load karta hai"""
        self.book_list = []  # Books store karne ke liye khali list
        self.storage_file = "books_data.json"  # File jisme books ka data store hoga
        self.read_from_file()  # Start hote hi data load kar lein

    def read_from_file(self):
        """File se saved books read karta hai, agar file na ho to khali list banata hai"""
        try:
            with open(self.storage_file, "r") as file:  # File read mode mein kholta hai
                self.book_list = json.load(file)  # JSON data ko list mein convert karta hai
        except (FileNotFoundError, json.JSONDecodeError):  # Agar file na mile ya corrupt ho
            self.book_list = []  # To khali list rakhta hai

    def save_to_file(self):
        """Book list ko JSON file mein save karta hai permanent storage ke liye"""
        with open(self.storage_file, "w") as file:  # File write mode mein open hoti hai
            json.dump(self.book_list, file, indent=4)  # List ko file mein likhta hai (4 space indent ke sath)

    def create_new_book(self):
        """Nayi book add karta hai user se input le kar"""
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        # Book details ek dictionary mein store kiye
        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)  # Book list mein new book add ki
        self.save_to_file()  # File mein save kiya
        print("Book added successfully!\n")

    def delete_book(self):
        """Title ke zariye book delete karta hai"""
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():  # Case-insensitive check
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")  # Agar book na mile

    def find_book(self):
        """Book ya author ke naam se search karta hai"""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()

        # Matching books dhoondta hai
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("No matching books found.\n")  # Agar kuch na mile

    def update_book(self):
        """Book ke details ko edit karne ka function"""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower() == "yes"
                )
                self.save_to_file()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")  # Agar title match na kare

    def show_all_books(self):
        """Saari books list karta hai"""
        if not self.book_list:
            print("Your collection is empty.\n")
            return

        print("Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )
        print()

    def show_reading_progress(self):
        """Kitni books read ho chuki hain, iska percentage show karta hai"""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        """Main menu interface - user se options leta hai"""
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Thank you for using Book Collection Manager. Goodbye!")
                break  # Loop se bahar nikal jata hai
            else:
                print("Invalid choice. Please try again.\n")  # Agar wrong input ho

# Program ka entry point
if __name__ == "__main__":
    book_manager = BookCollection()  # Class ka object banaya
    book_manager.start_application()  # App start ki

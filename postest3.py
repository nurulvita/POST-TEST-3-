# POST TEST 3 (DOUBLE LINKED LIST)
# NURUL VITA AZIZAH (2209116038)

# Mengimpor modul os dan prettytable
import os
from prettytable import PrettyTable

os.system("cls")

# Mendefinisikan kelas Book
class Book:
    def __init__(self, code, title, author):
        self.code = code
        self.title = title
        self.author = author
        self.prev = None
        self.next = None

# Mendefinisikan kelas Library
class Library:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []  # inisialisasi variabel history

    # Menambahkan buku ke katalog
    def add_book(self, code, title, author):
        # Membuat objek baru dari kelas Book
        new_book = Book(code, title, author)
        # Jika katalog kosong, maka buku menjadi head dan tail
        if not self.head:
            self.head = new_book
            self.tail = new_book
        else:
            # Buku baru menjadi buku setelah tail
            self.tail.next = new_book
            # Buku sebelumnya adalah tail
            new_book.prev = self.tail
            # Buku baru sekarang adalah tail
            self.tail = new_book
        # Menambahkan catatan ke history
        self.history.append("-" * 41)
        self.history.append(f"Added: {title}\nby {author} with code {code}")

    # Mengupdate buku berdasarkan kode buku
    def update_book(self, code):
        current_book = self.head
        while current_book:
            if current_book.code == code:
                # Meminta input dari pengguna untuk mengubah judul dan/atau penulis
                new_title = input("Enter new title (leave blank to keep current title): ")
                new_author = input("Enter new author (leave blank to keep current author): ")
                # Jika tidak ada perubahan yang diminta, maka keluar dari fungsi
                if new_title == "" and new_author == "":
                    print("Nothing to update.")
                    return
                # Jika judul tidak diminta diubah, maka judul tetap sama
                if new_title == "":
                    new_title = current_book.title
                # Jika penulis tidak diminta diubah, maka penulis tetap sama
                if new_author == "":
                    new_author = current_book.author
                # Mengupdate judul dan penulis buku
                current_book.title = new_title
                current_book.author = new_author
                # Menambahkan catatan ke history
                print(f"{current_book.title} with code {code} has been updated.")
                self.history.append("-" * 41)
                self.history.append(f"Updated: {current_book.title}\nby {current_book.author} with code {code}")
                return
            current_book = current_book.next
        # Jika tidak ditemukan buku dengan kode yang dimaksud, maka keluar dari fungsi
        print(f"{code} is not in the catalog.")

    # Menghapus buku berdasarkan kode buku
    def remove_book(self, code):
        current_book = self.head
        while current_book:
            if current_book.code == code:
                if current_book.prev:
                    current_book.prev.next = current_book.next
                else:
                    self.head = current_book.next
                if current_book.next:
                    current_book.next.prev = current_book.prev
                else:
                    self.tail = current_book.prev
                # Mencetak pesan bahwa buku telah dihapus dari katalog
                print(f"{current_book.title} with code {code} has been removed from the catalog.")
                self.history.append("-"*41)
                # Menambahkan aksi hapus buku ke dalam riwayat
                self.history.append(f"Removed: {current_book.title} \nby {current_book.author} with code {code}")  # tambahan untuk mencatat history
                return
            current_book = current_book.next
        # Jika kode buku tidak ditemukan dalam katalog, mencetak pesan kesalahan
        print(f"{code} is not in the catalog.")

    # Menampilkan riwayat tindakan yang dilakukan pada katalog
    def display_history(self):  
        print( "History Library ".center(41,"="))
        for action in self.history:
            print(action)

    # Mencari buku berdasarkan kode buku
    def search_book(self, keyword):
        current_book = self.head
        found_books = []
        while current_book:
            if keyword.lower() in current_book.title.lower() or keyword.lower() in current_book.author.lower() or keyword.lower() == current_book.code.lower():
                found_books.append(current_book)
            current_book = current_book.next

        if found_books:
            table = PrettyTable()
            table.field_names = ["Code", "Title", "Author"]
            for book in found_books:
                table.add_row([book.code, book.title, book.author])
            # Menampilkan daftar buku yang ditemukan dengan keyword
            print(f"Found {len(found_books)} book(s) with '{keyword}':")
            print(table)
        # Jika tidak ada buku yang ditemukan dengan keyword
        else :
            print(f"No books found with '{keyword}'.")
    
    # Menampilkan daftar buku
    def display_books(self):
        current_book = self.head
        if not current_book:
            print("The catalog is empty.")
            return
        table = PrettyTable()
        table.title = "LIBRARY BOOK LIST"
        table.field_names = ["Code","Title", "Author"]
        while current_book:
            table.add_row([current_book.code, current_book.title, current_book.author])
            current_book = current_book.next
        print(table)

library = Library()
library.add_book("A001","Laskar Pelangi", "Andrea Hirata")
library.add_book("A002","The Hobbit", "J.R.R. Tolkien")
library.add_book("A003","Negeri 5 Menara", "Ahmad Fuadi")
library.add_book("A004","Perahu Kertas", "Dee Lestari")
library.add_book("A005","Sang Pemimpi", "Andrea Hirata")
library.add_book("A006","Perahu Kertas", "Dee Lestari")
library.add_book("A007","5 cm", "Donny Dhirgantoro")
library.add_book("A008","Pergi", "Tere Liye")

# Fungsi utama untuk mengatur alur program.
def main():
        print("LIBRARY MANAGEMENT SYSTEM".center(41,"="))
        name = input("Enter your name: ")
        os.system("cls")
        print("="*41)
        print(f" Welcome to library {name} ^_^".center(41,"-"))
        # Loop program utama
        while True:
            print("="*41)
            print("What would you like to do?".center(41))
            print("-----------------------------------------")
            print("| [1] Add a book to the catalog         |")
            print("| [2] Remove a book from the catalog    |")
            print("| [3] Search for a book                 |")
            print("| [4] Display all books                 |")
            print("| [5] Update a book                     |")
            print("| [6] History library                   |")
            print("| [7] Exit                              |")
            print("-----------------------------------------")
            choice = input("Enter your choice: ")
        
            # Pilihan 1: Menambahkan buku ke katalog
            if choice == "1":
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                code = input("Enter the code of the book: ")
                library.add_book(code, title, author)
                print(f"{title} by {author} has been added to the catalog with code [{code}].")
                library.display_books()
                input("Press enter to continue...")
                os.system("cls")
            # Pilihan 2: Menghapus buku dari katalog
            elif choice == "2":
                library.display_books()
                code = input("Enter the code of the book to remove: ")
                library.remove_book(code)
                input("Press enter to continue...")
                os.system("cls")
            # Pilihan 3: Mencari buku di katalog
            elif choice == "3":
                keyword = input("Enter the keyword to search for: ")
                library.search_book(keyword)
                input("Press enter to continue...")
                os.system("cls")
            # Pilihan 4: Menampilkan seluruh buku di katalog
            elif choice == "4":
                library.display_books()
                input("Press enter to continue...")
                os.system("cls")
            # Pilihan 5: Mengupdate data buku
            elif choice == "5":
                library.display_books()
                code = input("Enter the book code you want to update : ")
                library.update_book(code)
                input("Press enter to continue...")
                os.system("cls")
            # Pilihan 6: Menampilkan history perubahan di katalog
            elif choice == "6":
                library.display_history()
                print("-"*41)
                input("Press enter to continue...")
                os.system("cls")
            # Pilihan 7: Keluar dari program
            elif choice == "7":
                print("Thank you for using the Library Management System!")
                break
            # Pilihan tidak valid
            else:
                print("Invalid choice. Please try again.")

# Memanggil fungsi utama
main()
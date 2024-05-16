from fastapi import FastAPI,Body

app = FastAPI()


books = [
  {"Judul": "Tetralogi Buru","Author": "Pramudya Ananta Toer","Category": "Revolusi"},
  {"Judul": "Sahabat","Author": "Agam Wispi","Category": "Kiri"},
  {"Judul": "Kamus Al-Qur'an","Author": "Nazwar Syamsu","Category": "Agama"},
  {"Judul": "Tan Malaka : Pergulatan Menuju Republik","Author": "Harry A. Poeze","Category": "Revolusi"},
  {"Judul": "Jang sudah hilang","Author": "Pramudya Ananta Toer","Category": "Fiksi sastra"},
  {"Judul": "Madilog","Author": "Tan Malaka","Category": "Kiri"},
  {"Judul": "Dari Penjara ke Penjara","Author": "Tan Malaka","Category": "Revolusi"},
  {"Judul": "Islam dan Sosialisme","Author": "HOS Tjokroaminoto","Category": "Sejarah"},
  {"Judul": "Demokrasi Kita","Author": "Muhammad Hatta","Category": "Revolusi" }
]

dictionary_books = {
    '1': {'Judul': 'Tetralogi Buru', 'Author': 'Pramudya Ananta Toer', 'Category': 'Revolusi'},
    '2': {'Judul': 'Demokrasi Kita', 'Author': 'Muhammad Hatta', 'Category': 'Revolusi'},
    '3': {'Judul': 'Sahabat', 'Author': 'Agam Wispi', 'Category': 'Kiri'},
    '4': {'Judul': 'Kamus Al-Qur"an', 'Author': 'Nazwar Syamsu', 'Category': 'Agama'},
    '5': {'Judul': 'Tan Malaka : Pergulatan Menuju Republik', 'Author': 'Harry A. Poeze', 'Category': 'Revolusi'}
    
}

@app.get('/alldictionary_books')
async def read_all_dict_books():
    return dictionary_books

@app.get('/allbooks')
async def read_all_books():
    return books

#Path Parameter
@app.get('/books/{judul}') #langsung merujuk ke judul yang ingin dicari
async def read_book(judul:str):
    for book in books:
        if book.get('Judul').casefold() == judul.casefold(): #menggunakan get karena dia langsung mengakses kedalam dict books
            return book #/books/{judul}: "Mengembalikan buku dengan judul yang sesuai.

        
#Query parameter menggunakan / sebagai penutup query        
@app.get('/books/by_query/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in books:
        if book.get('Category').casefold() == category.casefold(): #menggunakan get karena dia langsung mengakses kedalam dict books
            books_to_return.append(book)
    return books_to_return 

    #/books/: "Mengembalikan daftar buku berdasarkan kategori yang diberikan sebagai query parameter."

@app.get('/books/{book_author}/') #DISINI
async def read_author_categor_by_query(book_author:str,category:str):
    books_to_return = []
    for book in books:
        if book.get('Author').casefold() == book_author.casefold() and book.get('Category').casefold() == category.casefold(): #menggunakan get karena dia langsung mengakses kedalam dict books
            books_to_return.append(book)
    return books_to_return 
    #/books/{book_author}/: "Mengembalikan daftar buku oleh penulis tertentu dalam kategori tertentu yang diberikan sebagai query parameter.

@app.post('/books/create_book')
async def create_book(new_book = Body() ):
    books.append(new_book)
    #{"Judul":"Islam dan Sosialisme", "Author":"HOS Tjokroaminoto", "Category":"Sejarah"} # yang ini dari HTTP POST
    #HARUS MENGGUNAKAN DOUBLE QUOTE ("") dalam mengisi body tidak boleh dengan single quote ('')

@app.put('/books/update_book')
async def update_book(updated_book = Body()):
    for i in range(len(books)):
        if books[i].get('Judul').casefold() == updated_book.get('Judul').casefold(): #menggunakan get karena dia langsung mengakses kedalam dict books
            books[i] = updated_book

@app.delete('/books/delete_books/{book_title}')
async def delete_book(book_title:str):
    for i in range(len(books)):
        if books[i].get('Judul').casefold() == book_title.casefold(): #menggunakan get karena dia langsung mengakses kedalam dict books
            books.pop(i)
            break

@app.get('/books_byauthor/{author}')
async def get_books_by_author(author:str):
    kumpulan_buku_authorsama = []
    for authorr in books:
        if authorr.get('Author').casefold() == author.casefold(): #menggunakan get karena dia langsung mengakses kedalam dict books
            kumpulan_buku_authorsama.append(authorr)

    return kumpulan_buku_authorsama
        
@app.get('/book/by_authorr/') #YANG BERMASALAH
async def get_book_by_auth(author:str):
    kumpulan_buku_authorsama = []
    for auth in books:
        if auth.get('Author').casefold() == author.casefold(): #menggunakan get karena dia langsung mengakses kedalam dict books
            kumpulan_buku_authorsama.append(auth)
    return kumpulan_buku_authorsama

#https://gemini.google.com/app/6f6f3a38f9406f0d penjelasan masalah diatas ini
        
'''Penjelasan trailing slash(/) di penutup query 
Analisis Perbedaan Hasil Route /books/by_query dan /books/by_query/
Perbedaan hasil route /books/by_query dan /books/by_query/ pada kode yang Anda berikan terletak pada trailing slash (garis miring di akhir URL).

1. Route dengan Trailing Slash (/books/by_query/)

Saat Anda menggunakan trailing slash, URL diinterpretasikan sebagai direktori, bukan file.
FastAPI mencocokkan URL dengan route handler berdasarkan tingkatan direktori.
Dalam kasus ini, route /books/by_query/ cocok dengan route handler read_category_by_query karena nama direktori (books) dan nama file (by_query) cocok dengan URL.
Oleh karena itu, fungsi read_category_by_query dijalankan dan mengembalikan daftar buku yang sesuai dengan kategori yang diberikan.
2. Route tanpa Trailing Slash (/books/by_query)

Ketika Anda tidak menggunakan trailing slash, URL diinterpretasikan sebagai file.
FastAPI tidak memiliki route handler yang cocok dengan URL books/by_query karena tidak ada file dengan nama tersebut di direktori books.
Akibatnya, FastAPI mengembalikan status HTTP 404 (Not Found) dan tidak menjalankan fungsi read_category_by_query.
Kesimpulan:

Trailing slash penting untuk route yang ingin Anda gunakan sebagai direktori dan menjalankan fungsi route handler berdasarkan tingkatan direktori.
Jika Anda ingin route hanya menangani file, hindari trailing slash.
Solusi:

Gunakan trailing slash (/books/by_query/) jika Anda ingin route berfungsi sebagai direktori dan menjalankan fungsi read_category_by_query.
Ubah nama route menjadi /books/by_query_file tanpa trailing slash jika Anda ingin route hanya menangani file dan mengembalikan hasil yang sama seperti /books/by_query/.
Catatan:

Sebaiknya gunakan trailing slash secara konsisten di seluruh aplikasi Anda untuk menghindari kebingungan dan perilaku yang tidak terduga.
Anda dapat membaca dokumentasi resmi FastAPI tentang https://stackoverflow.com/questions/70007582/fastapi-post-method-call-with-and-without-trailing-slashes untuk informasi lebih lanjut.

Perbedaan Mengakses Direktori dan Mengakses File dalam Penjelasan Trailing Slash di FastAPI
Trailing slash (garis miring di akhir URL) memiliki perbedaan makna dalam konteks mengakses direktori dan file dalam FastAPI:

1. Mengakses Direktori:

Saat Anda menggunakan trailing slash, URL diinterpretasikan sebagai direktori, bukan file.
FastAPI mencocokkan URL dengan route handler berdasarkan tingkatan direktori.
Contoh: URL /books/ diinterpretasikan sebagai direktori books.
Dalam kasus ini, FastAPI akan mencari route handler yang cocok dengan nama direktori (books).
2. Mengakses File:

Ketika Anda tidak menggunakan trailing slash, URL diinterpretasikan sebagai file.
FastAPI mencocokkan URL dengan route handler berdasarkan nama file.
Contoh: URL /books/by_query diinterpretasikan sebagai file by_query di dalam direktori books.
Dalam kasus ini, FastAPI akan mencari route handler dengan nama file yang cocok (by_query).
Perbedaan Perilaku:

Mengakses Direktori:
Route handler yang cocok akan dijalankan berdasarkan tingkatan direktori.
Fungsi route handler dapat mengembalikan daftar file atau konten direktori.
Mengakses File:
Route handler yang cocok dengan nama file akan dijalankan.
Fungsi route handler biasanya mengembalikan konten file.
Contoh Implementasi:

Misalkan Anda memiliki struktur direktori berikut:

books/
├── by_author.py
├── by_category.py
└── by_title.py
Mengakses Direktori:
URL /books/ akan cocok dengan route handler yang ditentukan dalam file index.py (misalkan file ini berisi daftar file dan direktori di dalam direktori books).
Mengakses File:
URL /books/by_author.py akan cocok dengan route handler yang ditentukan dalam file by_author.py.
URL /books/by_category.py akan cocok dengan route handler yang ditentukan dalam file by_category.py.
URL /books/by_title.py akan cocok dengan route handler yang ditentukan dalam file by_title.py.
Kesimpulan:

Trailing slash menunjukkan bahwa URL diinterpretasikan sebagai direktori.
Tanpa trailing slash, URL diinterpretasikan sebagai file.
Perbedaan ini memengaruhi bagaimana FastAPI mencocokkan URL dengan route handler dan menentukan fungsi yang akan dijalankan.
Praktik Terbaik:

Gunakan trailing slash secara konsisten di seluruh aplikasi Anda untuk menghindari kebingungan dan perilaku yang tidak terduga.
Dokumentasikan dengan jelas bagaimana URL Anda diinterpretasikan (direktori atau file) untuk membantu pengguna memahami cara mengakses data Anda.
Sumber Daya Tambahan:

Dokumentasi Resmi FastAPI tentang Trailing Slash: [URL yang tidak valid dihapus]
Pertanyaan Stack Overflow tentang Trailing Slash di FastAPI: https://stackoverflow.com/questions/70007582/fastapi-post-method-call-with-and-without-trailing-slashes
'''
#uvicorn app:app --reload untuk reload atau start fast api

#DAY 2










































from fastapi import FastAPI,Body,Path,Query,HTTPException
from pydantic import BaseModel,Field 
from typing import Optional
from starlette import status



app = FastAPI()

class book: #pembuatan class
    id:int
    title:str
    author:str
    description:str
    rating:int
    published_date : int

    def __init__(self,id,title,author,description,rating, published_date): #proses pembuatan class buku 
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel): 
    id: Optional[int] = None
    title:str = Field(min_length=3) #memberikan min lengt untuk memberikan minim karakter yang disubmit
    author:str = Field(min_length=1, max_length=100)
    description:str = Field(min_length=3, max_length=100)
    rating:int = Field(gt=-1, lt=6) #gt = greater than lt = less than 
    published_date : int
    #penggunaan field pada class ini membuat sebuah class dapat memberikan parameter tertentu sebelum value tersebut dapat di submit 

    class Config: #pembuatan contoh pembuatan example value pada request body di swagger 
        json_schema_extra = {
            'example' : {
                'title':'Judul Buku Baru',
                'author':'Tian',
                'description':'Deskripsi Buku Baru', 
                'rating': 5 ,
                'published_date': 2020
            }
        }

books = [
    book(1, 'Tetralogi Buru', 'Pramoedya Ananta Toer', 'REAL BOOK', 5, 1957),
    book(2, 'Sahabat', 'Agam Wispi', 'Kiri', 4, 2017),
    book(3, 'Kamus Al-Qur\'an', 'Nazwar Syamsu', 'Agama', 3, 2003),
    book(4, 'Tan Malaka : Pergulatan Menuju Republik', 'Harry A. Poeze', 'Revolusi', 5, 2001),
    book(5, 'Jang sudah hilang', 'Pramudya Ananta Toer', 'Fiksi sastra', 5, 1948),
    book(6, 'Madilog', 'Tan Malaka', 'Kiri', 3, 1943),
    book(7, 'Dari Penjara ke Penjara', 'Tan Malaka', 'Revolusi', 5, 1980),
    book(8, 'Islam dan Sosialisme', 'HOS Tjokroaminoto' ,'Sejarah', 5, 1961),
    book(9, 'Demokrasi Kita', 'Muhammad Hatta', 'Revolusi', 2, 1957)
]


@app.get('/books',status_code=status.HTTP_200_OK)
async def get_all_books():
    return books

#Video pertama berfokus pada membuat class,membuat list isi dari buku serta membuat 1 route untuk menampilkan hasil buku tersebut

# @app.post('/create_books') #bentuk awal 
# async def create_books(tambah_buku = Body()):
#     books.append(tambah_buku)




@app.post('/create_books',status_code=status.HTTP_201_CREATED) #bentuk setelah menggunakan pydantic
async def create_books(tambah_buku : BookRequest):#tambah buku harus berisi objek yang mengikuti struktur data dalam class BookRequest
    #Lebih baik menggunakan book request karena didalamnya terdapat fitur untuk validasi data, bisa menjaga keamanan data dari manipulasi data, membuat lebih teratur dari segi pemeliharaan dan menjaga konsistensi dan fleksibilitas terhadap penambahan bidang atau penyesuaian terhadap batasan dan validasi
    new_book = book(**tambah_buku.model_dump()) 
    #mengambil data dari objek tambah buku dan meneruskan ke konstruktor class book
    #Double ** digunakan untuk membongkar dict yang diekstrak menjadi argument keyword individual untuk konstruktor class
    books.append(find_book_id(new_book))

'''dalam video ke 2 berfokus pada penambahan buku di class book dan di variabel books tapi terdapat masalah dimana
kita bisa membuat rating lebih dari ketentuan dan id bisa berwujud (-) atau minus
'''

'''
dalam video ke 3 berfokus pada validasi data menggunakan pydantic di library python 
'''
'''Penjelasan Rinci Kode FastAPI untuk create_books
Kode create_books di FastAPI memiliki fungsi untuk menambahkan data buku baru ke dalam daftar buku (books). 
Berikut penjelasan rincinya:

1. Decorator @app.post:

Decorator @app.post menandakan bahwa fungsi ini menangani request HTTP POST.
Request HTTP POST digunakan untuk mengirim data baru ke server.
Dalam kasus ini, request HTTP POST digunakan untuk menambahkan data buku baru.
2. Parameter tambah_buku:

Parameter tambah_buku menerima objek BookRequest.
BookRequest adalah kelas yang dibuat untuk menampung data buku yang akan ditambahkan.
Data buku ini dikemas dalam bentuk JSON sebelum dikirim ke server.
3. book(**tambah_buku.model_dump()):

Baris kode ini membuat objek buku baru berdasarkan data yang terdapat dalam tambah_buku.
model_dump() adalah metode yang disediakan oleh FastAPI untuk mengonversi objek BookRequest menjadi dictionary JSON.
Dictionary JSON ini kemudian dilewatkan ke konstruktor kelas book untuk membuat objek buku baru.
4. print(new_book):

Baris kode ini mencetak objek buku baru ke konsol.
Hal ini dapat membantu untuk memeriksa apakah data buku baru telah dibuat dengan benar.
5. books.append(new_book):

Baris kode ini menambahkan objek buku baru ke dalam daftar buku (books).
Daftar buku ini digunakan untuk menyimpan semua data buku di aplikasi FastAPI.
Kesimpulan:

Kode create_books di FastAPI memungkinkan pengguna untuk menambahkan data buku baru ke dalam aplikasi. 
Kode ini menangani request HTTP POST, mengonversi data JSON menjadi objek buku, mencetak objek buku baru, 
dan menambahkan objek buku baru ke dalam daftar buku.

Tips:

Pastikan Anda membuat kelas BookRequest yang sesuai dengan struktur data buku yang ingin Anda tambahkan.
Anda dapat memodifikasi kode ini untuk menambahkan validasi data dan menangani error dengan lebih baik.
Semoga penjelasan ini membantu!
'''


def find_book_id(book:book):
    if len(books) > 0:
        book.id = books[-1].id + 1 
    else:
        book.id = 1 
    
    return book

'''CARA KERJA FUNGSI find_book_id
Baik, mari saya jelaskan dengan lebih rinci. books[-1] mengambil elemen terakhir dari daftar books. 
Kemudian .id mengambil nilai atribut id dari objek buku tersebut.

Mari kita tinjau langkah demi langkah:

books[-1]: Ini adalah cara Python untuk mengakses elemen terakhir dari sebuah list. 
Indeks -1 merujuk pada elemen terakhir dari list. Dalam konteks ini, books[-1] mengambil objek buku terakhir dari daftar books.

.id: Setelah kita mendapatkan objek buku terakhir dari books, kita ingin mengakses atribut id dari objek tersebut. 
Atribut id adalah atribut yang telah Anda tetapkan dalam definisi kelas book.

Jadi, kombinasi books[-1].id mengambil nilai ID dari objek buku terakhir dalam daftar books.

Misalnya, jika kita memiliki daftar buku seperti ini:

python
Copy code
books = [
    book(1, 'Buku 1', 'Penulis 1', 'Deskripsi 1', 5),
    book(2, 'Buku 2', 'Penulis 2', 'Deskripsi 2', 4),
    book(3, 'Buku 3', 'Penulis 3', 'Deskripsi 3', 3)
]
Ketika kita mengakses books[-1].id, kita akan mendapatkan nilai ID dari buku terakhir dalam daftar, yaitu 3.
'''

#88 disini mempelajari untuk data validasi menggunakan field dalam library pydantic dan membuat id baru untuk setiap buku baru 
'''detail nya 
class BookRequest(BaseModel):
    id: Optional[int]
    title:str = Field(min_length=3) #memberikan min lengt untuk memberikan minim karakter yang disubmit
    author:str = Field(min_length=1, max_length=100)
    description:str = Field(min_length=3, max_length=100)
    rating:int = Field(gt=-1, lt=6) #gt = greater than lt = less than 

    def find_book_id(book:book): UNTUK PENAMBAHAN ID BARU
    if len(books) > 0:
        book.id = books[-1].id + 1 
    else:
        book.id = 1 
    
    return book
'''

#dalam video 89 disini berfokus pada configurasi terutama di dalam schema dan example value di swagger open api fast api
'''detailnya
penambahan id: Optional[int] = None , Field(title='id  not needed') tapi title tidak muncul jadi kurang begitu berguna

dan penambahan di bagian 
class Config:
        json_schema_extra = {
            'example' : {
                'title':'Judul Buku Baru',
                'author':'Tian',
                'description':'Deskripsi Buku Baru', 
                'rating': 5 
            }
        }

untuk memudahkan ketika belum di executte sudah diberikan gambaran seperti apa nilai nilai yang akan ditampilkan dalam example value
'''


@app.get('/books/{book_id}',status_code=status.HTTP_200_OK)
def Read_book_by_id(book_id:int = Path(gt=0)):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404 , detail='Items not found')

#dalam video 90 berfokus pada bagaimana mencari buku berdasarkan dengan id nya 

@app.get('/books/read_by_rating/',status_code=status.HTTP_200_OK)
def read_book_by_rating(rating:int = Query(gt=-1, lt=6)):
    all_books_by_rating =[]
    for book in books:
        if book.rating == rating: #penggunaan book.rating bisa dijalankan langsung tanpa get karena dia bisa langsung mengakses book karena book adalah objek dari kelas book yang sudah di definisikan diatas berbeda dengan get karena get mengakses ke dict langsung 
            all_books_by_rating.append(book)
    return all_books_by_rating


# dalam video ke 91 berfokus dalam bagaimana kita bisa melakukan pencarian buku yang memiliki rating sama dengan metode query parameter 


@app.put('/books/update_book/',status_code=status.HTTP_204_NO_CONTENT) #jika didalam video tutorial tidak harus menulis id disini harus menulis id 
def update_book(book:BookRequest):
    book_changed = False
    for i in range(len(books)):
        if books[i].id == book.id:
            books[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

#dalam video ke 92 kita berfokus dalam bagaimana untuk melakukan update data tapi kita tetap harus memasukkan id yang ada walaupun di video kita tidak harus memasukkan id 


@app.delete('/books/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id:int = Path(gt=0)):
    book_changed = False
    for i in range(len(books)):
        if books[i].id == book_id:
            books.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='item not found ')


@app.get('/books/get_by_published_date/{published_date}',status_code=status.HTTP_200_OK)
#tidak bisa dengan @app.get('/books/{published_date}') karena sama persis dengan  @app.get('/books/{book_id}') karena http method yang sama dan url depan yang sama harus diganti paling tidak menjadi url yang sekarang 
def get_book_by_published_date(published_date : int = Path(gt=1900,lt=2100)):
    all_book_by_published_date = []
    for book in books:
        if book.published_date == published_date:
            all_book_by_published_date.append(book)
    return all_book_by_published_date
        

#pada Video 96 dan 97 berfokus pada membuat data validation di path dan query parameter sama seperti penggunaan field di class bookrequest
'''Contohnya 
path parameter :
@app.get('/books/get_by_published_date/{published_date}')
def get_book_by_published_date(published_date : int = Path(gt=1900,lt=2100)): disini letak perbedaan penambahan validasi data dengan menggunakan = path(value data validation)
    all_book_by_published_date = []
    for book in books:
        if book.published_date == published_date:
            all_book_by_published_date.append(book)
    return all_book_by_published_date

query parameter : 
@app.put('/books/update_book') 
def update_book(book:BookRequest = Query(gt=0)):
    for i in range(len(books)):
        if books[i].id == book.id:
            books[i] = book
'''


#Didalam video 99 dan 100 berfokus pada pembuatan adanya exception untuk apabila ada kondisi data nya tidak ada atau kondisi lain bisa mengirimkan status code tertentu dan penambahan status code untuk by default berapa status code apabila data berhasil terkirim

'''
@app.delete('/books/{book_id}',status_code=status.HTTP_204_NO_CONTENT) #bagian pembuatan default status code
def delete_book(book_id:int = Path(gt=0)):
    book_changed = False
    for i in range(len(books)):
        if books[i].id == book_id:
            books.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='item not found ') #bagian pembuatan exception 
'''




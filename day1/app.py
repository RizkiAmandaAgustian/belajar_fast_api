# #Membahas variabel dan sedikit tentang string #

# uang = 50
# pajak = 3/100 
# harga_barang = uang -15-(15*pajak)
# print(harga_barang)
# #jawabanku 35.45 tapi harus e 34.55 wkwkwkwk ternyata efek kurung asw
# tes = "agus"
# tis = "tian"
# hasil = "HI {}{}"
# print(hasil.format(tes,tis)) # ternyata iso ngene ki tak kiro gur F'{value}'

# nama = input('siapa nama anda\n')
# ultah = input('berapa hari lagi sampai anda ulang tahun\n')
# tes = int(ultah) // 7 
# print(f'ulang tahun {nama} ternyata masih tersisa {tes} minggu lagi')

#list 

list_saya = [20,1,2,3]
print(list_saya)
list_orang = ['TES','TIS','TUS']
print(list_orang[0:2]) # [X:Y] jika data hanya diisi X maka akan menampilkan data yang ingin dicari 
                       # namun jika Y juga dicari maka data tersebut akan menampilkan urutan sampai sebelum y karena y tidak akan ditampilkan
'''
beberapa contoh perintah dalam list. X = contoh variabel list
X.append = menambahkan data ke baris atau bagian dari list 
x.Insert(Z,Y) = menambahkan data ke baris dengan Z sebagai tujuan urutan data Y sebagai value yang ingin dimasukkan
x.remove(y) = menghapus data yang spesifik dengan y
x.pop(y) = menghapus data yang spesifik dalam urutan ke-y dari list yang tersedia
x.sort() = mengurutkan by default akan mengirimkan data urut asc
'''
# SET 
set_saya = {1,2,4,5,1,2}
print(set_saya)# akan menghasilkan 1 2 4 5 saja karena set tidak memperbolehkan adanya duplikasi data yang sama
# print(set_saya[0]) akan menghasilkan eror karena set tidak memperbolehkan menampilkan data spesifik yang diinginkan menggunakan [0]
'''
beberapa contoh perintah dalam list. X = contoh variabel set
x.discard(y) = menghapus isi data set yang memiliki nilai spesifik seperti yang dimasukkan kedalam Y
x.clear() = untuk menghapus seluruh data yang ada dalam set
x.add(y) = seperti append untuk menambahkan data ke dalam baris terakhir dengan value(y)
x.add([a,b,c]) = seperti add diatas tapi ini bisa menambah data banyak sekaligus 


'''
# tuple 
tuple_saya = (1,2,3,4,5,3,2,1)
print(tuple_saya)
'''
pada dasarnya tipe data ini normal seperti bisa dicari spesifik dan bisa duplikasi
namun tipe data ini memiliki kekurangan yaitu tidak bisa menambah data
'''
'''
Lists Assignment
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals
'''
zoo = ['Lion','Tiger','Elephant','Rabbit','Hippopotamus']
print(zoo)
zoo.pop(3)
zoo.append('Cat')
zoo.remove('Lion')
print(zoo)
print(zoo[0:3])

#BOOLEAN AND OPERATOR
# suka_game = True #Bool TRUE
# suka_duren = False#BOOL FALSE
# makanan = 'Mie'
# angka = 123
# print(type(suka_game)) 
# print(type(suka_duren))
# print(type(makanan))
# print(type(angka))

# print(1>2) #operator 
# print(1<2)
# print(1==2)
# print(1!=2)
# print(1<=2)
# print(1>=2)

# print(1 < 2 and 3 < 5)
# print(1 > 2 and 3 < 5) #operator logical AND harus memiliki kebenaran dalam kedua statement
# print(1 > 2 or 3 < 5) # sedangkan operator OR 'Bisa' hanya memiliki 1 kebenaran dalam 2 statement dan akan dianggap true 


#IF ELSE STATEMENT

x = 23

if x >= 10 and x <= 20: # apabila X memenuhi operator ini maka operasi ini dilakukan
    print('X bilangan belasan')
elif x <= 99 and x >= 21:# apabila X tidak memenuhi operator pertama maka elif akan menjadi opsi jika sesuai maka akan di eksekusi apabila tidak akan dicek ke elif lainya atau langsung ke els
    print('Bilangan Puluhan')
else:
    print('X bilangan kecil') # apabila X tidak memenuhi operator di atas maka operasi ini yang dilakukan
print('INI TETAP DI PRINT APAPUN YANG TERJADI') #Bagian ini tetap akan di print apapun yang terjadi karena ini diluar dari if else tersebut 

# angka = int(input('MASUKKAN ANGKA HASIL UJIAN \n'))

# if angka >= 90:
#     print(f'karena nilai anda {angka} maka nilai anda A')
# elif angka >= 80:
#     print(f'karena nilai anda {angka} maka nilai anda B')
# elif angka >= 70:
#     print(f'karena nilai anda {angka} maka nilai anda C')
# elif angka >= 60:
#     print(f'karena nilai anda {angka} maka nilai anda D')
# else:
#     print(f'karena nilai anda dibawah ketentuan maka nilai anda F')

#FOOR LOOP & WHILE

# my_list = ['ini tes list di loop 1','ini tes list di loop 2','ini tes list di loop 3','ini tes list di loop 4','ini tes list di loop 5','ini tes list di loop 6','ini tes list di loop 7','ini tes list di loop 8']
# for wkwkwk in my_list: #mencoba for loop sedangkan masih sedikit bingung
#     print(wkwkwk)

# for x in range(1,10):
#     print(x)

# hayolo = [1,2,3,4,5,6,7,8,9,10]
# totalan = 0
# for y in hayolo:
#     totalan += y
# print(f'Hasil dari totalan adalah {totalan}')

# i = 0 

# while i < 5:
#     i += 1 
#     print(i)

# given = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
# p = 1
# while p < 4 :
#     p += 1
#     for l in given:
#         if l == 'MONDAY':
#             print('--------------')
#             continue
#         print(l)

#DICTIONARY 
        
# user_dict = {
#     'username': 'coding with tian',
#     'name': 'Tian',
#     'age' : 32
# }
# user_dict['HIDUP'] = True #Akan menambahkan data kedalam dictionary
# tesaja = {'Kegiatan saat puasa':['Coding','Bermain HP']} # ini juga akan menambahkan data kedalam dictionary
# user_dict.update(tesaja)
# print(user_dict)
# print(len(user_dict)) #mencari Jumlah value yang ada didalam dictionary tersebut
# user_dict.pop('age') # mengeluarkan value age dari dictionary
# print(user_dict)

# for g,h in user_dict.items(): #for Looping guna untuk mendapatkan key jika ingin mendapatkan value tambah .items dalam perintah looping tersebut
#     print(g,h)

'''
Dictionaries Assignment
Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values
- Create a new variable vehicle2, which is a copy of my_vehicle
- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
- Delete the mileage key and value from vehicle2
- Print just the keys from vehicle2
'''

# my_vehicle = {
#     'Model':'Ford',
#     'Make': 'Explorer',
#     'Year': 2018,
#     'Mileage' : 40000
# }

# for yeyeye,lalala in my_vehicle.items():
#     print(yeyeye,lalala)

# vehicle2 = my_vehicle.copy()
# vehicle2['Number of Tires'] = 4
# print (vehicle2)

# vehicle2.pop('Mileage')
# print(vehicle2)

# for tes in vehicle2:
#     print(tes)

# Function 

# print('Hello to function')

# def fungsi_saya():   #pembuatan definisi dari suatu fungsi kalau dalam baris ini bernama fungsi saya
#     print('Didalam fungsi') 

# fungsi_saya() #pemanggilan fungsi dan akan menampilkan print yang terdapat dalam definisi diatas

# def print_my_name (first_name,last_name): #definisi print_my_name menerima 2 parameter first_name,last_name
#     print(f'hello {first_name} {last_name}!') # disini first_name,last_name tersebut dipanggil dalam f string

# print_my_name('Rizki Amanda','AGUSTIAN') # disini definisi tersebut kita panggil dan dalam parameter kita masukkan isi dari parameter

# def greet(name, age): #contoh lain
#     print(f'Selamat datang {name}, usia Anda {age} tahun.')

# greet('Andi', 25)

# def greet(name, message="Selamat pagi!"): #contoh lain
#   print(f"{message}, {name}!") # walaupun secara parameter yang berarti pesan sudah terdefinisikan dalam parameter dan tinggal dipanggil kedalam print dan parameter name menerima langsung dari string yang berisi andi

# greet("Andi") # Output: "Selamat pagi!, Andi!"

# def print_color_red(): #CONTOH SCOPE GLOBAL DAN LOCAL 
#     color = 'red'
#     print(color)

# color = 'Blue'
# print(color)
# print_color_red()

# def angka(angka_tertinggi, angka_terendah):
#     print(angka_tertinggi)
#     print(angka_terendah)

# angka(angka_tertinggi=10, angka_terendah=5) #kalau tidak di deklarasikan secara spesifik setiap parameter maka akan dipanggil sesuai urutan pemanggilan 

# def perkalian(u,i):
#     return u * i

# solusi = perkalian(9,8)
# print(solusi)

# def buy_item(cost_of_item):
#     return cost_of_item + add_tax_to_item(cost_of_item)

# def add_tax_to_item(cost_of_item):
#     current_tax_rate = .03
#     return cost_of_item * current_tax_rate

# final_cost = buy_item(50)
# print(final_cost)
'''
Functions Assignment
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
'''

def biodata(first_name,last_name,age): #salah
    return print( F'{first_name} {last_name} {age}')

biodata('Rizki Amanda','Agustian',23)


#revisi 
def biodata_revisi(nama_depan,nama_belakang,umur):
    revisi = {
        'Firstname': nama_depan,
        'Lastname': nama_belakang,
        'AGE' : umur
    }
    return revisi
solusi = biodata_revisi(nama_depan='RIZKI AMANDA', nama_belakang='AGUSTIAN',umur= 23)
print(solusi)

homework_assignment_grades = {
    'homework 1': 85,
    'homework 2': 100,
    'homework 3': 81
}

def calculate_homework (homework_assignment_arg):
    sum_of_grades = 0
    for homework in homework_assignment_arg.values():
        sum_of_grades += homework
    final_grade = sum_of_grades / len(homework_assignment_arg)
    print(final_grade)

calculate_homework(homework_assignment_grades)


#OOP IN PYTHON

'''4 PILAR UTAMA OOP PYTHON ABSTRACTION, CONSTRUCTOR, ENCAPSULATION DAN INHERITANCE

Abstraksi: Proses menyembunyikan detail tertentu dan menyoroti hanya informasi penting dari objek untuk interaksi 
            yang lebih sederhana dan efektif.
Konstruksi: Pembuatan objek dari suatu kelas dengan menggunakan metode khusus __init__, yang memungkinkan inisialisasi 
            atribut-atribut objek.
Enkapsulasi: Konsep dalam OOP di mana data bersama dengan metode yang mengoperasikan data tersebut terkandung dalam sebuah objek, 
            dan akses ke data dibatasi ke metode-metode objek itu sendiri.
Pewarisan (Inheritance): Proses di mana sebuah kelas mewarisi atribut dan metode dari kelas induknya, memungkinkan untuk penataan 
            hierarki dan penggunaan kembali kode yang lebih efisien.

'''

class Student :
    school = 'Online School'
    number_of_student = 0

    def __init__(self,First_name,Last_name,Major):
        self.Firstname = First_name
        self.Lastname = Last_name
        self.major = Major

        Student.number_of_student += 1


    def fullname_with_major(self):
        return f'{self.Firstname} {self.Lastname} {self.major}'
    
    def fullname_major_school(self):
        return f'{self.Firstname} {self.major} {self.school}'
    
    @classmethod
    def set_online_school(cls,new_school):
        cls.school = new_school
    @classmethod
    def split_student(cls,student_str):
        first_name,Last_name,Major = student_str.split('.')
        return cls(first_name,Last_name,Major)

print(Student.number_of_student)
    

student_1 = Student('Rizki Amanda','AGUSTIAN','INTERNATIONAL RELATION')
student_2 = Student('Ramadhan Agung','Pratama Saleh','International Relation')


print(student_1.Firstname) #mengambil Firstname dari class student
print(student_2.Lastname) #mengambil Lastname dari class student
print(Student.number_of_student)


print(student_1.fullname_with_major())

print(student_1.school)
print(student_1.fullname_major_school())

print(student_1.school)
print(student_2.school)

Student.set_online_school('I use zoom')

print(student_1.school)
print(student_2.school)
new_student = 'JOKO.PRAWIRO.JAWA'

student3 = Student.split_student(new_student)
print(student3.fullname_major_school())


from dayy1.HALO import * #contoh import class oop dari luar sebagai module


# musuh = Enemy()

# musuh.type_of_enemy = 'zombies'

# Enemy.talk()

# musuh.walk_fowrward()

# Enemy.attack

# print(f'{Enemy.type_of_enemy} has {Enemy.health_point} health point and can do {Enemy.attack_damage} attack damage')
# print(musuh.attack())
#ABSTRACTION IN OOP 

'''
abstraksi sendiri menyembunyikan impelentasi dari kode dan hanya menunjukkan details kepada user
kenapa harus abstraksi 
-membuat user tidak harus paham fungsionalitas dibelakang layar
-membuat code lebih simple dan reusable
-agar terhindar dari DRY (dont repeat yourself)
-membuat object dalam python lebih scalabe
'''

#Contoh abstraksi dari chat gpt
from abc import ABC, abstractmethod

class Shape(ABC):  # Kelas abstrak Shape
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # Implementasi metode area dari kelas abstrak Shape
        return self.width * self.height

    def perimeter(self):  # Implementasi metode perimeter dari kelas abstrak Shape
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 4)
print("Area:", rectangle.area())         # Output: 20
print("Perimeter:", rectangle.perimeter()) # Output: 18

'''
Dalam contoh di atas, kita memiliki kelas abstrak Shape yang memiliki metode abstrak area() dan perimeter(). 
Kelas Rectangle adalah kelas turunan yang mengimplementasikan metode-metode tersebut. Dengan menggunakan abstraksi, 
kita hanya perlu peduli tentang cara menghitung area dan perimeter sebuah bentuk, 
tanpa harus peduli dengan detail implementasi dari setiap bentuk.
'''

#CONSTRUCTOR IN OOP 

'''
digunakan untuk membuat dan menginisiasi objet dari sebuah class tanpa value permulaan
'''

'''#CHAT GPT
Constructor adalah metode khusus dalam sebuah kelas yang secara otomatis dipanggil ketika sebuah objek dari kelas tersebut dibuat. 
Tujuan utama dari constructor adalah untuk melakukan inisialisasi objek dengan memberikan nilai awal kepada atribut-atribut kelas.

Dalam Python, constructor didefinisikan menggunakan metode bernama __init__(). Setiap kali Anda membuat objek dari kelas, 
constructor __init__() akan dipanggil secara otomatis.

Berikut adalah beberapa hal yang perlu dipahami tentang constructor:
- Nama Metode Khusus: Constructor dalam Python memiliki nama khusus yang harus diikuti, yaitu __init__(). 
Ini adalah konvensi yang disepakati secara umum dalam pemrograman Python.

- Parameter self: Constructor selalu memiliki parameter pertamanya sebagai self. Parameter self merujuk pada objek yang sedang 
dibuat dan digunakan untuk mengakses atribut dan metode objek tersebut.

- Inisialisasi Atribut: Constructor digunakan untuk menginisialisasi atribut-atribut objek dengan memberikan nilai awal. Ini adalah tempat di mana Anda biasanya melakukan inisialisasi untuk semua atribut yang dimiliki oleh objek.
Berikut adalah contoh sederhana penggunaan constructor dalam Python:
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Membuat objek dari kelas Person dan memanggil constructor secara otomatis
person1 = Person("Alice", 30)

# Mencetak atribut dari objek yang sudah dibuat
print("Name:", person1.name)  # Output: Alice
print("Age:", person1.age)    # Output: 30

'''
Dalam contoh di atas, constructor __init__() digunakan untuk menginisialisasi atribut name dan age saat objek dari kelas 
Person dibuat. Ketika objek person1 dibuat, constructor akan dipanggil secara otomatis dengan parameter name dan age 
yang diberikan, dan nilai-nilai tersebut akan disimpan dalam atribut name dan age objek tersebut.
'''

musuh = Enemy('Zombie',15,3)

print(f'{musuh.get_type_of_enemy()} has {musuh.health_point} health points and can do attack of {musuh.attack_damage}')



#ENCAPSULATION IN OOP 

'''#CHAT GPT
Encapsulation adalah konsep di mana data (variabel) bersama dengan metode yang beroperasi pada data tersebut dibungkus 
bersama dalam sebuah unit yang disebut kelas. Dengan menggunakan encapsulation, Anda dapat mengontrol akses ke data tersebut 
dan menerapkan aturan bisnis atau validasi.
'''
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Variabel _balance bersifat protected

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance

account = BankAccount(100)
print("Balance:", account.get_balance())  # Output: 100

account.deposit(50)
print("Balance after deposit:", account.get_balance())  # Output: 150

account.withdraw(30)
print("Balance after withdrawal:", account.get_balance())  # Output: 120

'''
Dalam contoh ini, variabel _balance bersifat "protected", yang berarti seharusnya tidak diakses langsung dari luar kelas. 
Metode deposit() dan withdraw() digunakan untuk memodifikasi saldo, sementara metode get_balance() digunakan untuk mendapatkan 
saldo. Dengan menggunakan encapsulation, kita dapat mengontrol bagaimana data saldo dimanipulasi dan memastikan bahwa validasi 
tertentu diterapkan sebelum perubahan saldo dilakukan.
'''

#INHERITANCE IN OOP 

'''#CHAT GPT
Inheritance (Pewarisan)
Inheritance adalah konsep di mana sebuah kelas dapat mewarisi atribut dan metode dari kelas lain yang disebut 
sebagai kelas induk atau superclass. Kelas turunan atau subclass dapat memperluas fungsionalitas kelas induk dan menerapkan 
fungsionalitas tambahan yang spesifik untuk kebutuhan mereka sendiri.
'''
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog mewarisi dari kelas Animal
    def bark(self):
        print("Dog barks")

'''
-semisal parent tidak punya fungsi dan child punya fungsi sedangkan kita panggil fungsi parent dengan fungsi child maka akan 
menghasilkan eror 
-sebaliknya apabila child tidak punya fungsi sedangkan fungsi tersebut terdapat dalam parent nya maka otomatis python akan 
mengambil fungsi didalam parent nya karena child class nya memanggil fungsi tersebut sedangkan child nya tidak punya 
fungsi tersebut
'''
dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks


zombie = Zombie(20,1)
ogre = Ogre(30,5)

print(f'{zombie.get_type_of_enemy()} has {zombie.health_point} health point and can do attack of {zombie.attack_damage}')
print(f'{ogre.get_type_of_enemy()} has {ogre.health_point} health point and can do attack of {ogre.attack_damage}')


''' SELF VS SUPER IN OOP
self:
- self adalah parameter yang digunakan dalam definisi metode di dalam sebuah kelas di Python.
- Secara konvensi, self adalah nama parameter yang digunakan untuk merujuk pada objek yang sedang diproses dalam metode tersebut.
- Saat Anda memanggil metode pada objek, Python secara otomatis menyediakan referensi objek tersebut ke dalam parameter self, 
sehingga Anda dapat mengakses atribut dan metode objek tersebut di dalam metode tersebut.

Contoh:
'''
class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

obj = MyClass(10)
obj.print_value()  # Output: 10

'''
Dalam contoh di atas, saat Anda memanggil obj.print_value(), Python secara otomatis memberikan objek obj ke parameter 
self di dalam metode print_value(), yang memungkinkan metode untuk mengakses atribut value dari objek tersebut.
'''

'''
super:
- super() adalah fungsi yang digunakan untuk merujuk ke superclass (parent class) dari suatu kelas.
- Ini berguna ketika Anda ingin mengakses metode atau atribut dari superclass dalam subclass.
- Dalam kebanyakan kasus, super() digunakan di dalam metode di subclass untuk memanggil metode superclass dan menambahkan 
atau mengubah perilaku tersebut.

CONTOH :
'''

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print("I am", self.age, "years old.")

child = Child("Alice", 5)
child.greet()


'''
Dalam contoh di atas, super().__init__(name) digunakan dalam metode __init__ di dalam class Child untuk memanggil metode 
__init__ dari class Parent, yang memungkinkan inisialisasi atribut name dari class Parent untuk dilakukan di dalam class Child. 
Kemudian, super().greet() digunakan dalam metode greet di class Child untuk memanggil metode greet dari class Parent, 
sehingga pesan salam dari class Parent ditampilkan bersama dengan informasi tambahan yang ditambahkan di class Child.

'''

#POLIMOFPHISM IN OOP 

'''

Polimorfisme adalah konsep dalam pemrograman berorientasi objek di mana suatu objek dapat memiliki banyak bentuk (atau perilaku) 
yang berbeda dalam konteks yang berbeda. Dengan kata lain, objek yang sama dapat menunjukkan perilaku yang berbeda tergantung 
pada situasi atau konteksnya. Polimorfisme memungkinkan Anda untuk menulis kode yang lebih fleksibel, modular, dan mudah dikelola.

Di Python, polimorfisme sering dicapai melalui dua mekanisme: overriding metode dan penggunaan metode spesial 
seperti __len__, __add__, dan sebagainya.

Berikut adalah contoh polimorfisme di Python menggunakan overriding metode:
'''
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(5), Circle(3)]

for shape in shapes:
    print("Area:", shape.area())

'''
Dalam contoh di atas, kita mendefinisikan kelas Shape yang memiliki metode area() yang harus diimplementasikan oleh subclassnya. 
Kemudian kita mendefinisikan dua subclass dari Shape: Square dan Circle, masing-masing dengan metode area() yang dioverride 
untuk menghitung luas area mereka sendiri. Saat kita membuat objek-objek dari kedua kelas ini dan memanggil metode area(), 
Python akan memilih implementasi yang sesuai dengan jenis objek yang sedang diproses, menunjukkan polimorfisme.

Ini adalah contoh polimorfisme di Python menggunakan metode spesial:
'''
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Chirp!"

pets = [Dog(), Cat(), Bird()]

for pet in pets:
    print(pet.speak())

'''
Dalam contoh ini, kita mendefinisikan tiga kelas: Dog, Cat, dan Bird, yang semuanya memiliki metode speak(). 
Saat kita membuat objek-objek dari ketiga kelas ini dan memanggil metode speak(), Python akan memanggil implementasi yang sesuai 
dengan jenis objek yang diproses, menunjukkan polimorfisme.

Dengan demikian, melalui penggunaan overriding metode dan metode spesial, Python memungkinkan kita untuk mengimplementasikan 
polimorfisme dengan mudah dan efisien.
'''

def battle (e: Enemy):
    e.talk()
    e.attack()


zombie = Zombie(10,1)
ogre = Ogre(20,3)

battle(ogre)
battle(zombie)


def battlle ( e1 : Enemy, e2 : Enemy):
    e1.talk()
    e2.talk()
    while e1.health_point > 0 and e2.health_point > 0:
        print('-------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_point} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_point} HP left')
        e2.attack()
        e1.health_point -= e2.attack_damage
        e1.attack()
        e2.health_point -= e1.attack_damage
        print('-------------')
    if e1.health_point > 0:
        print(f'{e1.get_type_of_enemy()} wins !')
    else:
        print(f'{e2.get_type_of_enemy()} wins !')

zombie = Zombie(10,1)
ogre = Ogre(20,3)

battlle(zombie,ogre)

#COMPOSITION IN OOP 

'''
Composition adalah salah satu konsep dalam pemrograman berorientasi objek (OOP) di mana sebuah objek terdiri dari beberapa objek 
lain sebagai bagian-bagian nya. Dalam konsep komposisi, hubungan antara objek yang lebih besar (objek induk) dan objek yang 
lebih kecil (objek komponen) adalah hubungan "memiliki" atau "terdiri dari".

Dalam Python, komposisi sering kali diimplementasikan dengan membuat objek-objek dalam kelas induk (atau kelas lain) 
sebagai atribut atau komponen dari objek tersebut. Dengan cara ini, objek induk memiliki akses ke objek-objek komponen, 
dan dapat menggunakan atau memanipulasi mereka sesuai kebutuhan.

Berikut adalah contoh sederhana untuk menjelaskan konsep komposisi:
'''
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()  # Membuat objek Engine sebagai komponen dari Car

    def start(self):
        print("Car started")
        self.engine.start()  # Memanggil metode start dari objek Engine

    def stop(self):
        print("Car stopped")
        self.engine.stop()  # Memanggil metode stop dari objek Engine

car = Car()
car.start()  # Output: Car started \n Engine started
car.stop()   # Output: Car stopped \n Engine stopped

'''
Dalam contoh di atas, kelas Car memiliki objek Engine sebagai salah satu atributnya. Ini adalah contoh komposisi 
di mana Car terdiri dari Engine. Ketika metode start() dipanggil pada objek Car, ia juga memanggil metode start() 
pada objek Engine yang merupakan salah satu komponennya. Hal yang sama berlaku untuk metode stop().

Dengan menggunakan komposisi, kita dapat membuat struktur objek yang modular dan mudah diorganisasikan, 
di mana kita membagi fungsionalitas ke dalam bagian-bagian yang lebih kecil dan lebih terfokus. Ini membantu dalam 
pengembangan dan pemeliharaan kode yang lebih bersih, terstruktur, dan mudah dimengerti.
'''

def hero_batle ( hero : Hero, e2 : Enemy):
    e2.talk()
    while hero.health_point > 0 and e2.health_point > 0:
        print('-------------')
        
        print(f'hero : {hero.health_point} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_point} HP left')
        e2.attack()
        hero.health_point -= e2.attack_damage
        hero.attack()
        e2.health_point -= hero.attack_damage
        print('-------------')
    if hero.health_point > 0:
        print(f' HERO  wins !')
    else:
        print(f'{e2.get_type_of_enemy()} wins !')

zombie = Zombie(10,1)
ogre = Ogre(20,3)
hero = Hero(10,1)
weapon = Weapon('Sword',10)
hero.weapon = weapon
hero.equip_weapon()

hero_batle(hero,ogre)




























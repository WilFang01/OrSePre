# Tugas Kecil Stima 2
Program OrSePre (Order Semester with Prerequisite) adalah sebuah program untuk mengurutkan mata kuliah per semester sesuai dengan prasyarat dari mata kuliah.

Deskripsi Singkat
Program ini memanfaatkan algoritma Decrease and Conquer dan diimplementasikan menggunakan Topological Sort. Program akan membentuk sebuah array 2d yang menampung semua mata kuliah. Untuk mata kuliah yang memiliki prasyarat, prasyarat akan dimasukkan ke dalam array mata kuliah tersebut dalam indeks berikutnya. Kemudian, masing-masing mata kuliah akan dihitung derajat-masuk. Mata kuliah yang sudah terdaftar dalam semester akan dihilangkan dari prasyarat mata kuliah yang memiliki prasyarat mata kuliah tersebut, sehingga derajat-masuk mata kuliah tersebut berkurang, yang mana akan menghasilkan sebuah daftar derajat simpul baru ingga semua mata kuliah sudah terdaftar dalam semester.

Requirement Program :
  -Python
  
Cara menggunakan program : 
1. Buka file main_13519025.py dalam aplikasi python atau aplikasi yang mendukung bahasa python
2. Siapkan sebuah testfile yang ingin diurutkan mata kuliahnya
3. Pada program main_13519025.py, ubahlah directory dari open file ke directory tempat testfile berada
4. Run Program
 
Identitas pembuat :
Wilbert Fangderson (13519025)

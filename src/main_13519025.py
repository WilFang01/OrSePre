# NIM : 13519025
# Nama : Wilbert Fangderson
# Tugas Kecil 2 Stima

# Penyusunan Rencana Kuliah dengan Topological Sort
# Penerapan Decrease and Conquer

from fungsi_13519025 import *

# Program Utama 
# =============
# Hitung jumlah line pada file
with open("testfile8.txt","r") as file :
    jumlah_matkul = count_line(file)

# Register matkul
with open("testfile8.txt","r") as file :
    matkul = register_matkul(file,jumlah_matkul)

# Menghapus spasi pada head dan tail setiap matkul
for i in range(jumlah_matkul):
    for j in range(len(matkul[i])):
        matkul[i][j] = matkul[i][j].strip()

# Inisialisasi semester pertama dan ubah array dari matkul
semester,matkul = register_satu_semester(matkul,len(matkul))

# sem sebagai integer penentu semester ke berapa
sem = 1

# Output
# Selama matkul masih mempunyai isi, maka akan dilakukan loop mengisi semester dan
# menghapus mata kuliah dari array matkul hingga kosong (False)
while (matkul) :
    # Semester hanya boleh <= 8 semester dari QnA
    if (sem < 9) :
        # Output berupa (Semester <semester>  : <matakuliah dalam semester itu>)
        print("Semester",int_to_roman(sem),":",end=" ")
        # Apabila bukan merupakan matkul terakhir dalam satu semester, akan ditambahkan koma
        for i in range (len(semester)):
            if (i < len(semester)-1) :
                print(semester[i],end=", ")
            else :
                print(semester[i],end="")
        # Print New Line (Perapian)
        print()
        semester,matkul = register_satu_semester(matkul,len(matkul))
        sem+=1
    # Apabila semester > 8
    else :
        print("Kapan mau tamatnya T.T")

# Output semester terakhir diluar looping
if (sem < 9):
    print("Semester",int_to_roman(sem),":",end=" ")
    for i in range (len(semester)):
        if (i < len(semester)-1) :
            print(semester[i],end=", ")
        else :
            print(semester[i],end="")
    print(".")

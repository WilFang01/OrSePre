# NIM : 13519025
# Nama : Wilbert Fangderson
# Tugas Kecil 2 Stima

# Penyusunan Rencana Kuliah dengan Topological Sort
# Penerapan Decrease and Conquer

# Fungsi
# ======
def count_line(file):
    # Menghitung jumlah line pada file
    total_line = 0
    line = file.read()
    line_split = line.split("\n")

    # Dengan setiap new line, jumlah total_line akan bertambah
    for i in line_split :
        if i :
            total_line += 1

    return total_line


def register_matkul(file,jumlahmatkul):
    # Melakukan register matkul ke dalam array dua dimensi matkul utama (amu)
    amu = [[0 for j in range(jumlahmatkul)] for i in range(jumlahmatkul)]
    # n sebagai integer penentu index ke berapa
    n = 0

    # Looping untuk setiap line yang terdapat dalam file txt
    for line in file :
        # Menghapus spasi pada kepala dan ekor baris
        line = line.strip()
        # Hilangkan titik yang di berada pada end of string
        line = line.replace('.','')
        # Pisahkan depan matkul dengan prereq matkulnya
        amu[n] = line.split(',', jumlahmatkul)
        n += 1

    return amu


def register_satu_semester(matkul,jumlahmatkul):
    # Melakukan register matkul sesuai dengan semesternya
    semester = [0 for i in range(jumlahmatkul)]
    # z sebagai integer penentu index ke berapa dari semester 
    z = 0

    for i in range (jumlahmatkul):
        # Apabila di dalam suatu array hanya terdapat 1 isi (matkul)
        if (len(matkul[i]) == 1) :
            # Matkul dimasukkan ke dalam array semester
            semester[z] = matkul[i][0]
            z+=1

    # Hapus matkul yang terdapat di dalam z
    for m in range (jumlahmatkul):
        for y in range (z):
            if (semester[y] in matkul[m]) :
                # remove untuk menghapus
                matkul[m].remove(semester[y])

    # Hapus nilai 0 yang terdapat dalam array semester
    x = z
    while (x < jumlahmatkul):
        semester.remove(0)
        x+=1

    # Filter untuk menghilangkan array yang kosong ([])
    matkul = list(filter(None,matkul))

    return semester,matkul


def int_to_roman(tahun):
    # Fungsi akan mengubah nilai integer ke dalam bentuk roman
    # Referensi : https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
    
    # Inisialisasi angka romawi untuk 5 4 dan 1
    simbol_tahun = [5, 4, 1]
    simbol_roman = ["V", "IV", "I"]

    # Inisialisasi
    tahun_roman = ''
    i = 0

    # Selama tahun masih > 0, akan digenerate angka romawi V untuk 5, IV untuk 4, dan penambahan I untuk setiap lebih dari 5
    while (tahun > 0) :
        for _ in range (tahun // simbol_tahun[i]):
            tahun_roman += simbol_roman[i]
            tahun -= simbol_tahun[i]
        i+=1

    # Looping merapikan output
    if (tahun_roman == "I") :
        tahun_roman = "I   "
    elif (tahun_roman == "II") :
        tahun_roman = "II  "
    elif (tahun_roman == "III"): 
        tahun_roman = "III "
    elif (tahun_roman == "IV") :
        tahun_roman = "IV  "
    elif (tahun_roman == "V") :
        tahun_roman = "V   "
    elif (tahun_roman == "VI") :
        tahun_roman = "VI  "
    elif (tahun_roman == "VII") :
        tahun_roman = "VII "

    return tahun_roman

# Program Perpustakaan sederhana
# I.S.:Pengguna memasukan array judul (Judul), Penulis Buku (Penulis), Genre Buku (Genre), Tahun Terbit Buku(Tahun)
# F.S.:Menampilkan, Mengurutkan, Menghapus, Mencari, Menambahkan,  
import os

#konstanta
MAKSDAFTAR = 10

# subrutin menu perpustakaan
def MenuUtama(MenuPilihan):
    print('<< MENU PERPUSTAKAAN >>')
    print('1. Pengisian Data Buku')
    print('2. Tampil dan Pengurutan Data Buku')
    print('3. Penghapusan Data Buku')
    print('4. Pencarian Data Buku')
    print('5. Penambahan Data Buku')
    print('6. Penghancuran Data Buku')
    print('0. Keluar')
    MenuPilihan = int(input('Pilihan anda? '))


    #validasi menu beasiswa
    while (MenuPilihan < 0) or (MenuPilihan > 7):
        print('menu yang dipilih tidak boleh negatif dan lebih dari 7, ulangi!')
        os.system('pause')
        os.system('cls')
        # menampilakn menu pilihan kembali
        print('<< MENU PERPUSTAKAAN >>')
        print('1. Pengisian Data Buku')
        print('2. Tampil dan Pengurutan Data Buku')
        print('3. Penghapusan Data Buku')
        print('4. Pencarian Data Buku')
        print('5. Penambahan Data Buku')
        print('6. Penghancuran Data Buku')
        print('0. Keluar')
        MenuPilihan = int(input('Pilihan anda? '))

    return MenuPilihan
    
#subrutin mengisi data buku
def IsiDataBuku(Judul, Penulis, Genre, Tahun,):
    i = 0
    print(f'<<           Data Buku Perpustakaan          >>')
    print(f'-----------------------------------------------')
    Judul[i]              =  str(input('Judul Buku          :')).upper()
    while (Judul[i] != 'STOP'):
        Penulis[i]        =  str(input('Penulis Buku        :')).upper()
        Genre[i]          =  str(input('Genre Buku          :')).upper()
        Tahun[i]          =  int(input('TahunTerbit Buku    :'))

        #memasukan data buku berikutnya
        print()
        i += 1
        print(f'Data Buku Ke-{i+1}')
        print(f'------------------')
        Judul[i]           = str(input('Judul Buku          :')).upper()
    N = i
    return N

#subrutin menu urut data peserta
def MenuUrut(MenuPilihan1):
    print('1. Tampilkan data tanpa pengurutan')
    print('2. Tampilkan data berdasarkan Judul')
    print('3. Tampilkan data berdasarkan Penulis')
    print('4. Tampilkan data berdasarkan Genre')
    print('5. Tampilkan data berdasarkan Tahun Terbit')
    print('0. Keluar')
    MenuPilihan1 = int(input('Pilihan anda? '))

    #validasi menu urut data peserta
    while (MenuPilihan1 < 0) or (MenuPilihan1 > 5):
        print('menu yang dipilih tidak boleh negatif dan lebih dari 5, ulangi!')
        os.system('pause')
        os.system('cls')
        print('1. Tampilkan data tanpa pengurutan')
        print('2. Tampilkan data berdasarkan Judul')
        print('3. Tampilkan data berdasarkan Penulis')
        print('4. Tampilkan data berdasarkan Genre')
        print('5. Tampilkan data berdasarkan Tahun Terbit')
        print('0. Keluar')
        MenuPilihan1 = int(input('Pilihan anda? '))
    return MenuPilihan1

#subrutin tampil data peserta
def TampilDataPeserta(Judul, Penulis, Genre, Tahun, N):
    print('<<                                        DATA BUKU                                            >>')
    print('+-----------------------------------------------------------------------------------------------+')
    print('| No |            Judul           |        Penulis        |       Genre       |   Tahun Terbit   ')
    print('+-----------------------------------------------------------------------------------------------+')
    for i in range(N):
        print(f'| {i + 1:>1}  | {Judul[i]:19} | {Penulis[i]:10} | {Genre[i]:10} | {Tahun[i]:10} |')
    print('+-----------------------------------------------------------------------------------------------+')

#subrutin menu pengurutan berdasarkan Judul
def UrutJudul(UrutJudul1):
    print('<< PENGURUTAN BERDASARKAN JUDUL >>')
    print('1. Pengurutan secara Ascending')
    print('2. Pengurutan secara Descending')
    print('0. Keluar')
    UrutJudul1 = int(input('Pilihan Kamu?'))
    
    # validasi menu pengurutan berdasarkan Judul
    while(UrutJudul1 < 0) or (UrutJudul1 > 2):
        print('menu yang dipilih tidak boleh negatif dan lebih dari 2, ulangi!')
        os.system('pause')
        os.system('cls')
        print('<< PENGURUTAN BERDASARKAN JUDUL >>')
        print('1. Pengurutan secara Ascending')
        print('2. Pengurutan secara Descending')
        print('0. Keluar')
        UrutJudul1 = int(input('Pilihan Kamu?'))
    return UrutJudul1 

#subrutin mengurutkan Nama secara Ascending (Minimum Sort)
def SusunJudulAsc(Judul, Penulis, Genre, Tahun, N):
    for i in range(N-1):
        min = i
        for j in range(min+1,N):
            if(Judul[j] < Judul[min]):
                min = j
                
        #tukarPenulis
        Temp = Penulis[i]
        Penulis[i] = Penulis[min]
        Penulis[min] = Temp
        
        #tukarJudul
        Temp = Judul[i]
        Judul[i] = Judul[min]
        Judul[min] = Temp
            
        #tukarGenre
        Temp = Genre[i]
        Genre[i] = Genre[min]
        Genre[min] = Temp
            
        #tukarTahun
        Temp = Tahun[i]
        Tahun[i] = Tahun[min]
        Tahun[min] = Temp
        
#subrutin mengurutkan Judul secara Descending (Bubble Sort)
def SusunJudulDsc(Judul, Penulis, Genre, Tahun, N):
    for i in range(N-1):
        for j in range(N-(i+1)):
            if(Judul[j] < Judul[j+1]):
                #tukarPenulis
                Temp = Penulis[j]
                Penulis[j] = Penulis[j+1]
                Penulis[j+1] = Temp
                
                #tukarJudul
                Temp = Judul[j]
                Judul[j] = Judul[j+1]
                Judul[j+1] = Temp
                    
                #tukarGenre
                Temp = Genre[j]
                Genre[j] = Genre[j+1]
                Genre[j+1] = Temp
                    
                #tukarTahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp
                
#subrutin menu pengurutan berdasarkan Penulis
def UrutPenulis(UrutPenulis1):
    print('<< PENGURUTAN BERDASARKAN PENULIS >>')
    print('1. Pengurutan secara Ascending')
    print('2. Pengurutan secara Descending')
    print('0. Keluar')
    UrutPenulis1 = int(input('Pilihan Kamu?'))
    
    # validasi menu pengurutan berdasarkan PeNulis
    while(UrutPenulis1 < 0) or (UrutPenulis1 > 2):
        print('menu yang dipilih tidak boleh negatif dan lebih dari 2, ulangi!')
        os.system('pause')
        os.system('cls')
        print('<< PENGURUTAN BERDASARKAN PENULIS >>')
        print('1. Pengurutan secara Ascending')
        print('2. Pengurutan secara Descending')
        print('0. Keluar')
        UrutPenulis1 = int(input('Pilihan Kamu?'))
    return UrutPenulis1

#subrutin mengurutkan Penulis secara Ascending (Minimum Sort)
def SusunPenulisAsc(Judul, Penulis, Genre, Tahun, N):
    for i in range(N-1):
        min = i
        for j in range(min+1,N):
            if(Penulis[j] < Penulis[min]):
                min = j
                
        #tukarPenulis
        Temp = Penulis[i]
        Penulis[i] = Penulis[min]
        Penulis[min] = Temp
        
        #tukarJudul
        Temp = Judul[i]
        Judul[i] = Judul[min]
        Judul[min] = Temp
            
        #tukarGenre
        Temp = Genre[i]
        Genre[i] = Genre[min]
        Genre[min] = Temp
            
        #tukarTahun
        Temp = Tahun[i]
        Tahun[i] = Tahun[min]
        Tahun[min] = Temp 

#subrutin mengurutkan Penulis secara Descending (Bubble Sort)
def SusunPenulisDsc(Judul, Penulis, Genre, Tahun, N):
    for i in range(N-1):
        for j in range(N-(i+1)):
            if(Penulis[j] < Penulis[j+1]):
                #tukarPenulis
                Temp = Penulis[j]
                Penulis[j] = Penulis[j+1]
                Penulis[j+1] = Temp
                
                #tukarJudul
                Temp = Judul[j]
                Judul[j] = Judul[j+1]
                Judul[j+1] = Temp
                    
                #tukarGenre
                Temp = Genre[j]
                Genre[j] = Genre[j+1]
                Genre[j+1] = Temp
                    
                #tukarTahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

# validasi menu pengurutan berdasarkan Genre
    while(UrutGenre1 < 0) or (UrutGenre1 > 2):
        print('menu yang dipilih tidak boleh negatif dan lebih dari 2, ulangi!')
        os.system('pause')
        os.system('cls')
        print('<< PENGURUTAN BERDASARKAN GENRE >>')
        print('1. Pengurutan secara Ascending')
        print('2. Pengurutan secara Descending')
        print('0. Keluar')
        UrutGenre1 = int(input('Pilihan Kamu?'))
    return UrutGenre1

#subrutin mengurutkan Penulis secara Ascending (Minimum Sort)
def SusunGenreAsc(Judul, Penulis, Genre, Tahun, N):
    for i in range(N-1):
        min = i
        for j in range(min+1,N):
            if(Genre[j] < Genre[min]):
                min = j
                
        #tukarPenulis
        Temp = Penulis[i]
        Penulis[i] = Penulis[min]
        Penulis[min] = Temp
        
        #tukarJudul
        Temp = Judul[i]
        Judul[i] = Judul[min]
        Judul[min] = Temp
            
        #tukarGenre
        Temp = Genre[i]
        Genre[i] = Genre[min]
        Genre[min] = Temp
            
        #tukarTahun
        Temp = Tahun[i]
        Tahun[i] = Tahun[min]
        Tahun[min] = Temp  

#subrutin mengurutkan Genre secara Descending (Bubble Sort)
def SusunGenreDsc(Judul, Penulis, Genre, Tahun, N):
    for i in range(N-1):
        for j in range(N-(i+1)):
            if(Genre[j] < Genre[j+1]):
                #tukarPenulis
                Temp = Penulis[j]
                Penulis[j] = Penulis[j+1]
                Penulis[j+1] = Temp
                
                #tukarJudul
                Temp = Judul[j]
                Judul[j] = Judul[j+1]
                Judul[j+1] = Temp
                    
                #tukarGenre
                Temp = Genre[j]
                Genre[j] = Genre[j+1]
                Genre[j+1] = Temp
                    
                #tukarTahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp

# validasi menu pengurutan berdasarkan Tahun
    while(UrutTahun1 < 0) or (UrutTahun1 > 2):
        print('menu yang dipilih tidak boleh negatif dan lebih dari 2, ulangi!')
        os.system('pause')
        os.system('cls')
        print('<< PENGURUTAN BERDASARKAN TAHUN TERBIT >>')
        print('1. Pengurutan secara Ascending')
        print('2. Pengurutan secara Descending')
        print('0. Keluar')
        UrutTahun1 = int(input('Pilihan Kamu?'))
    return UrutTahun1 

#subrutin mengurutkan Tahun secara Ascending (Minimum Sort)
def SusunTahunAsc(Judul, Penulis, Genre, Tahun, N):
    for i in range(N-1):
        min = i
        for j in range(min+1,N):
            if(Tahun[j] < Tahun[min]):
                min = j
                
        #tukarPenulis
        Temp = Penulis[i]
        Penulis[i] = Penulis[min]
        Penulis[min] = Temp
        
        #tukarJudul
        Temp = Judul[i]
        Judul[i] = Judul[min]
        Judul[min] = Temp
            
        #tukarGenre
        Temp = Genre[i]
        Genre[i] = Genre[min]
        Genre[min] = Temp
            
        #tukarTahun
        Temp = Tahun[i]
        Tahun[i] = Tahun[min]
        Tahun[min] = Temp  

#subrutin mengurutkan Tahun secara Descending (Bubble Sort)
def SusunTahunDsc(Judul, Penulis, Genre, Tahun, N):
    for i in range(N-1):
        for j in range(N-(i+1)):
            if(Tahun[j] < Tahun[j+1]):
                #tukarPenulis
                Temp = Penulis[j]
                Penulis[j] = Penulis[j+1]
                Penulis[j+1] = Temp
                
                #tukarJudul
                Temp = Judul[j]
                Judul[j] = Judul[j+1]
                Judul[j+1] = Temp
                    
                #tukarGenre
                Temp = Genre[j]
                Genre[j] = Genre[j+1]
                Genre[j+1] = Temp
                    
                #tukarTahun
                Temp = Tahun[j]
                Tahun[j] = Tahun[j+1]
                Tahun[j+1] = Temp                                                                        

# subrutin menu cari data peserta
def MenuCari(MenuPilihan2):
    print('<<<           Menu Pencarian           >>>')
    print('------------------------------------------')
    print('1. Cari Judul Buku')
    print('2. Cari Penulis Buku')
    print('3. Cari Genre Buku')
    print('4. Cari Tahun Terbit Buku')
    print('0. Keluar')
    MenuPilihan2 = int(input('Pilihan Anda? '))

    # validasi menu pilihan 2
    while(MenuPilihan2 < 0) or (MenuPilihan2 > 6):
        print('menu yang dipilih tidak boleh negatif dan lebih dari 4, ulangi!')
        os.system('pause')
        os.system('cls')
        print('Menu Pencarian')
        print('--------------')
        print('1. Cari Judul Buku')
        print('2. Cari Penulis Buku')
        print('3. Cari Genre Buku')
        print('4. Cari Tahun Terbit Buku')
        print('0. Keluar')
        MenuPilihan2 = int(input('Pilihan Anda? '))

    return MenuPilihan2

# subrutin mencari Judul tertentu menggunakan metode sequential search tanpa sentinel
def CariJudul(Judul, Penulis, Genre, Tahun, N):
    # memasukkan Judul yang dicari
    CariJudul = str(input('Judul yang dicari = ')).upper()
    # proses pencarian
    i = 0
    while(Judul[i] != CariJudul) and (i < N):
        i += 1
    print('<<<                                      DATA YANG DICARI                                          >>>')
    if(Judul[i] == CariJudul):
        print('<<                                        DATA PENDAFTAR                                            >>')
        print(f'Judul Yang Dicari : {CariJudul}')
        print('+-----------------------------------------------------------------------------------------------+')
        print('| No |            Judul           |        Penulis        |       Genre       |   Tahun Terbit   ')
        print('+-----------------------------------------------------------------------------------------------+')
        No = 0
        for j in range(i, N):
            if(Judul[j] == CariJudul):
                print(f'| {i + 1:>1}  | {Judul[i]:19} | {Penulis[i]:10} | {Genre[i]:10} | {Tahun[i]:10} |')
                print('+-----------------------------------------------------------------------------------------------+')
    else:
        print(f'Judul {CariJudul} Tidak Ditemukan!!')

# subrutin mencari Penulis tertentu menggunakan metode sequential search tanpa sentinel
def CariPenulis(Judul, Penulis, Genre, Tahun, N):
    # memasukkan Judul yang dicari
    CariPenulis = str(input('Penulis yang dicari = ')).upper()
    # proses pencarian
    i = 0
    while(Judul[i] != CariPenulis) and (i < N):
        i += 1
    print('<<<                                      DATA YANG DICARI                                          >>>')
    if(Penulis[i] == CariPenulis):
        print('<<                                        DATA PENDAFTAR                                            >>')
        print(f'Judul Yang Dicari : {CariPenulis}')
        print('+-----------------------------------------------------------------------------------------------+')
        print('| No |            Judul           |        Penulis        |       Genre       |   Tahun Terbit   ')
        print('+-----------------------------------------------------------------------------------------------+')
        No = 0
        for j in range(i, N):
            if(Penulis[j] == CariPenulis):
                print(f'| {i + 1:>1}  | {Judul[i]:19} | {Penulis[i]:10} | {Genre[i]:10} | {Tahun[i]:10} |')
                print('+-----------------------------------------------------------------------------------------------+')
    else:
        print(f'Judul {CariPenulis} Tidak Ditemukan!!')   

# subrutin mencari Genre tertentu menggunakan metode sequential search tanpa sentinel
def CariGenre(Judul, Penulis, Genre, Tahun, N):
    # memasukkan Genre yang dicari
    CariGenre = str(input('Genre yang dicari = ')).upper()
    # proses pencarian
    i = 0
    while(Penulis[i] != CariPenulis) and (i < N):
        i += 1
    print('<<<                                      DATA YANG DICARI                                          >>>')
    if(Penulis[i] == CariPenulis):
        print('<<                                        DATA PENDAFTAR                                            >>')
        print(f'Judul Yang Dicari : {CariPenulis}')
        print('+-----------------------------------------------------------------------------------------------+')
        print('| No |            Judul           |        Penulis        |       Genre       |   Tahun Terbit   ')
        print('+-----------------------------------------------------------------------------------------------+')
        No = 0
        for j in range(i, N):
            if(Penulis[j] == CariPenulis):
                print(f'| {i + 1:>1}  | {Judul[i]:19} | {Penulis[i]:10} | {Genre[i]:10} | {Tahun[i]:10} |')
                print('+-----------------------------------------------------------------------------------------------+')
    else:
        print(f'Judul {CariPenulis} Tidak Ditemukan!!')              

def main():
    # Inisialisasi array untuk menyimpan data buku
    Judul = [''] * MAKSDAFTAR
    Penulis = [''] * MAKSDAFTAR
    Genre = [''] * MAKSDAFTAR
    Tahun = [0] * MAKSDAFTAR
    N = 0  # Jumlah buku yang terdaftar
    MenuPilihan = -1

    while MenuPilihan != 0:
        os.system('cls')
        MenuPilihan = MenuUtama(MenuPilihan)

        if MenuPilihan == 1:
            N = IsiDataBuku(Judul, Penulis, Genre, Tahun)

        elif MenuPilihan == 2:
            if N == 0:
                print("Belum ada data buku yang dimasukkan!")
            else:
                MenuPilihan1 = -1
                while MenuPilihan1 != 0:
                    os.system('cls')
                    MenuPilihan1 = MenuUrut(MenuPilihan1)

                    if MenuPilihan1 == 1:
                        TampilDataPeserta(Judul, Penulis, Genre, Tahun, N)

                    elif MenuPilihan1 == 2:
                        UrutJudul1 = UrutJud1ul(UrutJudul1)
                        if UrutJudul1 == 1:
                            SusunJudulAsc(Judul, Penulis, Genre, Tahun, N)
                        elif UrutJudul1 == 2:
                            SusunJudulDsc(Judul, Penulis, Genre, Tahun, N)
                        TampilDataPeserta(Judul, Penulis, Genre, Tahun, N)

                    elif MenuPilihan1 == 3:
                        UrutPenulis1 = UrutPenulis(UrutPenulis1)
                        if UrutPenulis1 == 1:
                            SusunPenulisAsc(Judul, Penulis, Genre, Tahun, N)
                        elif UrutPenulis1 == 2:
                            SusunPenulisDsc(Judul, Penulis, Genre, Tahun, N)
                        TampilDataPeserta(Judul, Penulis, Genre, Tahun, N)

                    elif MenuPilihan1 == 4:
                        UrutGenre1 = UrutGenre(UrutGenre1)
                        if UrutGenre1 == 1:
                            SusunGenreAsc(Judul, Penulis, Genre, Tahun, N)
                        elif UrutGenre1 == 2:
                            SusunGenreDsc(Judul, Penulis, Genre, Tahun, N)
                        TampilDataPeserta(Judul, Penulis, Genre, Tahun, N)

                    elif MenuPilihan1 == 5:
                        UrutTahun1 = UrutTahun(UrutTahun1)
                        if UrutTahun1 == 1:
                            SusunTahunAsc(Judul, Penulis, Genre, Tahun, N)
                        elif UrutTahun1 == 2:
                            SusunTahunDsc(Judul, Penulis, Genre, Tahun, N)
                        TampilDataPeserta(Judul, Penulis, Genre, Tahun, N)

        elif MenuPilihan == 3:
            if N == 0:
                print("Belum ada data buku yang dimasukkan!")
            else:
                JudulHapus = str(input('Masukkan Judul Buku yang ingin dihapus: ')).upper()
                for i in range(N):
                    if Judul[i] == JudulHapus:
                        for j in range(i, N-1):
                            Judul[j] = Judul[j+1]
                            Penulis[j] = Penulis[j+1]
                            Genre[j] = Genre[j+1]
                            Tahun[j] = Tahun[j+1]
                        N -= 1
                        print(f'Buku dengan judul "{JudulHapus}" telah dihapus.')
                        break
                else:
                    print(f'Buku dengan judul "{JudulHapus}" tidak ditemukan.')

        elif MenuPilihan == 4:
            if N == 0:
                print("Belum ada data buku yang dimasukkan!")
            else:
                MenuPilihan2 = -1
                while MenuPilihan2 != 0:
                    os.system('cls')
                    MenuPilihan2 = MenuCari(MenuPilihan2)

                    if MenuPilihan2 == 1:
                        CariJudul(Judul, Penulis, Genre, Tahun, N)
                    elif MenuPilihan2 == 2:
                        CariPenulis(Judul, Penulis, Genre, Tahun, N)
                    elif MenuPilihan2 == 3:
                        CariGenre(Judul, Penulis, Genre, Tahun, N)
                    elif MenuPilihan2 == 4:
                        CariTahun(Judul, Penulis, Genre, Tahun, N)

        elif MenuPilihan == 5:
            if N < MAKSDAFTAR:
                Judul[N] = str(input('Judul Buku          :')).upper()
                Penulis[N] = str(input('Penulis Buku        :')).upper()
                Genre[N] = str(input('Genre Buku          :')).upper()
                Tahun[N] = int(input('Tahun Terbit Buku    :'))
                N += 1
                print("Data buku berhasil ditambahkan.")
            else:
                print("Daftar buku sudah penuh!")

        elif MenuPilihan == 6:
            print("Fitur penghancuran data buku belum diimplementasikan.")

        os.system('pause')

if __name__ == "__main__":
    main()

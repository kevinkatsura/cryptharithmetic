#IMPORT LIBRARY
from datetime import datetime

#MEMBACA FILE DAN DIMASUKKAN KE DALAM ARRAY
namaFile = str(input("Masukkan nama file :"))
file = open(namaFile,'r',encoding='utf8')
array = file.readlines()

# Menghitung waktu
start_time = datetime.now()

for i in range (len(array)) :
    print(array[i].strip('\n'))
for i in range (len(array)) :
    array[i] = array[i].strip('\n').strip('+')
    
valueRetention = []
alphabetList =[]

del array[len(array)-1]
del array[len(array)-2]


#MAIN PROCESS

# Membentuk batasan untuk panjang dari kata input yang diterima oleh program
def panjangSesuai() :
    sesuai = True
    i = 0
    while ( i < (len(array)) and sesuai):
        if( len(array[i]) <= 10 ):
            i+=1
        else:
            sesuai = False
    return sesuai

# Membuat daftar huruf-huruf yang digunakan dalam setiap kata ke dalam suatu array
def arrayKumpulanHuruf():
    for i in array :
        for j in (i):
            k = 0
            Found = False
            while ( k < len(alphabetList) and (not Found )):
                if( alphabetList[k][0] == j ) :
                    Found = True
                else :
                    k +=1
            if ( not Found ) :
                alphabetList.append(j)

# Membentuk batasan pada program agar huruf terdepan dari masing-masing kata tidak bernilai 0
def hurufDepan():
    i = 0
    done = False
    while (i < len(valueRetention) and not done):
        if (valueRetention[i] == 0):
            done = True
        else :
            i+=1
    diDepan = False
    j = 0
    while (not diDepan and j < len(array)):
        if (array[j][0] == alphabetList[i]):
            diDepan =True
        else :
            j+=1
    if(diDepan) :
        print("wowww")
        permutasi(valueRetention)


# Mengatur setiap huruf memiliki nilai awal agar terdaftar
def setNilaiAwalHuruf ():
    for i in range (len(alphabetList)-1,-1,-1):
        valueRetention.append(i)


# Membuat batasan yang merupakan nilai huruf yang diambil tidak dapat digunakan lagi pada huruf lain dalam pencarian nilai pada masing-masing huruf
def cariValue(indeks):
    a = valueRetention[indeks] + 1
    i = 0
    while (i < indeks):
        if(a == valueRetention[i]) :
            a = (a+1)%10
            i = 0
        else :
            i+=1
    return a


# Mengembalikan nilai huruf dari suatu inputan karakter
def cariValueTersedia(x):
    i = 0
    Found = False
    while((not Found) and i < len(alphabetList)):
        if(alphabetList[i] == x ):
            Found = True
        else:
            i+=1
    return valueRetention[i]


# Memperbaharui nilai dari masing-masing huruf pada array dengan pertimbangan kemungkinan-kemungkinan yang tersedia
def permutasi(arrayOfValue):
    done = False
    tanda3=1
    pengurangIndeks = len(arrayOfValue)-1
    i=pengurangIndeks
    while not done:
        if (arrayOfValue[i]+tanda3<=9 and (arrayOfValue[i]+tanda3) not in arrayOfValue):
            arrayOfValue[i] = cariValue(i)
            tanda=1
            tanda2=0
            indeks=pengurangIndeks-i
            while tanda<=indeks:
                if tanda2 not in arrayOfValue:
                    arrayOfValue[i+tanda]=tanda2
                    tanda+=1
                    tanda2+=1
                else:
                    tanda2+=1
            done=True
        elif arrayOfValue[i]==9:
            arrayOfValue[i-1] = cariValue(i-1)
            tanda=0
            tanda2=0
            indeks=pengurangIndeks-i
            while tanda<=indeks:
                if tanda2 not in arrayOfValue:
                    arrayOfValue[i+tanda] = tanda2
                    tanda+=1
                    tanda2+=1
                else:
                    tanda2+=1
            done=True
        elif arrayOfValue[i]+tanda3 >9:
            arrayOfValue[i]=-1    
            i-=1
            tanda3=1
        elif arrayOfValue[i]+tanda3 in arrayOfValue:
            tanda3+=1

if panjangSesuai() :
    arrayKumpulanHuruf()
    setNilaiAwalHuruf()
    Found = False
    JumlahPermutasi = 1
    while (not Found) :
        x = 0
        for i in range (len(array)-1):
            y = ""
            for j in array[i] :
                y = y+str(cariValueTersedia(j))
            x = x + int(y)
        z = ""
        for k in (array[len(array)-1]) :
            z = z + str(cariValueTersedia(k))
        if(x == int(z)) :
            Found = True
        else :
            permutasi(valueRetention)
            JumlahPermutasi+=1
    print(" DENGAN : ")
    for i in range (len(valueRetention)):
        print(alphabetList[i]+" = "+str(valueRetention[i]))
    print(" SOLUSI YANG MUNGKIN ADALAH ")
    
    for j in range (len(array)-1) :
        kata = ""
        for k in array[j] :
            l = 0
            found = False
            while (not found) :
                if(k == alphabetList[l]):
                    kata = kata + str(valueRetention[l])
                    found = True
                else :
                    l += 1
        print(kata)
    print("---------- +")
    kata = ""
    for k in array[len(array)-1] :
        l = 0
        found = False
        while (not found) :
            if(k == alphabetList[l]):
                kata = kata + str(valueRetention[l])
                found = True
            else :
                l += 1
    print(kata)
    end_time = datetime.now()
    print('\nDuration: {}'.format(end_time - start_time))
    print("Total percobaan Cryptarithmetic adalah "+str(JumlahPermutasi))
else :
    print ("Terdapat kata yang memiliki jumlah karakter lebih dari 10.")
    

#CLOSE FILE
file.close()


import sys
sys.path.insert(1,'Lib\site-packages') #all package stored here
import os
import urllib.request
from urllib.request import urlopen
from urllib.request import urlretrieve
import cgi

def DownloadOne(Link_url):
    remotefile = urlopen(Link_url) #Open the provided link
    blah = remotefile.info()['Content-Disposition'] 
    value, params = cgi.parse_header(blah)
    filename = params["filename"] #Getting the file with their extension
    myPath = 'Downloaded/' #Creating new folder
    try:
        os.mkdir(myPath)
    except OSError:
        pass

    fullfilename = os.path.join(myPath, filename)  #Storing the file in the "Downloaded" folder
    urlretrieve(Link_url, fullfilename) #Download the desired file


def DownloadMany(Link_url,Link_urlStart,Link_urlStop):
    for i in range(Link_urlStart,Link_urlStop+1):
        try:                                #To handle lost download link
            DownloadOne(Link_url + str(i))
            print("File dengan kode " + str(i) + " telah didownload")
        except:
            print("File dengan kode " + str(i) + " tidak ditemukan")
while True:
    print("========================= Tilep Elisa ==================================")
    print("1. Tilep satu file")
    print("2. Tilep banyak file")
    print("3. About")
    print("4. Exit")
    Choice =int(input("Pilih opsi : "))

    if Choice == 1:
        Code = int(input("Masukkan angka: "))
        try:                                            #To handle lost download link
            DownloadOne('https://elisa.ugm.ac.id/user/archive/download/'+ str(Code))
            print("File dengan kode " + str(Code) + " telah didownload")
        except:
            print("File dengan kode " + str(Code) + " tidak ditemukan")
    elif Choice == 2:
        Start = int(input("Masukkan angka awal: "))
        Stop = int(input("Masukkan angka akhir: "))
        url = 'https://elisa.ugm.ac.id/user/archive/download/' #Elisa default link
        DownloadMany(url, Start, Stop)
    elif Choice == 3:
        print("")
        print("=================================================================================")
        print("Tools untuk menilep tugas-tugas yang sudah dikumpul di https://elisa.ugm.ac.id")
        print("How it works?")
        print("Kode yang diminta saat input adalah angka yang menunjukkan urutan keberapa tugas tersebut dikumpul")
        print("Urutan angka tersebut sudah mulai dihitung sejak elisa dibuat, maka angka yang dijadikan link adalah angka yang cukup besar")
        print("Struktur link Elisa: https://elisa.ugm.ac.id/user/archive/download/AngkaUrut")
        print("Dengan mengganti angka urut, maka kita bisa mendapat tugas orang lain")
        print("=================================================================================")
        print("")
    else:
        break
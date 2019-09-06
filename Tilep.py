import sys
sys.path.insert(1,'Lib\site-packages')
import os
import urllib.request
from urllib.request import urlopen
from urllib.request import urlretrieve
import cgi

def DownloadOne(Link_url):
    remotefile = urlopen(Link_url)
    blah = remotefile.info()['Content-Disposition']
    value, params = cgi.parse_header(blah)
    filename = params["filename"]
    myPath = 'Downloaded/' #Creating new folder
    try:
        os.mkdir(myPath)
    except OSError:
        pass

    fullfilename = os.path.join(myPath, filename) 
    urlretrieve(Link_url, fullfilename)

def DownloadMany(Link_url,Link_urlStart,Link_urlStop):
    for i in range(Link_urlStart,Link_urlStop+1):
        DownloadOne(Link_url + str(i))
while True:
    print("========================= Tilep Elisa ==================================")
    print("1. Tilep satu file")
    print("2. Tilep banyak file")
    print("3. Exit")
    Choice =int(input("Pilih opsi : "))

    if Choice == 1:
        Code = input("Masukkan angka: ")
        pathDownload = 'Downloaded/' #Creating new folder
        try:
            os.mkdir(pathDownload)
        except OSError:
            pass
        DownloadOne('https://elisa.ugm.ac.id/user/archive/download/'+ str(Code))
    elif (Choice == 2):
        Start = int(input("Masukkan angka awal: "))
        Stop = int(input("Masukkan angka akhir: "))
        url = 'https://elisa.ugm.ac.id/user/archive/download/'
        DownloadMany(url, Start, Stop)
    else:
        break
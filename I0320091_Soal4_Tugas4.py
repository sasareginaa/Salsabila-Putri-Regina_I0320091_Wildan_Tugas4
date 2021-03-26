#Soal 4

umur = int(input("Berapa usia kamu? "))
lulus = input("Apakah Anda sudah lulus ujian kualifikasi (Y / T)? ")

if umur >= 21 :
    if lulus == "Y" :
        print("Anda dapat mendaftar di kursus")
    else :
        print("Anda tidak dapat mendaftar di kursus")
else :
    print("Anda tidak dapat mendaftar di kursus")
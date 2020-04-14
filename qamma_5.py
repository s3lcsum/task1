#program odczytuje plik o formacie .fasta. Można taki wczytać z ncbi
import sys

print (" Program ten jest narzędziem pomocniczym do przeprowadzenia reakcji PCR.\nUżytkownik wczytuje nazwę pliku zawierającego sekwencję nukleotydową w formacie .fasta lub .txt na podstawie której,\n program wylicza procentową zawartość nukleotydów G i C oraz tworzy dwa startery komplementarne do zadanej sekwencji\n")
plik=open(input(" Wprowadź nazwę pliku z rozszerzeniem .fasta: "))
readplik = plik.read() #załadowanie pliku
readplik = readplik.strip() #zrobienie z pliku listy
readplik = readplik.split('\n')
print(readplik) #wydrukowanie pliku, później można to ewentualnie usunąć

gc=0      
at=0
reszta_znakow=0   #zmienne, które będą potem zmieniać wartość wraz z dodaniem kolejnego znaku pasującego w pliku

for line in readplik:
    if line[0] == '>': #tylko pierwsza linijka, która nie ma sekwencji posiada ten symbol
        gc=0
        at=0
        reszta_znakow=0 #wyzerowanie znaków z pierwszej linijki
    else:
        for n in line:
            if n =='G' or n=='g' or n=='C' or n=='c':
                gc+=1
            elif n=='A' or n=='a' or n=='T' or n=='t':
                at+=1 #zsumowanie znaków z następnych linijek

suma=gc+at
print('Zawartość GC w zadanej sekwencji wynosi: ',gc)
print('Zawartość AT w zadanej sekwencji wynosi: ',at)
procent=round((gc/suma)*100)
print("GC stanowią", procent,'% sekwencji')

def make_primer_forward(readplik, forward_len = 20): #tworzenie starteru przedniego
    forward = readplik[1][:(forward_len+1)] #wprowadzenie zakresu sekwencji od 1 znaku do ustanowionego znaku
    return forward
def make_primer_reverse(readplik, reverse_len = 20): #tworzenie starteru końca sekwencji   
    reverse = readplik[-1][(len(readplik[-1])-reverse_len):len(readplik[-1])] #wprowadzenie zakresu sekwencji
    reverse_0 = reverse[::-1]
    dict_nt = {"A":"T","T":"A","C":"G","G":"C","N":"N"} #zamiana nukleotydów na komplementarne
    reverse_1 = ""
    for nt in reverse_0:
        reverse_1 += dict_nt[nt]  #utworzenie listy z komplementarną sekwencją
    return reverse_1

def percent_GC(forward, reverse):
    GC_f = 0
    GC_r = 0
    for nt in forward: #bierze argumenty z powstałego wcześniej forwardu i sprawdza które z nich to G lub C
        if nt == "G" or nt == "C":
            GC_f += 1
    for nt in reverse: 
        if nt == "G" or nt == "C":
            GC_r += 1
    good_number_f = round((GC_f/len(forward))*100) #wyznaczenie %GC starteru forward
    good_number_r = round((GC_r/len(reverse))*100) # wyznaczenie %GC starteru reverse
    rest_of_f=len(forward)-GC_f
    dlugosc=len(reverse)
    if good_number_f-good_number_r>8:
        for i in range(9):
            reverse=reverse[:dlugosc-i]
            good_number_r = round((GC_r/len(reverse))*100) #nowe wyznaczenie %GC reverse po wszelkich poprawkach
            if good_number_f-good_number_r<8:
                 reverse
                 good_number_r
            else:
                 reverse
    else:
        reverse,good_number_r
    if good_number_f-good_number_r>8:
        print("Dopasowanie starterów nie powiodło się, w takim wypadku zostanie wygenerowany starter o długości odpowiadającej tej, co ma forward:")
        reverse=reverse[:19]
        good_number_r
    rest_of_r=len(reverse)-GC_r    
    print ("Procent GC dla startera:")
    print ("dla primera forward wynosi: " + str(good_number_f)+"%")
    print ("Dla ostatecznie dopasowanego reverse wynosi: " + str(good_number_r) + "%")
    print ("Sekwencja primera forward:",forward,",jego długość wynosi:",len(forward))
    print ("Sekwencja primera reverse:",reverse,",jego długość wynosi:",len(reverse))
    Tm_f=(rest_of_f*2)+(GC_f*4)
    Tm_r=(rest_of_r*2)+(GC_r*4)
    print("Temperatura topnienia primera forward wynosi: ",Tm_f,"a primera reverse:",Tm_r)
    if ((Tm_f+Tm_r)/2)>Tm_f+4 or ((Tm_f+Tm_r)/2)<Tm_f-4:
        print("Proponowałabym przeprowadzić tzw. PCR gradientowy. Wtedy zakres wprowadzonych temperatur wyniósłby: od",((Tm_f+Tm_r)/2)-4,", do",((Tm_f+Tm_r)/2)+4)
    else:
        print("Proponowana temperatura do przeprowadzenia reakcji:",(Tm_f+Tm_r)/2)
    return good_number_f, good_number_r
    return len(reverse), len(forward)
    return reverse
forward = make_primer_forward(readplik,18) #utworzenie starteru z nadaną długością sekwencji równą 18
reverse = make_primer_reverse(readplik,25) #działa
good_number_f, good_number_r = percent_GC(forward,reverse)
forward
reverse






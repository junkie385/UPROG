# Napišite program za unos imena i prezimena (jedna varijabla) te adrese stanovanja za 5 
# studenata. Unos imena i prezimena je obavezan, ako se ne unese, tražiti ponovan upis. Unos 
# adrese nije obavezan. Podatci se unose u main funkciji, te se šalju na ispis funkciji ispis. Funkcija 
# ispis može se pozvati na dva načina – sa jednim ili sa dva argumenta. Ako se podatak o adresi ne 
# pošalje funkciji, vrijednost njenog drugog parametra će biti ‘Adresa će biti naknadno upisana’. 

class StudentModel(object):
    def __init__(self, imePrezime, adresa):
        self.ImePrezime = imePrezime
        self.Adresa = adresa

def ispis(p_ip, p_add = "Adresa će biti naknadno upisana."):
    print()
    print(F"Ime i prezime: {p_ip}")
    print(F"Adresa: {p_add}")

def main():
    Studenti = []
    
    for i in range(5):     
        tempImePrezime = ""   
        while tempImePrezime == "":            
            tempImePrezime = input(F"Unesite ime i prezime {i+1}. studenta: ")

        tempAdresa = input(F"Unesite adresu {i+1}. studenta:")

        Studenti.append(StudentModel(tempImePrezime, tempAdresa))

    for stud in Studenti:        
        if stud.Adresa == "":
            ispis(stud.ImePrezime)
        else:
            ispis(stud.ImePrezime, stud.Adresa)

main()
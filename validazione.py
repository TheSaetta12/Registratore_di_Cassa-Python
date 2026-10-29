def chiedi_testo(messaggio):
    while True:
        testo = input(messaggio).strip()
        
        if not testo:
            print("Errore: il campo non può essere vuoto. Riprova.")
            continue
            
        if testo.isdigit():
            print("Errore: il testo non può essere composto solo da numeri. Riprova.")
            continue
            
        return testo

def chiedi_numero(messaggio, minimo, massimo):
    while True:
        try:
            input_utente = input(messaggio)
            
            valore_pulito = input_utente.replace(",", ".")
            
            valore = float(valore_pulito)
            
            if minimo <= valore <= massimo:
                return valore
            else:
                print(f"Errore: inserisci un valore compreso tra {minimo} e {massimo}.")
                
        except ValueError:
            print("Errore: devi inserire un numero valido, non del testo.")

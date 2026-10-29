import validazione
import prodotti
import cassa

def main():
    listino = prodotti.carica_listino()
    
    while True:
        carrello = []
        print("\n=== REGISTRATORE DI CASSA IN FUNZIONE ===")
        
        sessione_attiva = True
        while sessione_attiva:
            nome_input = validazione.chiedi_testo("Inserisci prodotto (o 'fine' per lo scontrino): ")
            
            if nome_input.lower() == "fine":
                if not carrello:
                    print("Errore: il carrello è vuoto. Inserisci almeno un prodotto prima di fare lo scontrino.")
                    continue 
                
                totale = cassa.calcola_totale(carrello)
                sconto = cassa.calcola_sconto(totale)
                print("\n" + cassa.genera_scontrino(carrello, totale, sconto))
                
                print("\nCosa desideri fare?")
                print("1 - Nuovo scontrino (Azzera carrello)")
                print("2 - Aggiungi altri prodotti a questo scontrino")
                print("0 - Esci")
                
                scelta = int(validazione.chiedi_numero("Scegli un'opzione: ", 0, 2))
                
                match scelta:
                    case 1:
                        sessione_attiva = False 
                    case 2:
                        print("\n--- Ritorno all'aggiunta prodotti ---")
                        continue 
                    case 0:
                        print("Chiusura della cassa. Arrivederci!")
                        return

            prodotto = prodotti.cerca_prodotto(listino, nome_input)
            
            if prodotto is None:
                print(f"Attenzione: '{nome_input}' non trovato nel listino.")
            else:
                quantita = validazione.chiedi_numero(f"Quantità per {prodotto['nome']} (1-100): ", 1, 100)
                cassa.aggiungi_al_carrello(carrello, prodotto, quantita)
                print(f"Aggiunto: {prodotto['nome']} x{int(quantita)}")

if __name__ == "__main__":
    main()
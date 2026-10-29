import validazione
import prodotti
import cassa
import formato

def main():
    listino = prodotti.carica_listino()
    carrello = []
    
    while True:
        print("\n===== REGISTRATORE DI CASSA =====")
        print("1 - Aggiungi prodotto al listino")
        print("2 - Mostra listino")
        print("3 - Aggiungi prodotto al carrello")
        print("4 - Mostra totale carrello")
        print("5 - Chiudi scontrino")
        print("6 - Storico scontrini")
        print("0 - Esci")
        
        scelta = input("Seleziona un'opzione: ")

        match scelta:
            case "1":
                nome = validazione.chiedi_testo("Nome del nuovo prodotto: ")
                prezzo = validazione.chiedi_numero(f"Prezzo per '{nome}': ", 0.01, 1000)
                
                risultato = prodotti.aggiungi_prodotto(listino, nome, prezzo)
                
                if risultato is None:
                    print("Errore: Prodotto già presente nel listino!")
                else:
                    print(f"Prodotto '{nome}' aggiunto con successo.")

            case "2":
                elenco = prodotti.listino_formattato(listino)
                if elenco:
                    print("\n--- LISTINO PRODOTTI ---")
                    print(elenco)
                else:
                    print("\nIl listino è vuoto.")

            case "3":
                nome_cerca = validazione.chiedi_testo("Quale prodotto vuoi aggiungere? ")
                prodotto = prodotti.cerca_prodotto(listino, nome_cerca)
                
                if prodotto:
                    quantita = validazione.chiedi_numero(f"Quantità per {prodotto['nome']}: ", 1, 100)
                    cassa.aggiungi_al_carrello(carrello, prodotto, quantita)
                    print(f"Aggiunti {int(quantita)}x {prodotto['nome']} al carrello.")
                else:
                    print(f"Attenzione: '{nome_cerca}' non è presente nel listino.")

            case "4":
                if not carrello:
                    print("Il carrello è vuoto.")
                else:
                    totale = cassa.calcola_totale(carrello)
                    sconto = cassa.calcola_sconto(totale)
                    pagato = round(totale - sconto, 2)
                    
                    print(f"\nTotale attuale: {formato.formatta_euro(totale)}")
                    if sconto > 0:
                        print(f"Sconto applicato (10%): -{formato.formatta_euro(sconto)}")
                    print(f"Importo finale: {formato.formatta_euro(pagato)}")

            case "5":
                if not carrello:
                    print("Errore: Impossibile chiudere uno scontrino vuoto.")
                else:
                    totale = cassa.calcola_totale(carrello)
                    sconto = cassa.calcola_sconto(totale)
                    
                    print("\n" + cassa.genera_scontrino(carrello, totale, sconto))
                    
                    n_scontrino = cassa.salva_scontrino(carrello, totale, sconto)
                    print(f"\nScontrino n. {n_scontrino} salvato con successo!")
                    carrello = []

            case "6":
                print("\n" + cassa.storico_scontrini())

            case "0":
                print("Grazie per aver usato il registratore di cassa. Arrivederci!")
                break

            case _:
                print("Comando non riconosciuto. Riprova.")

if __name__ == "__main__":
    main()
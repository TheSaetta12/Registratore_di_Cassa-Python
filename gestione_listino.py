import prodotti
import validazione

def main():
    listino = prodotti.carica_listino()
    
    print("=== GESTIONE LISTINO PRODOTTI ===")

    while True:
        print("\nScegli un'opzione:")
        print("1 - Aggiungi prodotto")
        print("2 - Mostra listino")
        print("0 - Esci")
        
        scelta = validazione.chiedi_numero("Inserisci il comando: ", 0, 2)

        match int(scelta):
            case 1:
                nome = validazione.chiedi_testo("Nome del prodotto: ")
                prezzo = validazione.chiedi_numero(f"Prezzo per '{nome}': ", 0.01, 1000)
                
                risultato = prodotti.aggiungi_prodotto(listino, nome, prezzo)
                
                if risultato is None:
                    print("Errore: Prodotto già presente nel listino!")
                else:
                    print(f"Prodotto '{nome}' aggiunto correttamente.")

            case 2:
                elenco = prodotti.listino_formattato(listino)
                if elenco:
                    print("\n--- LISTINO ATTUALE ---")
                    print(elenco)
                else:
                    print("\nIl listino è attualmente vuoto.")

            case 0:
                print("Chiusura listino. Arrivederci!")
                break

            case _:
                print("Comando non riconosciuto.")

if __name__ == "__main__":
    main()
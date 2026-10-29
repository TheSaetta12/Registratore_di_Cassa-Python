from validazione import chiedi_testo, chiedi_numero

def main():
    print("--- Test di Validazione ---")

    nome = chiedi_testo("Inserisci il tuo nome: ")

    eta = chiedi_numero("Inserisci la tua età (1-120): ", 1, 120)

    prezzo = chiedi_numero("Inserisci un prezzo (0.01-1000): ", 0.01, 1000)

    print("\n--- Riepilogo Dati ---")
    print(f"Nome: {nome}")
    print(f"Età: {int(eta)} anni")
    print(f"Prezzo: {prezzo:.2f}€")

if __name__ == "__main__":
    main()
def formatta_euro(valore):
    testo_formattato = "%.2f" % valore
    
    testo_italiano = testo_formattato.replace(".", ",")
    
    return f"{testo_italiano} €"
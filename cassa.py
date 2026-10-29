import json
import os
from datetime import datetime
import formato

def aggiungi_al_carrello(carrello, prodotto, quantita):
    subtotale = round(prodotto["prezzo"] * quantita, 2)
    riga = {
        "nome": prodotto["nome"],
        "prezzo": prodotto["prezzo"],
        "quantita": quantita,
        "subtotale": subtotale
    }
    carrello.append(riga)
    return riga

def calcola_totale(carrello):
    totale = 0
    for riga in carrello:
        totale += riga["subtotale"]
    return round(totale, 2)

def calcola_sconto(totale):
    if totale > 50:
        return round(totale * 0.10, 2)
    return 0

def genera_scontrino(carrello, totale, sconto):
    adesso = datetime.now()
    data_it = adesso.strftime("%d/%m/%Y %H:%M")
    
    testo = "===== SCONTRINO FISCALE =====\n"
    testo += f"Data: {data_it}\n\n"
    
    for riga in carrello:
        prezzo_it = formato.formatta_euro(riga["subtotale"])
        testo += f"{riga['nome']} x{riga['quantita']}: {prezzo_it}\n"
    
    testo += "-----------------------------\n"
    testo += f"Totale: {formato.formatta_euro(totale)}\n"
    
    if sconto > 0:
        testo += f"Sconto 10%: -{formato.formatta_euro(sconto)}\n"
    
    pagato = round(totale - sconto, 2)
    testo += f"DA PAGARE: {formato.formatta_euro(pagato)}\n"
    testo += "============================="
    return testo

def carica_scontrini():
    if os.path.exists("scontrini.json"):
        with open("scontrini.json", "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def salva_scontrino(carrello, totale, sconto):
    scontrini = carica_scontrini()
    
    numero = len(scontrini) + 1
    pagato = round(totale - sconto, 2)
    
    nuovo_scontrino = {
        "numero": numero,
        "data_ora": str(datetime.now()),
        "righe": carrello,
        "totale": totale,
        "sconto": sconto,
        "pagato": pagato
    }
    
    scontrini.append(nuovo_scontrino)
    
    with open("scontrini.json", "w", encoding="utf-8") as file:
        json.dump(scontrini, file, indent=4)
    
    return numero

def storico_scontrini():
    scontrini = carica_scontrini()
    if not scontrini:
        return "Nessuno scontrino in archivio."
    
    testo = "============= STORICO SCONTRINI =============\n"
    for s in scontrini:
        d = s["data_ora"]
        data_it = f"{d[8:10]}/{d[5:7]}/{d[0:4]} {d[11:16]}"
        
        pagato_it = formato.formatta_euro(s["pagato"])
        
        testo += f"N. {s['numero']} del {data_it} - Pagato: {pagato_it}\n"
    return testo
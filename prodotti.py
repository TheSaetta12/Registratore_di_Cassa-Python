import json
import os
import formato

def carica_listino():
    if os.path.exists("listino.json"):
        with open("listino.json", "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def salva_listino(listino):
    with open("listino.json", "w", encoding="utf-8") as file:
        json.dump(listino, file, indent=4)

def cerca_prodotto(listino, nome):
    for prodotto in listino:
        if prodotto["nome"].lower() == nome.lower():
            return prodotto
    return None

def aggiungi_prodotto(listino, nome, prezzo):
    if cerca_prodotto(listino, nome):
        return None
    
    nuovo_prodotto = {"nome": nome, "prezzo": prezzo}
    listino.append(nuovo_prodotto)
    salva_listino(listino)
    return nuovo_prodotto

def listino_formattato(listino):
    risultato = ""
    for prodotto in listino:
        prezzo_it = formato.formatta_euro(prodotto["prezzo"])
        risultato += f"{prodotto['nome']} - {prezzo_it}\n"
    return risultato
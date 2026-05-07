#basics
import random
import string

print("\n" + " ✨ PASSWORT-GENERATOR ✨ ".center(40, "="))
print("=" * 40)
total = int(input('\n[#] Gesamtlänge des Passworts: '))
letters = int(input('[A] Anzahl der BUCHSTABEN:     '))
numbers = int(input('[0] Anzahl der ZAHLEN:         '))
symbols = int(input('[#] Anzahl der SYMBOLE:        '))

question = letters + numbers + symbols
passw =[]
let=[]
num =[]
sym =[]
password=[]
#work
if total < question:
    print("\n" + "!" * 40)
    print(" ⚠️ FEHLER: Summe zu groß! ".center(40))
    print("!" * 40 + "\n")
else:
    lettchoice= random.choices(string.ascii_letters,k=letters)
    let+=lettchoice
    numchoice= random.choices(string.digits,k=numbers)
    num+=numchoice
    symchoice= random.choices(string.punctuation,k=symbols)
    sym+=symchoice
    
    password.extend(let+num+sym)
    random.shuffle(password)
#result
    print("\n" + " ERGEBNIS ".center(40, "-"))
    print(f"🔑 Dein sicheres Passwort: ")
    print("━" * 40)
    print(f"  { ''.join(password) }  ".center(40))
    print("━" * 40)
    print("Bewahre es sicher auf!".center(40))
    print("=" * 40 + "\n")
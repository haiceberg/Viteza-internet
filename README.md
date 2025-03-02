# SpeedTest
## Descrierea Programului
Acest program Python efectuează un test de viteză al conexiunii la internet utilizând biblioteca speedtest-cli. Programul măsoară viteza de descărcare, viteza de încărcare și ping-ul și afișează aceste rezultate în megabiti pe secundă (Mbps) și milisecunde (ms).

## Funcționalități
* Măsurarea vitezei de descărcare: Măsoară viteza cu care datele sunt descărcate de la server la client (în Mbps).
* Măsurarea vitezei de încărcare: Măsoară viteza cu care datele sunt încărcate de la client la server (în Mbps).
* Măsurarea ping-ului: Măsoară latenta rețelei (în milisecunde).

## Dependențe
* Python 3.x
* Modul speedtest-cli: Se poate instala utilizând comanda pip install speedtest-cli.

## Rezultate
Programul va măsura și va afișa rezultatele vitezei de descărcare, încărcare și ping pentru conexiunea ta la internet.

###  Intrare 
* Programul va rula automat și va efectua testul de viteză.
* Rezultatele vor fi afișate pe ecran.

###  Ieșire 
La final, scriptul va afișa pe ecran viteza de descărcare, viteza de încărcare și ping-ul, precum în exemplul următor:

 #### Exemplu de output:
   
Viteza de descarcare:  50.12 Mbps
Viteza de incarcare:  10.45 Mbps
Ping:  25 ms
## Explicații

* `test.download()` : Măsoară viteza de descărcare de la serverul ales.
* `test.upload()`: Măsoară viteza de încărcare la serverul ales.
* `test.results.ping`: Măsoară latenta rețelei în milisecunde.
* `round(ds / 10**6, 2)`: Conversia vitezei de descărcare din biți în megabiți pe secundă (Mbps), rotunjit la două zecimale.
* `round(us / 10**6, 2)`: Conversia vitezei de încărcare din biți în megabiți pe secundă (Mbps), rotunjit la două zecimale.

## Personalizare
* Alegerea serverului: Se poate personaliza programul pentru a selecta un server anume pentru testare (de exemplu, cel mai apropiat server geografic).
* Lungimea testului: Poți modifica durata testului pentru o măsurare mai detaliată a vitezei sau pentru a salva rezultatele pe o perioadă mai lungă de timp.

## Contribuții
  Dacă dorești să îmbunătățești acest program sau să adaugi funcționalități suplimentare, te rog să contribui printr-un pull request.

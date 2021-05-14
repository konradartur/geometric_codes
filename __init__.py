# Napisac program, który dla wywołania z parametrami:
# (1) -type t n
# wygeneruje macierz incydencji konfiguracji odpowiedniego typu, przy czym t = A, P, C oznaczaja odpowiednio: płaszczyzne afiniczna, płaszczyzne rzutowai konfiguracje cykliczna; parametr n (bedacy liczbapierwsza) ozna- cza rzad odpowiedniej płaszczyzny lub liczbe elementów ciała w przypad- ku konfiguracji cyklicznej
# (2) -type t n -mindist
# wyznaczy odległosc minimalna kodu utworzonego z wierszy macierzy in- cydencji konfiguracji okreslonej parametrem -type analogicznie jak w (1)
# (3) -type t n -correct file
# przeprowadzi korekcje błedów dla komunikatu składajacego sie z wekto- rów odczytanych (z kolejnych linii) pliku file, przy uzyciu kodu utworzo- nego z macierzy incydencji konfiguracji; korekcje nalezy przeprowadzac zgodnie z zasada najblizszego sasiedztwa (maksymalnego prawdopodo- bienstwa) - w przypadku braku mozliwosci jednoznacznego skorygowania danego wektora program powinien wypisac słowo ERROR i kontynuowac działanie
# UWAGI
# Wyniki obliczen nalezy wypisywac na standardowe wyjscie: kazdy wektor (ew. wiersz macierzy) w osobnej linii, kolejne współrzedne wektora oddzielone spacja. W dalszych czesciach zadania mozna oczywiscie wykorzystac poprzednie - przy- kładowo obliczanie odległosci minimalnej w (2) mozna wykorzystac przy korekcji błedów w (3).
# Prosze zadbac o efektywnosc działania programu - np. rozwiazanie (3), które za- wsze sprawdza “po kolei” wszystkie wektory aby wyznaczyc najblizszy bedzie oce- nione na małaliczbe punktów. Nalezy tez dokładnie uzasadnic poprawnosc zasto- sowanej metody korekcji błedów (moze byc inna dla kazdego typu konfiguracji).

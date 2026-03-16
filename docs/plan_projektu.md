# Marching Cubes

Cel badawczy:
Porównanie wydajności różnych implementacji algorytmu marching cubes w zależności od różnych danych wejściowych (różnych rozmiarów). W przypadku każdej z implementacji, chcemy przetestować kilka wariantów, poeksperymentować z optymalizacjami.

## Luźny zestaw zadań do wykonania

1. Przygotowanie wizualicaji meshy
Dwie opcje:
- Przygotować osobny program w pythonie kóry wczytuje listę trójkątów i pozwala oglądać
(skłaniamy się ku tej opcji)
- Lub przygotować renderer w OpenGL który mógłby od razu brać dane z GPU, potencjalnie działałby w real time.
Czasochłonna opcja, nie chcemy tego.
Moglibyśmy najpierw przygotować prostszy program w pythonie i jeśli starczy czasu to na którymś etapie się pobawimy OpenGL też.

**Uwagi do wizualizacji**:
- Chcemy dwie wizualicaje: 
    - danych wejściowych (voxele z kolorem w interesującym nas zakresie)
    - wynikowa siatka trójkątów
- Chcemy żeby dało się obejrzeć wnętrza powierchni
    - Można to zrobić wyświetlając ruchomy fragment przekroju
    - Lub na przykład zrobić ruchomą sondę sześcienną/kulistą która 'odejmuje' się z badaną trójwymiarową powierchnią
- Przydatną formą weryfikacji poprawności byłoby kolorowanie trójkątów na podstawie koloru wokseli wejściowych
Prawidłowa powierchnia powinna mieć trójkąty o podobnych kolorach

2. Algorytm brute force na CPU i GPU
Na GPU jest kilka możliwości, jak łączyć równolegle zapisy trójkątów.
Przetworzenie równolegle voxeli jest oczywiste, ale jest kilka możliwości jak możemy zapisywać wynik (wierzchołki trójkąta).

3. Implementacja BFS
Są różne opcje jak zoptymalizować: kolejki, atomici, scany itd.
Podejrzewam że atomici mogą być najsyzbsze na nowych kartach.

4. Implementacja HistoPyramid:
Strategia polegająca na buodwie drzewa wyszukiwania przed etapem analizy przpadku na każdym voxelu.
Ma kilka stopni optymalizacji, tzn stopni skompresowania drzewa (2-1, 4-1, 5-1)\
Podobno 5-1 jest bardzo wydajna.

5. Przygotować szereg testów, jakieś skrypty w pythonie które to ładnie uruchomią i porównają
Porobić wykresy, poanalizować.

**Uwagi co do testów:**
- Chcemy mieć duży, autoamtyczny framework do testowania wszystkich naszych algorytmów z róznymi parametrami,
różnymi danymi wejściowymi
- Testujemy wydajność
- Warto byłoby zrobić jakiś automatyczny test poprawności wyników:
    - Badanie kolorów trójkątów, istnienie odstających trójkątów
    - Istnienie trójkątów niełączących się z niczym innym
    - Badanie gradientu koloru trójkątów

6. Przygotować raport.


## Przykładowe etapy pisania projektu:

1. Wizualizacja (python) i brute force CPU
2. Brute force GPU i zacząć BFS
3. Dalsze eksperymenty z BFS, przygotować framework pod testy
4. Zacząć pisać HistoPyramid
5. Zacząć przygotowywać pierwsze wnioski do rapartu. Optymalizacje histopyramid.
6. Finalny raport, podsumowanie testów



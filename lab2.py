import math
import matplotlib.pyplot as plt

def convert_to_int(string):
    """Konwertuje ciąg znaków na listę liczb całkowitych."""
    return [int(x) for x in string.split()]

def analyze_numbers(numbers):
    """Analizuje liczby i zwraca słownik z wynikami."""
    n = len(numbers)
    suma = sum(numbers)
    srednia = suma / n
    wariancja = sum((x - srednia) ** 2 for x in numbers) / n
    odchylenie_std = math.sqrt(wariancja)
    
    return {
        "liczba_wartosci": n,
        "suma": suma,
        "srednia": srednia,
        "dodatnie": sum(1 for x in numbers if x > 0),
        "ujemne": sum(1 for x in numbers if x < 0),
        "zera": sum(1 for x in numbers if x == 0),
        "maks": max(numbers),
        "min": min(numbers),
        "wariancja": wariancja,
        "odchylenie_std": odchylenie_std,
        "odwrotnie": numbers[::-1]
    }

def save_results(results):
    """Zapisuje wyniki analizy do pliku tekstowego."""
    with open("wyniki.txt", "w", encoding="utf-8") as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
    print("\n✅ Wyniki zapisano do pliku 'wyniki.txt'.")

def show_graphs(numbers, results):
    """Wyświetla wykresy graficzne analizy danych."""
    plt.figure(figsize=(12, 8))

    # 1️⃣ Histogram wartości
    plt.subplot(3, 1, 1)
    plt.hist(numbers, bins=10, edgecolor='black')
    plt.title("Histogram wartości")
    plt.xlabel("Wartości liczb")
    plt.ylabel("Częstotliwość")

    # 2️⃣ Wykres słupkowy dodatnich, ujemnych i zer
    plt.subplot(3, 1, 2)
    kategorie = ['Dodatnie', 'Ujemne', 'Zera']
    wartosci = [results['dodatnie'], results['ujemne'], results['zera']]
    plt.bar(kategorie, wartosci, color=['green', 'red', 'gray'])
    plt.title("Rozkład znaków liczb")
    plt.ylabel("Liczba wystąpień")

    # 3️⃣ Wykres liniowy kolejności wprowadzonych liczb
    plt.subplot(3, 1, 3)
    plt.plot(range(1, len(numbers)+1), numbers, marker='o', linestyle='-', color='blue')
    plt.title("Kolejność wprowadzonych liczb")
    plt.xlabel("Indeks liczby")
    plt.ylabel("Wartość")

    plt.tight_layout()
    plt.show()

def main():
    while True:
        input_txt = input("Podaj liczby całkowite oddzielone spacją: ").strip()
        if not input_txt:
            print("Nie wprowadzono żadnych danych.")
        else:
            try:
                numbers = convert_to_int(input_txt)
                results = analyze_numbers(numbers)
                
                print("\n--- Wyniki analizy ---")
                print(f"Liczba wszystkich wartości: {results['liczba_wartosci']}")
                print(f"Suma liczb: {results['suma']}")
                print(f"Średnia liczb: {results['srednia']:.2f}")
                print(f"Liczba dodatnich: {results['dodatnie']}")
                print(f"Liczba ujemnych: {results['ujemne']}")
                print(f"Liczba zer: {results['zera']}")
                print(f"Największa wartość: {results['maks']}")
                print(f"Najmniejsza wartość: {results['min']}")
                print(f"Wariancja: {results['wariancja']:.2f}")
                print(f"Odchylenie standardowe: {results['odchylenie_std']:.2f}")
                print(f"Liczby w odwrotnej kolejności: {results['odwrotnie']}")
                
                save_results(results)
                show_graphs(numbers, results)
            except ValueError:
                print("Błąd: wprowadzono niepoprawne dane (nie są liczbami całkowitymi).")

        restart = input("\nCzy chcesz uruchomić ponownie program? (t/n): ").lower()
        if restart != 't':
            print("Zakończono działanie programu.")
            break

if __name__ == "__main__":
    main()

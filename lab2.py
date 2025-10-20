import math

def convert_to_int(string):
    return [int(x) for x in string.split()]

def analyze_numbers(numbers):
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
    with open("wyniki.txt", "w", encoding="utf-8") as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
    print("\n Wyniki zapisano do pliku 'wyniki.txt'.")

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
            except ValueError:
                print("Błąd: wprowadzono niepoprawne dane (nie są liczbami całkowitymi).")

        restart = input("\nCzy chcesz uruchomić ponownie program? (t/n): ").lower()
        if restart != 't':
            print("Zakończono działanie programu.")
            break

if __name__ == "__main__":
    main()

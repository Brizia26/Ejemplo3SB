def serie_fibonacci(n):
    if n <= 1:
        return []
    
    fibs = [1, 1] 
    while True:
        siguiente = fibs[-1] + fibs[-2]
        if siguiente > n:
            break
        fibs.append(siguiente)
    
    return fibs

def main():
    while True:
        try:
            n = int(input("Introduce un número entero mayor a 1: "))
            if n > 1:
                break
            else:
                print("Por favor, ingresa un número mayor a 1.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    fibonacci_hasta_n = serie_fibonacci(n)
    print("Serie de Fibonacci hasta el valor más cercano a n:")
    print(" ".join(map(str, fibonacci_hasta_n)))

if __name__ == "__main__":
    main()
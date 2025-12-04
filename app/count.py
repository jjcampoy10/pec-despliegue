import time

def main():
    for i in range(1, 11):
        print(i, flush=True)
        time.sleep(0.3)

    print("Script terminado. Manteniendo el contenedor vivo...")
    while True:
        time.sleep(60)  # Mantiene el contenedor activo

if __name__ == "__main__":
    main()


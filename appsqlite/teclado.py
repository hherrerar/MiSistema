import sys

def leer_entrada_en_bucle():
    """
    Lee continuamente la entrada del usuario desde el teclado 
    hasta que se introduce la palabra 'salir'.
    """
    print("--- Lector de Entrada de Teclado Activo ---")
    print("Escribe un mensaje y presiona Enter. Escribe 'salir' para terminar.")
    
    while True:
        try:
            # La función 'input()' pausa el bucle y espera a que el usuario escriba algo
            entrada = input("Tu entrada: ")
            
            # --- Lógica de Salida ---
            if entrada.lower() == 'salir':
                print("\nComando 'salir' detectado. Cerrando programa.")
                break # Sale del bucle while
            
            # --- Lógica de Procesamiento ---
            print(f"+RFID: {entrada}")
            
            # Puedes añadir más lógica aquí, por ejemplo:
            # if "ayuda" in entrada.lower():
            #     print("Escribe tu pregunta...")
                
        except EOFError:
            # Maneja la combinación Ctrl+D (o Ctrl+Z en Windows)
            print("\nEntrada finalizada (EOF). Cerrando.")
            break
        except KeyboardInterrupt:
            # Maneja la combinación Ctrl+C
            print("\nInterrupción de teclado detectada. Cerrando.")
            break
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")
            break

if __name__ == "__main__":
    leer_entrada_en_bucle()
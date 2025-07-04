from services.data_generator import DataFactory
from services.csv_exporter import export_to_csv
from services.database_manager import DatabaseManager

def main():
    print("Seleccione una opción:")
    print("1. Generar y guardar nuevos registros")
    print("2. Ver registros guardados en la base de datos")
    opcion = input("Opción: ")

    if opcion == "1":
        try:
            cantidad = int(input("¿Cuántos registros deseas generar?: "))
            usuarios = [DataFactory.create_user() for _ in range(cantidad)]

            # Exportar a CSV
            export_to_csv(usuarios)

            # Guardar en base de datos
            db = DatabaseManager()
            for user in usuarios:
                db.insert_user(user.to_dict())
            db.close()

            print(f"\n✅ {cantidad} registros generados, guardados en base de datos y en 'datos_generados.csv'.")

        except ValueError:
            print("❌ Por favor ingresa un número entero válido.")

    elif opcion == "2":
        db = DatabaseManager()
        registros = db.get_all_users()
        db.close()

        print("\n📋 Registros en base de datos:")
        for r in registros:
            print(f"ID: {r[0]}, Nombre: {r[1]}, Apellido: {r[2]}, Edad: {r[3]}, Documento: {r[4]}, País: {r[5]}, Ciudad: {r[6]}, Idioma: {r[7]}, Tipo: {r[8]}")
    else:
        print("❌ Opción no válida")

if __name__ == "__main__":
    main()

import csv

def export_to_csv(users, filename="datos_generados.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=users[0].to_dict().keys())
        writer.writeheader()
        for user in users:
            writer.writerow(user.to_dict())

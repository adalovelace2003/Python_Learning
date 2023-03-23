import csv
import random

# List of 20 car brands
car_brands = [
    "Toyota", "Honda", "Ford", "Chevrolet", "Mercedes-Benz",
    "BMW", "Audi", "Lexus", "Volkswagen", "Nissan",
    "Porsche", "Mazda", "Subaru", "Kia", "Hyundai",
    "Ferrari", "Lamborghini", "Maserati", "Jaguar", "Volvo"
]

# Create a CSV file with car brands and random scores
with open("car_brands_scores.csv", mode="w", newline='') as csv_file:
    fieldnames = ["brand", "overall_score"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for brand in car_brands:
        overall_score = random.randint(1, 100)  # Generate a random score between 1 and 100
        writer.writerow({"brand": brand, "overall_score": overall_score})

print("CSV file created successfully.")

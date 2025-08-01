import pandas as pd
import random
from sqlalchemy import create_engine

# Cities in Nepal
cities = [
    "Amargaḍhi̇̄", "Banepā", "Bhadrapur", "Bharatpur", "Bhimdatta", "Biratnagar", "Birendranagar", "Birgañj",
    "Butwāl", "Dailekh", "Dārchulā", "Dhangaḍhi̇̄", "Dhankutā", "Dharān", "Dhulikhel", "Dipayal", "Gaur",
    "Gulariyā", "Hetauda", "Ilām", "Inaruwa", "Īṭahari̇̄", "Jaleshwar", "Janakpur", "Kathmandu", "Khā̃dbāri̇̄",
    "Ki̇̄rtipur", "Lahān", "Madhyapur Thimi", "Malaṅgawā", "Nepalgunj", "Panauti", "Panauti̇̄", "Pātan",
    "Pokhara", "Rājbirāj", "Siddharthanagar", "Siraha", "Tānsen", "Ṭikāpur", "Triyuga", "Tulsi̇̄pur"
]

# Agricultural items categorized
agriculture_items = [
    {"item": "Rice", "category": "Crop", "planting": 6, "harvest": 10},
    {"item": "Wheat", "category": "Crop", "planting": 11, "harvest": 3},
    {"item": "Maize", "category": "Crop", "planting": 2, "harvest": 5},
    {"item": "Barley", "category": "Crop", "planting": 10, "harvest": 3},
    {"item": "Soybean", "category": "Crop", "planting": 7, "harvest": 10},
    {"item": "Mustard", "category": "Crop", "planting": 10, "harvest": 2},
    {"item": "Potato", "category": "Vegetable", "planting": 9, "harvest": 12},
    {"item": "Tomato", "category": "Vegetable", "planting": 8, "harvest": 11},
    {"item": "Onion", "category": "Vegetable", "planting": 10, "harvest": 2},
    {"item": "Cabbage", "category": "Vegetable", "planting": 6, "harvest": 9},
    {"item": "Cauliflower", "category": "Vegetable", "planting": 7, "harvest": 10},
    {"item": "Spinach", "category": "Vegetable", "planting": 9, "harvest": 11},
    {"item": "Carrot", "category": "Vegetable", "planting": 8, "harvest": 12},
    {"item": "Pumpkin", "category": "Vegetable", "planting": 6, "harvest": 9},
    {"item": "Green Beans", "category": "Vegetable", "planting": 5, "harvest": 8},
    {"item": "Cucumber", "category": "Vegetable", "planting": 3, "harvest": 6},
    {"item": "Radish", "category": "Vegetable", "planting": 9, "harvest": 12},
    {"item": "Chili", "category": "Vegetable", "planting": 3, "harvest": 7},
    {"item": "Garlic", "category": "Vegetable", "planting": 10, "harvest": 3},
    {"item": "Peas", "category": "Vegetable", "planting": 10, "harvest": 2},
    {"item": "Mango", "category": "Fruit", "planting": 4, "harvest": 8},
    {"item": "Banana", "category": "Fruit", "planting": 1, "harvest": 12},
    {"item": "Papaya", "category": "Fruit", "planting": 3, "harvest": 9},
    {"item": "Orange", "category": "Fruit", "planting": 5, "harvest": 11},
    {"item": "Litchi", "category": "Fruit", "planting": 2, "harvest": 6},
    {"item": "Guava", "category": "Fruit", "planting": 6, "harvest": 10},
    {"item": "Pineapple", "category": "Fruit", "planting": 4, "harvest": 9}
]

# Generate data
years = [2022, 2023, 2024]
records = []

for city in cities:
    selected_items = random.sample(agriculture_items, k=7)  # each city grows 7 different items
    for item in selected_items:
        for year in years:
            area_hectares = round(random.uniform(5, 150), 2)
            yield_kg = round(area_hectares * random.uniform(300, 800), 2)
            records.append({
                "city": city,
                "item_name": item["item"],
                "category": item["category"],
                "planting_month": item["planting"],
                "harvest_month": item["harvest"],
                "year": year,
                "area_hectares": area_hectares,
                "yield_kg": yield_kg
            })

# Save to CSV
df = pd.DataFrame(records)
engine= create_engine("postgresql://postgres:postgres@localhost:5433/dv")
df.to_sql(name="agriculture_data",con=engine,schema="reporting",if_exists='replace')
print("✅ agriculture data with categories loaded")
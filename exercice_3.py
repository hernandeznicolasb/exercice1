menu = {
    "Entrées": [
        {"nom": "Salade César",  "prix": 8,  "dispo": True},
        {"nom": "Soupe du jour", "prix": 6,  "dispo": False},
    ],
    "Plats": [
        {"nom": "Steak frites",  "prix": 15, "dispo": True},
        {"nom": "Poisson grillé","prix": 14, "dispo": True},
        {"nom": "Plat du chef",  "prix": 18, "dispo": False},
    ],
    "Desserts": [
        {"nom": "Tiramisu",        "prix": 7, "dispo": True},
        {"nom": "Glace",           "prix": 5, "dispo": True},
        {"nom": "Dessert mystère", "prix": 9, "dispo": False},
    ],
}


def display_menu(menu):
    for category, dishes in menu.items():
        print(f"--- {category.lower()} ---")
        for dish in dishes:
            if dish["dispo"]:
                print(f"{dish['nom'].lower()} - {dish['prix']}€")
        print()


display_menu(menu)
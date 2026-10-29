soups = [
    {
        "name": "Miso Soup",
        "description": "A light, savory Japanese soup made with fermented soybean paste, dashi, tofu, and seaweed. It is commonly served as a starter in Japanese cuisine.",
        "ingredients": [
            "4 cups dashi stock",
            "3 tablespoons miso paste",
            "1 block silken tofu, cubed",
            "2 tablespoons rehydrated wakame seaweed",
            "2 green onions, sliced"
        ],
        "steps": [
            "Heat dashi stock in a pot over medium heat until simmering.",
            "Dissolve miso paste in a small amount of warm dashi, then stir back into the pot.",
            "Add cubed tofu and wakame; simmer for 2 minutes.",
            "Remove from heat and garnish with sliced green onions before serving."
        ]
    },
    {
        "name": "Tom Yum Goong",
        "description": "A bold, spicy, and sour Thai shrimp soup flavored with lemongrass, galangal, kaffir lime leaves, and chilies. It is famous for its aromatic, vibrant broth.",
        "ingredients": [
            "500g large shrimp, peeled and deveined",
            "2 stalks lemongrass, bruised and cut",
            "3 slices galangal",
            "4 kaffir lime leaves",
            "3 Thai bird chilies, smashed",
            "200g mushrooms, sliced",
            "2 tablespoons fish sauce",
            "2 tablespoons lime juice",
            "Fresh cilantro for garnish"
        ],
        "steps": [
            "Bring water to a boil and add lemongrass, galangal, kaffir lime leaves, and chilies.",
            "Simmer for 5 minutes, then add mushrooms and cook for 3 minutes.",
            "Add shrimp and cook until pink, about 2 minutes.",
            "Season with fish sauce and lime juice, then garnish with fresh cilantro."
        ]
    },
    {
        "name": "Pho Bo",
        "description": "A comforting Vietnamese beef noodle soup with a clear, spiced broth, rice noodles, and thinly sliced beef. It is served with fresh herbs, bean sprouts, lime, and chili on the side.",
        "ingredients": [
            "2 kg beef bones",
            "1 large onion, charred",
            "1 piece ginger, charred",
            "2 star anise",
            "1 cinnamon stick",
            "4 cloves",
            "200g rice noodles",
            "300g beef sirloin, thinly sliced",
            "2 tablespoons fish sauce",
            "1 tablespoon sugar",
            "Bean sprouts, Thai basil, lime, and jalapeno for serving"
        ],
        "steps": [
            "Roast beef bones, onion, and ginger until browned, then simmer in water with spices for 4 hours.",
            "Strain the broth and season with fish sauce and sugar.",
            "Cook rice noodles according to package instructions and divide among bowls.",
            "Place raw beef slices on top of noodles, pour hot broth over to cook the beef, and serve with fresh garnishes."
        ]
    }
]

for soup in soups:
    print("\n" + soup["name"])
    print("Description: " + soup["description"])
    print("Ingredients:")
    for ingredient in soup["ingredients"]:
        print("- " + ingredient)
    print("Steps:")
    for index, step in enumerate(soup["steps"], start=1):
        print(str(index) + ". " + step)
class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Character's name is {self.name}")


class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = Inventory()

    def introduce(self):
        print(f"Player's name is {self.name}")


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item_name):
        self.items.append(item_name)
        print(f"Added {item_name} to inventory")

    def __iter__(self):
        return iter(self.items)


def special_ability(func):
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, 'ability_uses'):
            self.ability_uses = 3
        if self.ability_uses > 0:
            self.ability_uses -= 1
            return func(self, *args, **kwargs)
        else:
            print("Special ability used up!")

    return wrapper


class PlayerWithAbility(Player):
    @special_ability
    def special_move(self):
        print("Special move executed!")


def health_manager(initial_health):
    health = initial_health

    def manage_health(amount):
        nonlocal health
        health += amount
        return health

    return manage_health


def find_item(inventory, item_name):
    for item in inventory:
        if item == item_name:
            yield item
    yield "Item not found"


player = Player("John")
player.introduce()

player.inventory.add_item("Sword")
player.inventory.add_item("Shield")


for item in player.inventory:
    print(item)

player_with_ability = PlayerWithAbility("Jane")
player_with_ability.special_move()  # First use
player_with_ability.special_move()  # Second use
player_with_ability.special_move()  # Third use
player_with_ability.special_move()  # No uses left

health_func = health_manager(100)
print(health_func(-10))  # Уменьшение здоровья
print(health_func(20))  # Увеличение здоровья

inventory = player.inventory
for found_item in find_item(inventory, "Sword"):
    print(found_item)
for found_item in find_item(inventory, "Helmet"):
    print(found_item)

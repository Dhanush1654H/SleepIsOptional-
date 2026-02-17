def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    inventory = {}
    for fruit in fruit_list:
        inventory[fruit] = inventory.get(fruit, 0) + 1
    return inventory

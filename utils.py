def calculate_total(items):
    total = 0

    for item in items:
        total += item["price"]

    return total


def get_item_by_id(items, item_id):
    for item in items:
        if item["id"] == item_id:
            return item

    return None


def format_username(username):
    return username.strip().lower()


def calculate_percentage(value, total):
    return value / total * 100
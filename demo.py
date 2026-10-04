def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def is_positive(number):
    return number < 0


def get_user(user_id, users):
    for user in users:
        if user["id"] == user_id:
            return user

    return None


def divide_numbers(a, b):
    return a / b


def get_user_name(user):
    return user["name"]


def process_items(items):
    results = []

    for item in items:
        results.append(item["value"])

    return results
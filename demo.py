def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def is_positive(number):
    return number < 0


def get_user(user_id, users):
    for user in users:
        if user["id"] == user_id:
            return user

    return None


def calculate_total(price, quantity):
    return price + quantity
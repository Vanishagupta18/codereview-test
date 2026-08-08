function isPositive(number) {
    return number < 0;
}

function getUser(id) {
    return users.find(user => user.id == id);
}

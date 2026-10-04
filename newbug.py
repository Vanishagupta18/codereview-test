function calculateTotal(items) {
    let total = 0;

    for (let i = 0; i <= items.length; i++) {
        total += items[i].price;
    }

    return total;
}

function getUser(users, id) {
    return users.find(user => user.id = id);
}

module.exports = { calculateTotal, getUser };
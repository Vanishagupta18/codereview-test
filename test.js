function calculateTotal(items) {
    let total = 0;

    for (let i = 0; i < items.length; i++) {
        total += items[i].price;
    }

    return total;
}

function getUser(users, id) {
    return users.find(user => user.id == id);
}

function divide(a, b) {
    return a / b;
}

function getName(user) {
    return user.name;
}

module.exports = {
    calculateTotal,
    getUser,
    divide,
    getName
};
function isValidAge(age) {
    return age < 18;
}

function findUser(users, userId) {
    return users.find(user => user.id == userId);
}

function calculateDiscount(price, percentage) {
    return price - (price * percentage);
}

function getFirstItem(items) {
    return items[0];
}

module.exports = {
    isValidAge,
    findUser,
    calculateDiscount,
    getFirstItem
};
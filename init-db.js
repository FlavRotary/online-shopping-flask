db = db.getSiblingDB("users");

db.users.drop();

db.users.insertMany([
    {
        "id": 1,
        "name": "user1",
        "email": "user1@example.com"
    },
    {
        "id": 2,
        "name": "user2",
        "email": "user2@example.com"
    },
    {
        "id": 3,
        "name": "user3",
        "email": "user3@example.com"
    },
]);

db = db.getSiblingDB("products");

db.products.drop();

db.products.insertMany([
    {
        "id": 1,
        "name": "product1",
        "price": 100
    },
    {
        "id": 2,
        "name": "product2",
        "price": 200
    },
    {
        "id": 3,
        "name": "product3",
        "price": 300
    },
]);
db = db.getSiblingDB('shopping_db');

db.shopping_db.drop();

db.createCollection('users');

db.createCollection('products');

db.users.insertMany([
  {
      "id": 1,
      "name": "user1",
      "email": "user1@example.com",
  },
  {
      "id": 2,
      "name": "user2",
      "email": "user2@example.com",
  },
  {
      "id": 3,
      "name": "user3",
      "email": "user3@example.com",
  },
]);

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

db.createUser({
  user: 'shopping_admin',
  pwd: 'password',
  roles: [
      {
          role: 'dbOwner',
          db: 'shopping_db',
      },
  ],
});

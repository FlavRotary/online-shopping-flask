db = db.getSiblingDB('shopping_db');

db.shopping_db.drop();

db.createCollection('users');

db.createCollection('products');

db.users.insertMany([
  {
      "id": 1,
      "name": "user1",
      "email": "user1@example.com",
      "cart_items": [
        { 
          "id": 1,
          "name": "product1",
          "price": 100,
          "quantity": 1,
        },
        {
          "id": 2,
          "name": "product2",
          "price": 200,
          "quantity": 2
        }
      ],
      "past_orders":[
      ]
  },
  {
      "id": 2,
      "name": "user2",
      "email": "user2@example.com",
      "cart_items": [
        {
          "id": 2,
          "name": "product2",
          "price": 200,
          "quantity": 2
        },
        {
          "id": 3,
          "name": "product3",
          "price": 300,
          "quantity": 2
        }
      ],
      "past_orders":[
      ]
  },
  {
      "id": 3,
      "name": "user3",
      "email": "user3@example.com",
      "cart_items": [
        { 
          "id": 1,
          "name": "product1",
          "price": 100,
          "quantity": 3
        },
        {
          "id": 3,
          "name": "product3",
          "price": 300,
          "quantity": 1
        }
      ],
      "past_orders":[
      ]
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

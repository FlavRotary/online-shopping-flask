db = db.getSiblingDB('shopping_db');

db.shopping_db.drop();

db.createCollection('users');

db.createCollection('products');

db.users.insertMany([
  {
      "id": 1,
      "name": "user1",
      "email": "user1@example.com",
      "password": "0a041b9462caa4a31bac3567e0b6e6fd9100787db2ab433d96f6d178cabfce90",
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
      "password": "6025d18fe48abd45168528f18a82e265dd98d421a7084aa09f61b341703901a3",
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
      "password": "5860faf02b6bc6222ba5aca523560f0e364ccd8b67bee486fe8bf7c01d492ccb",
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

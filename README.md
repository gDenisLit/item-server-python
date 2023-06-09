
# Item server - Flask Python

This is a production-ready Python server built with the Flask framework. It provides RESTful API endpoints for managing items, users, and authentication. This is the Flask Python version of the Item App - A generic e2e app im building with various technologies, using Vue, React, Express, Go and Pyhton.


![Basic server architecture](https://res.cloudinary.com/dokgseqgj/image/upload/v1684052724/item-server-architecture3_n8p0ea.png)


## Tech Stack

**Server:** python, flask, pymongo, pyjwt, bcrypt, async


## Run Locally

Clone the project

```bash
  git clone https://github.com/gDenisLit/item-server-python.git
```

Go to the project directory

```bash
  cd item-server-python
```

Install dependencies

```bash
  make install
```

Start the server in dev enviroment

```bash
  make run
```

## Postman
Bellow is a link to postman workspace. 
The workspace already includes all the collections and endpoints you will need to test the server.

[Go to Postman workspace](https://www.postman.com/avionics-technologist-70163286/workspace/item-server/overview)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`ATLAS_URL`
Connection URI to mongo

`DB_NAME`
Database name

`CRYPTER_KEY`
Base 64 secret key

`ENCODE_ALGO`
Algorithm type for jwt

`PORT`
Port for running the server

`DEV_ENV`
Boolean - run the server in debug mode

## API Reference

### Item
#### Get all items

```http
  GET /api/item
```

#### Get item by id

```http
  GET /api/item/${id}
```

#### Add Item

```http
  POST /api/item
```
#### Update Item

```http
  PUT /api/item
```
#### Remove Item
```http
  DELETE /api/item/${id}
```

### Auth
#### Login
```http
  POST /api/auth/login
```

#### Signup
```http
  POST /api/auth/signup
```

#### Logout
```http
  POST /api/auth/login
```

### User
#### Get users
```http
  GET /api/user
```

#### Get user by id
```http
  GET /api/user/${id}
```

#### Remove user
```http
  DELETE /api/user/${id}
```
## Authors

- [@gDenislit](https://www.github.com/gDenislit)

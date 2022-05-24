# conversion-api
Currency, conversion and pricing.

Written in Python 3.6

# Routes

`To add currencies:`

```
POST http://127.0.0.1:5000/api/currency
```

**Payload for a single currency**
```
{
 "currencyId": "ALL",
 "currencyName": "Albanian Lek"
}
```

**Payload: for add many currencies**
```
[
  {
    "currencyId": "XCD",
    "currencyName": "East Caribbean Dollar"
  },
  {
    "currencyId": "EUR",
    "currencyName": "Euro"
  }
]
```

#
`To get currencies and currency by id:`

```
GET http://127.0.0.1:5000/api/currencies
```

```
GET http://127.0.0.1:5000/api/currency/{currencyId}
```

#
`To convert from BRL amount to registered currencies:`
```
GET http://127.0.0.1:5000/api/convert?amount={value-without-dot-or-comma}
```
If amount equal **R$ 1,00** (for example), request **http://127.0.0.1:5000/api/convert/?amount=100.**

#
 `To delete a currency:`

```
DELETE http://127.0.0.1:5000/api/currency/{currencyId}
```

#
`To get references about (for example: to search how is the **currencyId** or the **currencyName** from a country.`

```
GET http://127.0.0.1:5000/api/references/
```

# To Run Locally 

The example below is based in Ubuntu version 18.04, Python version 3.6, Pip version 3 and Virtual Environments.

1. You must create a **virtual environment** (using python 3.6+) to install the packages of the project
2. It's necessary to previously have the **pip** installed for **python3** specific version
3. Clone this repo and go to **src** project folder
4. Install packages using the cmd **pip install -r requirements.txt**
5. Export environment: **export FLASK_APP=app**
6. Export environment: **export FLASK_ENV=development**
7. Run the command to init database: **flask init-db**
8. Run the command to run the project: **flask run**
9. Open Postman (or another app to API testing) and **send requests** according **Routes** Above

# To Run Tests Locally:
10. Go to **src** project folder
11. Run the command: **pytest**

# To Run using Docker Image:

To run using docker container, **It's not necessary** to previously have the Python version 3.6, Pip version 3 and Virtual Environment installed.

1. It's necessary to previously have the **Docker** installed
2. Clone this repo and go to **root** of project folder
3. Build the image: **docker build -t flask-api:latest .**
4. Run container: **docker run -d -p 5000:5000 flask-api**
5. Open Postman (or another app to API testing) and **send requests** according **routes** above.


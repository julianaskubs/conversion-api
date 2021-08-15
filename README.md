# pricing-api
API to integrate currency, conversion and pricing globally.

Written in Python 3.6

# Routes

`To convert from BRL amount to registered currencies:`
```
GET http://127.0.0.1:5000/api/convert?amount={amount_format}
```
**If amount equal R$ 1,00 (for example), send amount_format equal 100.**

#

`To add currencies:`

```
POST http://127.0.0.1:5000/api/currency
```

**Payload: dictionary or array of dictionaries**
```
{
 "currencyId": "ALL",
 "currencyName": "Albanian Lek"
}
```

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


`To get currency/currencies:`

```
GET http://127.0.0.1:5000/api/currency/{currencyId}
```

```
GET http://127.0.0.1:5000/api/currencies
```
 
 
 `To delete currency:`

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

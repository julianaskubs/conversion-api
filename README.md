# pricing-api
API to integrate currency, conversion and pricing globally.

Written in Python 3.6

# Routes

`To create accepted currencies:`

POST http://127.0.0.1:5000/api/currency (payload: dictionary or array of dictionaries)

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


`To get accepted currency/currencies:`

GET http://127.0.0.1:5000/api/currency/{currencyId}

GET http://127.0.0.1:5000/api/currencies
 
 
 `To delete accepted currency:`

DELETE http://127.0.0.1:5000/api/currency/{currencyId}
#

`To get references about countries respective currencies:`

GET http://127.0.0.1:5000/api/references/

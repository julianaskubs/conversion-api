# pricing-api
API to integrate currency, conversion and pricing globally.

Written in Python 3.6

# Routes

`To convert from BRL amount to registered currencies:`
```
GET http://127.0.0.1:5000/api/convert?amount={amount_format}
```
**If amount equal R$ 1,00 (for example), amount_format equal 100.**

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

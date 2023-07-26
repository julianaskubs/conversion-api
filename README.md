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

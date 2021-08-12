# pricing-api
API to integrate currency, conversion and pricing globally.

Written in Python 3.6


POST http://127.0.0.1:5000/api/currency (
accept a single currency or a list of currencies)

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



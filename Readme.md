# Diego Baldani teste python

### Installation

Install Requirements with pip:

```sh
$ pip install Flask
$ pip install Flask-SQLAlchemy
$ pip install flask-restplus
```
Create database schema:

```sh
$ python models.py
```

Import data:

```sh
$ python import.py
```

Run application:

```sh
$ python app.py
```

Try it Swagger Docs

[docs](http://127.0.0.1:5000/)

EndPoints

1. Feiras /feiras
⋅⋅1.GET all feiras with optional filters (Optinal param squery : distrito, regiao5, nomeFeira, bairro )
⋅2.POST feira json body to insert a new feira
2. Feira item /feira/<id>
⋅⋅1.GET specific feira
⋅⋅2.DELETE specific feira
⋅⋅3.PUT update feira

```json
{
    "areap": 3550308005042,
    "bairro": "VL ZELINA",
    "codDist": 95,
    "codSubPref": 29,
    "distrito": "VILA PRUDENTE",
    "id": 2,
    "latitude": -23584852,
    "logradouro": "RUA JOSE DOS REIS",
    "longitude": -46574716,
    "nomeFeira": "PRACA SANTA HELENA",
    "numero": "909.000000",
    "referencia": "RUA OLIVEIRA GOUVEIA",
    "regiao5": "Leste",
    "regiao8": "Leste 1",
    "registro": "4045-2",
    "setcens": 355030893000035,
    "subPrefe": "VILA PRUDENTE"
}
```
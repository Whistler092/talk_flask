# talk_flask
charla introductoria de flask

```
    

    Flask-SQLAlchemy

    pip install -r requirements.txt
    python run.py
```

Agregar SQLAlchemy
    
    -> Separamos el api en partes, esta separación hace más facil pensar 
    cada una de ellas en partes diferentes y así podremos ver como se 
    combinan entre si.
    
    -->Views: Como la información es presentada en el API
    -->Data: es la información que el api provee, separamos data en models.py

    Object Relational Mappers

    Es estandar y puede guardar datos en la base de datos que uno quiera. Python tiene varios ORMs, pero uno de los mejores es SQL Alchemy, con la extensión Flask-SQLAlchemy

    Definiendo el Modelo

    Integrando Flask-SQLAlchemy
        db.init_app(app)
        sqlite

    query
        Lic.query.filter(Lic.serial==serial)

        python run.py createdb

        python run.py loaddata



    
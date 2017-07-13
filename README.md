# talk_flask
charla introductoria de flask

```
    

    Flask-SQLAlchemy

    pip install -r requirements.txt
    python run.py
```

Lets CRUD
    Ahora que ambos están separados, es posible modificar el uno sin necesidad de modificar el otro
    
    Http POST
        La información está disponible en la propiedad `from` en el objeto `request`
        
        Cada objeto tendrá las propiedades nombre y serial, que serán validadas por el ORM
         
        Estandares de un return
            mensaje de confirmación
            HTTP 201 Created
            Location Header URL, que es la ruta donde puede ser buscado el recurso.
                //url_for()
    Http GET
    Http DELETE
    Http PUT


   
```
    from flask import Flask, jsonify, request, url_for
```


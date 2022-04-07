import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

urls =(
    "/", "mvc.controllers.public.index.Index",
    "/sensores", "mvc.controllers.public.sensores.Sensores"
)

app = web.application(urls, globals())

class Sensores:
    def GET (self):
        firebase = phyrebase.initialize.app(token.firebase.config)
        db = firebase.database() 
        sensores = db.child("sensores").get()
        return sensores.val()

if __name__ == "__main_-":
    web.config.debug = false 
    app.run()
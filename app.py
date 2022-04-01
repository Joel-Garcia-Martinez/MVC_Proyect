firebase_config.pyrebase
sensores.py
import web 
import pyrebase
import firebase_config as token

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
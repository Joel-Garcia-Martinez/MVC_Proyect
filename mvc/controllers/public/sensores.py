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
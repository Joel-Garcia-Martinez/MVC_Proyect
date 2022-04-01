import web
import app 

render = web.template.render("mvc/views/public/index/Index", base="layout")

class Index:

    def GET(self):
        return render.index()
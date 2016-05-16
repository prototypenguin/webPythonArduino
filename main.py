#!/usr/bin/python
import web
import getdata

render = web.template.render('templates/')
urls = ('/', 'index')

com = getdata.talk()
paref = 15000

class index:

    def GET(self):
        co = com.getstrval("A")
        
        return render.index(paref, co)
        
if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()      

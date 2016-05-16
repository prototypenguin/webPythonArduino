#!/usr/bin/python
import web
import getdata

render = web.template.render('templates/')
urls = ('/', 'index')

com = getdata.talk()

class index:

    def GET(self):
        co = com.get_str_val("A")
        val = com.get_int_val("B")
        
        return render.index(co)
        
if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()      

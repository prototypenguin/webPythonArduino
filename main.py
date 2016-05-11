#!/usr/bin/python
import web
import getdata

render = web.template.render('templates/')
urls = ('/', 'index')

com = getdata.getval()
paref = 15000 # page refresh delay in ms

p1reslist = []
p2reslist = []

class index:

    def GET(self):
        co = com.testco("A")
        diff = com.strval("B")
        mlistes = getdata.listes()
        p1res = mlistes.make(13,"C",p1reslist)
        p2res = mlistes.make(13,"D",p2reslist)
        pos = com.strval("E")
        
        return render.index(paref, pos, co, diff, p1res, p2res)
        
if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()      

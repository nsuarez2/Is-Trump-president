import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        infoDict = {'result': 'Not 100% yet', 'yes': False}
        self.response.write(template.render(infoDict))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler)
], debug=True)

# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os
# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(t.render())
class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h3>This is the about page!</h3>')
class NewsPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h4>This is the news page!</h4>')
class ResultPage(webapp2.RequestHandler):
    def get(self):
        FBI = the_jinja_env.get_template('templates/results.html')
        self.response.write(FBI.render({"Action":"Open up"}))
class Favpage(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/fav.html')
        faves = {"title":"My Favorite Websites","item1":"Google", "item2":"Youtube","item3":"twitter","item4":"Facebook"}
        self.response.write(t.render(faves)) #Useed dic as an argument *()
routes = [('/', MainPage),
('/about', AboutPage),
('/news', NewsPage),
('/result', ResultPage),
('/fav', Favpage)]
app = webapp2.WSGIApplication(routes ,debug=True)

from flask import Flask
from flask_restful import Resource, Api
from load_data_pipeline import load
from search import *
import os
from parse import *

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app = Flask(__name__)
api = Api(app)

directory_name = 'Files'

class Load(Resource):
  def get(self):
    load(directory_name)
    return 'Success'

class Search(Resource):
   def get(self, word):
     return str(search_by_word(word))
     
class ReusableForm(Form):
    name = TextField('Search term:', validators=[validators.required()])
    @app.route("/search", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            word = request.form['name']
            return str(search_by_word(word))
        return render_template('form.html', form=form)

class ReusableFormHyponym(Form):
    name = TextField('Search term:', validators=[validators.required()])
    @app.route("/search_hyponym", methods=['GET', 'POST'])
    def moose():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            word = request.form['name']
            return str(search_hyponyms(word))
        return render_template('form.html', form=form)

class ReusableFormConceptNet(Form):
    name = TextField('Search term:', validators=[validators.required()])
    @app.route("/conceptnet", methods=['GET', 'POST'])
    def moose2():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            word = request.form['name']
            return str(search_using_conceptnet(word))
        return render_template('form.html', form=form)

class ReusableForm(Form):
    name = TextField('Search term:', validators=[validators.required()])
    @app.route("/multiple", methods=['GET', 'POST'])
    def multiple():
        form = ReusableForm(request.form)
        print(form.errors)
        if request.method == 'POST':
            word = request.form['name']
            words = word.split(' ')
            return str(search_multiple_words(words))
        return render_template('form.html', form=form)

class Finhack(Form):
    name = TextField('Search term:', validators=[validators.required()])
    @app.route("/finhack", methods=['GET', 'POST'])
    def finhack():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            company = request.form['name']
            result = finhack_search(company)
            return {'text': result[0], 'parse': parse(result[0]), 'information': "{'defendant': 'Samsung Electronics and affiliated parties'}"}
        return render_template('form.html', form=form)


api.add_resource(Load, '/load')
api.add_resource(Search, '/search/<string:search_id>')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
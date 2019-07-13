import os

from flask import Flask
from flask import request

from flask import render_template

todo_store={}
    
todo_store['depo']= ['Go for run', 'Listen Rock Music'] 
todo_store['shivang']= ['Read book', 'Play Fifa', 'Drink Coffee'] 
todo_store['raj']= ['Study', 'Brush']
todo_store['anket']= ['Sleep', 'Code'] 
todo_store['aagam']= ['play cricket', 'have tea'] 


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    def select_todos(name):
        global todo_store
        return todo_store[name]

    def get_todos_by_name(name):
        try:
            return select_todos(name)  
        except:
            return None

    def ins_todo(name,todo):
        global todo_store
        todo_store[name].append(todo)

    def add_todo_by_name(name,todo):

        try:
            ins_todo(name,todo) 
            return 'success' 
        except:
            return 'fail'


    
    @app.route('/add_todo')
    def add_todo():
        name = request.args.get('name')
        todo = request.args.get('todo')

        print('---------')
        print(name," ",todo)
        print('---------')
        
        ans=add_todo_by_name(name,todo)

        if(ans=='success'):
            return "Added Successfully"    
        else:
            return render_template ('404.html'),404

        
         

    # http://127.0.0.1:5000/todos?name=duster
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('---------')
        print(name)
        print('---------')

        person_todo_list = get_todos_by_name(name)

        if(person_todo_list!=None):
            return render_template('todo_view.html',todoss=person_todo_list)    
        else:
            return render_template ('404.html'),404            



    return app


from flask import Flask, redirect, render_template, request, url_for
from flask_restful import Api, Resource
from app import app
class LoginController:
    def success(name):
        return 'welcome %s' % name
    


    @app.route("/login",methods=["GET","POST"])  
    def login():
        if request.method == 'POST':
            user = request.form['nm']
            return redirect(url_for('success', name=user))
        else:
            return render_template('login.html')

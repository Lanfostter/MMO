from flask import Flask, request, redirect, url_for, render_template


# class LoginController:
#     @app.route('/success/<name>')
#     def success(name):
#         return 'welcome %s' % name
#
#     @app.routflask e('/login', methods=['GET', 'POST'])
#     def login(self):
#         if request.method == 'POST':
#             user = request.form['nm']
#             return redirect(url_for('success', name=user))
#         else:
#             return render_template('login.html')

from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


    
#jinja_env = jinja2.Environment(
#    loader = jinja2.FileSystemLoader(template_dir), autoescape=True) #loads the jinja environment and autoescapes

app = Flask(__name__) #this creates the app container
app.config['DEBUG'] = True

#return redirect('/valid-time?time={0}'.format(time))


@app.route("/")
def index():
   
    #template = jinja_env.get_template('home_login.html')
    return render_template('home_login.html', username_error='', password_error='', validation_error='')
  

@app.route("/", methods=['POST'])
def validate():
    username_error1 = ''
    password_error1 = ''
    validation_error1 = ''
    email_error = ''
    username = request.form['username']
    user_password = request.form['user_password']
    password_confirm = request.form['password_confirm']
    email = str(request.form.get('email')) 
    test = 0
    
    def Is_email(emailaddress): 
        email = str(emailaddress)
        length = len(email.strip())
        if length <= 23 and length >= 3 and email.count('@') == 1 and email.count('.') == 1:
            return True
        else:
            return False

    #validation
    
                
                

    def is_valid(user_input):
        length = len(str(user_input))
        if length >= 3 and length<=20:
            return True
        else:
            return False

    if is_valid(username):
        test += 1
    else:
        username_error1 = 'Username not valid'
    if is_valid(user_password):
        test += 1
    else:
        password_error1 = 'Password not valid'
        validation_error1 = 'Passwords don\'t match'
        test = 0
    if is_valid(password_confirm):
        test += 1
    if str(user_password) == str(password_confirm):
        test += 1
        if is_valid(user_password) == False or is_valid(password_confirm) == False:
            password_error1 = 'Password not valid'
            test = 0  
    else:
        password_error1 = 'Password not valid'
        validation_error1 = 'Passwords don\'t match'
        test = 0

    if len(str(email)) > 0:
        if Is_email(str(email)):
            test += 1
        else: 
            email_error = 'Email not valid'
            test = 0
    else: 
        if len(str(email)) == 0:
            test += 1
        else:
            email_error = 'Email not valid'
            test = 0
        
        
            

    if test == 5:
        return redirect('/greeting?username={0}'.format(username))
    else: 
        return render_template('home_login.html', email_error= email_error, username = username,username_error = username_error1, validation_error= validation_error1, password_error = password_error1, user_password = '', password_validation = '')


    
    
    #return form
   
@app.route("/greeting")
def greeting():
    username = request.args.get('username') 
    #template = jinja_env.get_template('Login_greeting.html')
    return render_template('Login_greeting.html',name=username)

app.run()
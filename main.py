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

def is_filled(filled):
    phrase = str(filled).strip
    try:
        if len(str(phrase)) > 0:
            return True
    except ValueError:
        return False

def validate_password(password, validation):
    is_password = is_filled(password)
    is_validation = is_filled(validation)

    if is_password == is_validation:
        return True
    else:
        return False
   

@app.route("/", methods=['POST'])
def validate():
    username_error1 = ''
    password_error1 = ''
    validation_error1 = ''
    username = request.form['username']
    user_password = request.form['user_password']
    password_confirm = request.form['password_confirm']
    email = str(request.form.get('email')) 
    
    #template = jinja_env.get_template('home_login.html')
    #validation
   
    
    
    #return form
    if len(str(username)) > 3:
        if len(str(user_password)) > 3:
            if len(str(password_confirm)) > 3:
                if str(user_password) == str(password_confirm):
                    if len(str(email)) > 3 and len(str(email))< 20:
                        if '@' in str(email) and '.' in str(email):
                            return redirect('/greeting?username={0}'.format(username))
                        else:
                            return render_template('home_login.html', email_error = 'Email not valid', username = username)
                    else:
                        return redirect('/greeting?username={0}'.format(username))            
                else:
                    validation_error1 = 'Passwords don\'t match'
                    username_error1 = 'Username not valid'
                    validation_error1 = 'Passwords don\'t match'
                    return render_template('home_login.html', username = username,username_error = username_error1, validation_error= validation_error1, password_confirm = validation_error1, user_password = '')
            else: 
                 password_error1 = 'Password not valid'
                username_error1 = 'Username not valid'
                validation_error1 = 'Passwords don\'t match' 
                return render_template('home_login.html', username = username,username_error = username_error1, validation_error= validation_error1, password_confirm = validation_error1, user_password = '')
        else:
            password_error1 = 'Password not valid'
            username_error1 = 'Username not valid'
            validation_error1 = 'Passwords don\'t match' 
            return render_template('home_login.html', username = username, username_error = username_error1, validation_error= validation_error1, password_confirm = validation_error1, user_password = '')
    else:
        username_error1 = 'Username not valid' 
        password_error1 = 'Password not valid' 
        validation_error1 = 'Passwords don\'t match'
        return render_template('home_login.html', username = username, username_error = username_error1, validation_error= validation_error1, password_confirm = validation_error1, user_password = '')
         


@app.route("/greeting")
def greeting():
    username = request.args.get('username') 
    #template = jinja_env.get_template('Login_greeting.html')
    return render_template('Login_greeting.html',name=username)

app.run()
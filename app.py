from flask import Flask ,render_template #from flask module i have imported Flask class
#creating an object app
app = Flask(__name__) #creating an object(app) of Flask class and passing __name__ as argument

#adding htmlfile
@app.route('/html') 
def html_fn():
    return render_template('index.html')

#adding dynamic url to html page
@app.route('/dynamic/<name>') 
def dynamic(name):
    return render_template('dynamic.html' , name=name) #first name is passing in dynamic.html


@app.route("/")
#defining a function
    # below a dynamic url & that is chagable

@app.route('/<name>')
def home(name):
    return "Hello " + name
@app.route('/<int:num>')
def pass_integer(num):
    return f"The square of {num} is {num**2}"
#print decimal numbers
@app.route('/<float:num>')
def pass_decimal(num):
    return f"The square of {num} is {num**2}"
#passing a integer variable --giving age restriction
@app.route('/age/<int:age>')
def age(age):
    if age >= 18:
        return "You are an adult"
    else:
        return "You are a minor"

#these are static url and this is unchangable

@app.route("/about")
def about():
    return "This is about page"
@app.route("/product")
def product():
    return "This is product page"
@app.route("/product/laptop")
def laptop():
    return "This is login laptop page"
@app.route("/contact")
def contact():
    return "This is contact page"

app.add_url_rule('/home','home',home)

if __name__ == "__main__":
    app.run(debug=True) #running the app in debug mode.debug = True koduthal eppoozhum server restart cheyeda avishyamilla change varuthupol
    
    

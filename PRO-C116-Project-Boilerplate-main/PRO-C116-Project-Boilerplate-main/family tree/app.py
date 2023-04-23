# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Shivam" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route('/father')
def father():
    father_name ='Pravash'
    father_age = 50
    return render_template(father.html, father_name=father_name, father_age=father_age)
    

# define the route to mother webpage
@app.route("/mother")
def mother():
    mother_name = 'Pushpa'
    mother_age  = 38
    return render_template(mother.html,mother_name = mother_name, mother_age=mother_age)



# define the route to friends webpage
@app.route("/friends")
def friends():
    friend1_name = 'Shivam'
    friend1_age = 16

    friend2_name ='Shaurya'
    friend2_age = 17
    return render_template(friends.html,friend1_name=friend1_name,friend1_age=friend1_age,friend2_name=friend2_name,friend2_age=friend2_age)


    



# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)


# named card website route
@app.route('/card')
def card():
    return 'Card Website'


# named card website route
@app.route('/card/<name>')
def card_name(name):
    return 'Card Website for ' + name


# named card website route
@app.route('/card/<name>/<int:age>')
def card_name_age(name, age):
    return 'Card Website for ' + name + ' and age ' + str(age)


# named card website route
@app.route('/card/<name>/<int:age>/<float:weight>')
def card_name_age_weight(name, age, weight):
    return 'Card Website for ' + name + ' and age ' + str(age) + ' and weight ' + str(weight)


if __name__ == '__main__':
    app.run()

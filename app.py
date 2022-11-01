from argparse import Action
from tkinter.tix import Form
from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    users_froyo_flavor = request.args.get('flavor')
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo!'

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return"""
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    favorite_color = request.args.get('color')
    favorite_animal = request.args.get('animal')
    favorite_city = request.args.get('city')
    return f'Wow, I didn\'t know {favorite_color} {favorite_animal} lived in {favorite_city}!'

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return"""
    <form action="/message_results" method="POST">
        What is your secret message? <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!"><br/>
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    secret_message = request.form.get('message')
    return f"""
    Here's your secret message!<br/>
    {sort_letters(secret_message)}
    """

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    result = 'string'
    number_1 = int(request.args.get('operand1'))
    number_2 = int(request.args.get('operand2'))
    operation_input = str(request.args.get('operation'))
    if operation_input == 'add':
        result = f'You chose to add {number_1} and {number_2}. Your result is: {number_1} + {number_2}'
    elif operation_input == 'subtract':
        result = f'You chose to subtract {number_1} and {number_2}. Your result is: {number_1} - {number_2}'
    elif operation_input == 'multiply':
        result = f'You chose to multiply {number_1} and {number_2}. Your result is: {number_1} * {number_2}'
    elif operation_input == 'divide':
        result = f'You chose to multiply {number_1} and {number_2}. Your result is: {number_1} / {number_2}'
    
    contect = {
        "operand1" : number_1,
        "operand2" : number_2,
        "operation" : operation_input,
        "result" : result
    }
    
    return render_template("calculator_results.html")


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
   
    # TODO: Get the sign the user entered in the form, based on their birthday
    users_name = request.args.get('users_name')
    horoscope_sign = request.args.get('horoscope_sign')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES[horoscope_sign]

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1, 99)

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number,
        'users_name' : users_name,
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
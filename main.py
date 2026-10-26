# Comment here
from pyscript import display, document

def countries_capital(e):
    document.getElementById('output').innerHTML = ' '
    user_input = document.getElementById('input1').value.capitalize().strip()

    countries = {
    'Madagascar':'Antananarivo',
    'Mongolia':'Ulaanbatar',
    'Egypt':'Cairo',
    'Philippines':'Manila',
    'USA':'Washington D.C.',
    'Denmark':'Copenhagen',
    'Chile':'Santiago'
    }

    display(countries[user_input], target='result')
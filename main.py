import scratchconnect
from random import randint
from time import strftime, localtime
import os
from keep_alive import keep_alive
#scratch_cookie = {
#   'Username': 'ProKameronALT',
#  'SessionID': os.environ['sessionsid'],
# 'CSRFToken': os.environ['csrftoken']
#}

session = scratchconnect.ScratchConnect("ProKameronALT",
                                        os.environ['password'])

connection = session.connect_project("690241530", True)


def get_random_project():
    while True:
        try:
            id = randint(1, 600000000)
            project = session.connect_project(id)
            return id
        except scratchconnect.Exceptions.InvalidProject:
            pass


def get_random_user():
    return session.connect_project(get_random_project()).author()['username']


def set_var(name, value):
    connection.connect_cloud_variables().set_cloud_variable(name, value)


def read_var(name):
    return connection.connect_cloud_variables().get_cloud_variable(name)


def encode(text):
    chars = list(
        '          abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
    )
    encoded = ''
    for letter in text:
        encoded += str(chars.index(letter))
    return encoded


random_user = get_random_user()
keep_alive()
while True:
    second = int(strftime("%S", localtime()))
    minute = int(strftime('%M', localtime()))
    set_var('server_up?', "1")
    if minute == 0:
        random_user = get_random_user()
        set_var('scratcher_encoded', encode(random_user))
        while minute == 0:
            minute = int(strftime('%M', localtime()))
    elif second % 10 == 0:
        print("set")
        set_var('scratcher_encoded', encode(random_user))

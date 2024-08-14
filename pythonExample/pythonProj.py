#!/usr/bin/python

# Function definition is here
def printme( str ):
    # This prints a passed string into this function
    print (str)
    return;

from project import db, app
from Cryptodome.Cipher import ARC4
import hashlib,wget
import json
#import os
from faker import Faker
import random
from werkzeug.utils import secure_filename
from docx import Document
import yaml
import base64

def arc4_encrypt_password(key, password):
    cipher = ARC4.new(key.encode('utf-8'))
    encrypted_password = cipher.encrypt(password.encode('utf-8'))
    return hashlib.md5(encrypted_password).hexdigest()

# Now you can call printme function
printme("Hello from JFROG");
printme("this is a log line that is monitored by the team and will cause alerts")

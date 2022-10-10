from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt= Bcrypt(app)
app.secret_key = '92f09598141f38cd1ce84bc25737294f56a9c9dc65uftyfhkjgyur5y8c87179485234135757f5eghjdsgdhjsgfhjsdgafhjgsdkfgsdhshdjkgsdgf47tb2'
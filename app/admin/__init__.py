# -*- coding:utf-8 -*-
from flask import Blueprint

admin = Blueprint("home", __name__)

import app.home.views
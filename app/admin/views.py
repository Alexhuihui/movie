# -*- coding:utf-8 -*-
from app import admin


@admin.route("/")
def index():
	return "<h1 style='color:blue'>this is admin</h1>"
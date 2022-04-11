from flask import request
import datetime

def get_date_data(date_list):
    return int(date_list[0]), int(date_list[1]), int(date_list[2])

def get_date(year, month, day):
    return datetime.date(year, month, day).strftime("%d/%m/%Y")

def get_input(input):
    return request.form[input]

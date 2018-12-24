#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:45:05 2018

@author: hannaholdorf
"""

#%% Create a HTTP server that can do simple arithmetic tasks

#GET /sum/1/2 returns 3
#GET /multiply/3/4 returns 12

from flask import Flask, jsonify

server = Flask("simple_arithmetic")

@server.route("/sum1plus2")
def sum1plus2():
    return 1 + 2 

@server.route("/multiply3with4")
def multiply3with4():
    return 3 * 4


server.run()

#%% Create a web server that maintains a list of the books you've read
#%% You should be able to add and delete individual books, and list all the books you've read

from flask import Flask, jsonify

server = Flask("booklist")

books = []


@server.route("/add_book/<title>")
def add_book(title):
    books.append(title)
    return jsonify(books)


#@server.route("/post_book/<title>", methods =["POST"])
#def post_book(title):
#    books.append(title)
#    return jsonify(books)


@server.route("/delete_contact/<name>", methods = ["DELETE"])
def delete_book(titel): 
    if titel in books:
        books.remove(titel)
        return jsonify("Book not in list")


@server.route("/book_list")
def show_book_list():
    return jsonify(books)


server.run()



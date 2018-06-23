from flask import Flask, make_response,request, render_template,redirect,url_for
from flask.ext.mysqldb import MySQL
import uuid
import arrow
import datetime
import io
import csv

db = sqlite3.connect('db.sqlite3')

app = Flask(__name__)

@socketio.on('text', namespace='/')
def text(message):
    query = query_db('update mainApp_lead set price'+ message['price']  +' where id='+message['id'])
    emit('message', {'sender': mess['name'],'msg': mess['name'] + ':' + message['msg']})

@socketio.on('joined',namespace="/")
def joined(message):
    join_room(message['room'])
    emit('status', {'msg': message['name'] + ' has entered the room.'}, room=message['room'])


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)

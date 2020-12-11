import sys
from app import app
from flask import abort, request, render_template, Response, redirect

from .forms import ChannelForm
from .models import ChatManager, MessageManager, SessionManager
from .mailer import send_mail


# ------------ Web Routes ------------ #
@app.route('/')
def index():
    """
    Home page
    """
    return render_template('index.html', title="Home Page")

@app.route('/blog-inner/')
def blog_inner():
    return render_template('blog-inner.html', title="Blog")


@app.route('/resume/')
def resume():
    """
    Resume page
    """
    return render_template('resume.html', title="Resume Page")

@app.route('/resume-print/')
def resume_print():
    """
    Resume printable version
    """
    return render_template('resume-print.html', title="Resume Printable")

@app.route('/session-start/', methods=['GET', 'POST'])
def create_session_page():
    """
    Create session page
    """
    return render_template('session.html', title='Session')


@app.route('/channels/create/', methods=['GET', 'POST'])
def create_chat_page():
    """
    Create chat page
    """
    form = ChannelForm()
    if form.validate_on_submit():
        channel_name = form.channel_name.data
        chat = ChatManager.create_chat(channel_name)
        chat_hash = chat.hash_key
        chat_url = '/channel/{}/'.format(chat_hash)
        return redirect(chat_url)
    return render_template('create_channel.html', title="Create Channel", form=form)


@app.route('/channel/<string:chat_hash>/', methods=['GET'])
def chat_page(chat_hash):
    """
    Chat page
    """
    chat = ChatManager.get_chat_from_hash(chat_hash)
    data = { 'id': chat.id }
    if chat:
        return render_template('channel.html', channel_name=chat.name, data=data, title="Channel")
    else:
        return render_template('channel_not_found.html')


# ------------ Ajax Routes ------------ #
@app.route('/contact-form/', methods=['POST'])
def contact():
    body = request.json
    send_mail(body)
    return {}

@app.route('/session/', methods=['POST'])
def create_session():
    """
    Create a new session for the supplied username.

    Request Body expected:
    {
        username: "myUser"
    }

    returns token to identify user's session
    """
    body = request.json
    name = body['username']
    token = SessionManager.create_session(name)
    return {"token": token}


@app.route('/session/<string:token>/username/', methods=['GET'])
def get_username_from_token(token):
    """
    Gets username from the token provided in the URL.

    Expects URL such as: /session/abc123/username/
    """
    username = SessionManager.get_username(token)
    return {"username": username}


@app.route('/messages/', methods=['POST'])
def create_message():
    """
    Create a new message. Uses the message manager to create the
    object in DB.

    Request Body expected:
    {
        username: "myUser",
        content: "Hello World",
        chat_id: "abc123"
    }
    """
    body = request.json
    message = MessageManager.create_message(body)
    return {"id": message.id}


@app.route('/chat/<string:chat_id>', methods=['GET'])
def get_chat_api(chat_id):
    """
    Get all messages in chat.
    """
    result = ChatManager.get_all_chat_messages(chat_id)
    response = []
    for message in result:
        response.append(message.to_dict())
    return {"messages": response}


@app.route('/chat/<string:chat_id>/last', methods=['GET'])
def get_last_messages_in_chat(chat_id):
    """
    Get the last x messages in chat. X by default is 100.

    Expects URL such as: /chat/abc123/last?count=100
    """
    num_messages = request.args.get('count', default=100)
    result = ChatManager.get_chat_messages(chat_id, num_messages)
    response = []
    for message in result:
        response.append(message.to_dict())
    return {"messages": response}


@app.route('/chat/<string:chat_id>/updates', methods=['GET'])
def get_message_updates_in_chat(chat_id):
    """
    Gets the most recent chat messages starting after the supplied ref_id.
    If no ref_id, then send empty response.

    Expects URL such as: /chat/abc123/updates?ref_id=32
    """
    last_id = request.args.get('ref_id', default=None)
    if not last_id:
        result = []
    else:
        result = ChatManager.get_chat_updates(chat_id, last_id)
    response = []
    for message in result:
        response.append(message.to_dict())
    return {"messages": response}

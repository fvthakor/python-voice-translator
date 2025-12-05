"""
Real-Time Voice Translation Chat Server
WebSocket server that handles multiple clients with voice translation
"""

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from googletrans import Translator
import base64
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Initialize translator
translator = Translator()

# Store active users
active_users = {}
chat_rooms = {'global': []}

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    """
    Backend translation endpoint for long text or as fallback
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        source_lang = data.get('source', 'auto')
        target_lang = data.get('target', 'en')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Use googletrans for translation
        translation = translator.translate(text, src=source_lang, dest=target_lang)
        
        return jsonify({
            'translated_text': translation.text,
            'source_lang': translation.src,
            'target_lang': target_lang
        })
    except Exception as e:
        print(f"Translation error: {e}")
        return jsonify({'error': str(e), 'translated_text': text}), 500

@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')
    emit('connection_response', {'status': 'connected', 'sid': request.sid})

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Client disconnected: {request.sid}')
    if request.sid in active_users:
        user_info = active_users[request.sid]
        emit('user_left', {
            'username': user_info['username'],
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }, room='global', broadcast=True)
        del active_users[request.sid]

@socketio.on('join_chat')
def handle_join(data):
    username = data.get('username', 'Anonymous')
    speak_lang = data.get('speak_lang', 'en')
    hear_lang = data.get('hear_lang', 'en')
    
    active_users[request.sid] = {
        'username': username,
        'speak_lang': speak_lang,
        'hear_lang': hear_lang
    }
    
    join_room('global')
    
    # Notify others
    emit('user_joined', {
        'username': username,
        'speak_lang': speak_lang,
        'hear_lang': hear_lang,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, room='global', broadcast=True, include_self=False)
    
    # Send user list to new user
    user_list = [
        {'username': u['username'], 'speak_lang': u['speak_lang'], 'hear_lang': u['hear_lang']}
        for u in active_users.values()
    ]
    emit('user_list', {'users': user_list})
    
    print(f'{username} joined the chat')

@socketio.on('send_message')
def handle_message(data):
    if request.sid not in active_users:
        return
    
    user_info = active_users[request.sid]
    
    message_data = {
        'username': user_info['username'],
        'original_text': data.get('original_text', ''),
        'original_lang': user_info['speak_lang'],
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'sid': request.sid
    }
    
    # Broadcast to all users in the room
    emit('new_message', message_data, room='global', broadcast=True)
    print(f"Message from {user_info['username']}: {data.get('original_text', '')}")

@socketio.on('send_voice')
def handle_voice(data):
    if request.sid not in active_users:
        return
    
    user_info = active_users[request.sid]
    
    voice_data = {
        'username': user_info['username'],
        'audio_data': data.get('audio_data', ''),
        'original_text': data.get('original_text', ''),
        'original_lang': user_info['speak_lang'],
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'sid': request.sid
    }
    
    # Broadcast to all users
    emit('new_voice_message', voice_data, room='global', broadcast=True)
    print(f"Voice message from {user_info['username']}")

@socketio.on('typing')
def handle_typing(data):
    if request.sid not in active_users:
        return
    
    user_info = active_users[request.sid]
    emit('user_typing', {
        'username': user_info['username'],
        'is_typing': data.get('is_typing', False)
    }, room='global', broadcast=True, include_self=False)

if __name__ == '__main__':
    print("=" * 60)
    print("🌐 REAL-TIME VOICE TRANSLATION CHAT SERVER".center(60))
    print("=" * 60)
    print("\n🚀 Server starting on http://localhost:5000")
    print("💡 Open this URL in multiple browsers to test chat\n")
    print("=" * 60)
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)

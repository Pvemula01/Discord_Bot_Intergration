from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
passw='Pranav@20'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pranav%4020@localhost/discord_bot'
db = SQLAlchemy(app)
 
class AuthToken(db.Model):
    _tablename_ = 'auth_tokens'
    server_id = db.Column(db.String(255), primary_key=True)
    token = db.Column(db.String(255), nullable=False)

@app.route('/store_token', methods=['POST'])
def store_token():
    server_id = request.form['server_id']
    token = request.form['token']
    existing_token = AuthToken.query.get(server_id)
    if existing_token:
        existing_token.token = token
    else:
        new_token = AuthToken(server_id=server_id, token=token)
        db.session.add(new_token)
    db.session.commit()
    return 'Token stored successfully'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    

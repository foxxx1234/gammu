from flask import Flask
from smsweb.models import db, Message
from flask import render_template
import os
import sys

# Ensure the system gammu module is accessible
if '/usr/lib/python3/dist-packages' not in sys.path:
    sys.path.insert(0, '/usr/lib/python3/dist-packages')
try:
    import gammu
except Exception:
    gammu = None


def create_app(db_path='sqlite:///sms.db'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        if Message.query.count() == 0:
            # Seed example data
            db.session.add_all([
                Message(sender='Alice', receiver='Bob', text='Hello Bob!'),
                Message(sender='Carol', receiver='Dave', text='Test message'),
            ])
            db.session.commit()

    @app.route('/')
    def index():
        messages = Message.query.order_by(Message.timestamp.desc()).all()
        return render_template('index.html', messages=messages, gammu_loaded=gammu is not None)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')

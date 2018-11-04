import json

from db_config import db


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(80), unique=True, nullable=False)
    capital = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'state': self.state, 'capital': self.capital}

    @staticmethod
    def get_all_locations():
        return [Location.json(location) for location in Location.query.all()]

    @staticmethod
    def get_location(_state):
        query = Location.query.filter_by(state=_state).first()
        return query

    @staticmethod
    def add_location(_state, _capital):
        new_location = Location(state=_state, capital=_capital)
        db.session.add(new_location)
        db.session.commit()

    @staticmethod
    def update_capital(_state, _capital):
        location_to_update = Location.query.filter_by(state=_state).first()
        location_to_update.capital = _capital
        db.session.commit()

    @staticmethod
    def delete_location(_state):
        is_successful = Location.query.filter_by(state=_state).delete()
        db.session.commit()
        return bool(is_successful)

    @staticmethod
    def add_location_td():
        Location.add_location("mn", "st paul")
        Location.add_location("ca", "sacramento")
        Location.add_location("ny", "albany")

    def __repr__(self):
        location_object = {
            'state': self.state,
            'capital': self.capital
        }
        return json.dumps(location_object)

from studygrow_api import db


class Milestone(db.Model):

    __tablename__ = 's_milestone'

    user_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, primary_key=True)
    workitem_id = db.Column(db.Integer)

    def get_by_userid(self, user_id):
        self.query.all()

    def __repr__(self):
        return '<User %s %s>' % (self.user_id, self.email)

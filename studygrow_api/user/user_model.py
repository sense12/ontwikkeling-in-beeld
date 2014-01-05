from studygrow_api import db
from studygrow_api import db_cursor


class Class(db.Model):

    """
    Student - Class
    """

    __tablename__ = 's_class'
    uid = db.Column('class_id', db.Integer, db.ForeignKey('u_user.class_id'), primary_key=True)
    class_code = db.Column(db.String)
    start_year = db.Column(db.Integer)

    def __repr__(self):
        return "<Class %s %s %s>" % (
            self.uid,
            self.class_code,
            self.start_year
        )


class User(db.Model):

    """
    User - User
    """

    __tablename__ = 'u_user'
    uid = db.Column('user_id', db.Integer, primary_key=True)
    class_id = db.Column(db.Integer)
    email = db.Column(db.String)
    Class = db.relationship('Class', backref='user', lazy='dymanic')

    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    is_student = db.Column(db.Boolean)

    def get_by_class(self, class_names):
        c = db_cursor()
        classes = '"%s"' % '", "'.join(class_names)
        q = """
        select u.user_id, u.email, c.class_id, c.class_code, c.start_year from u_user u
        inner join s_class c ON c.class_id = u.class_id
        where u.is_student = 1 AND c.class_code in (%s)
        """ % (classes)
        c.execute(q)
        iter = c.fetchall()

        results = []
        for row in iter:
            user = User()
            _class = Class()
            user.uid, user.email, _class.uid, _class.class_code, _class.start_year = row
            self.classes = [_class]
            results.append(user)
        return results

    def __repr__(self):
        return "<User %s %s %s %s %s>" % (
            self.uid,
            self.class_id,
            self.email,
            self.password,
            self.is_student
        )

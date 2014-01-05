from studygrow_api import db


class Course(db.Model):

    """
    Material - Course
    """

    __tablename__ = 'm_course'
    uid = db.Column('course_id', db.Integer, primary_key=True)
    title = db.Column(db.String)

    def __repr__(self):
        return "<Course %s %s %s>" % (
            self.uid,
            self.title,
        )
#
#
#class Assignment(db.Model):
#
#    """
#    Material - Assignment
#    """
#
#    __table__ = 'm_assignment'
#    uid = db.Column('assignment_id', db.Integer, primary_key=True)
#    parent_id = db.Column('parent_assignment', db.Integer, primary_key=True)
#    course_id = db.Column(db.Integer, db.ForeignKey('m_course.class_id'))
#    title = db.Column(db.String)
#    weight = db.Column(db.Integer)
#
#    def __repr__(self):
#        return "<Assignment %s %s %s %s %s>" % (
#            self.uid,
#            self.parent_id,
#            self.course_id,
#            self.title,
#            self.weight
#        )

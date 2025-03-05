from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import relationship


Base=declarative_base()
student_course_association=Table('student_course',Base.metadata,
                                 Column('student_id', ForeignKey('students.id'),primary_key=True),
                                 Column('course_id', ForeignKey('courses.id'),primary_key=True))


class Student(Base):
    __tablename__='students'
    id=Column(Integer,primary_key=True)
    name= Column(String,nullable=False)
    age=Column(Integer)

    profile= relationship("Profile", back_populates="student",uselist=False)

    courses= relationship("Course",
                          secondary=student_course_association,
                          back_populates="students")


class Profile(Base):
     __tablename__='profiles'
     id=Column(Integer,primary_key=True)
     bio=Column(String)
     location=Column(String)
     student_id=Column(Integer,ForeignKey('students.id'),primary_key=True)

     student=relationship("Student", back_populates="profile")

class Course(Base):
     __tablename__='courses'
     id=Column(Integer,primary_key=True)
     title=Column(String,nullable=False)

     students=relationship("Student",
                          secondary=student_course_association,
                          back_populates="courses")

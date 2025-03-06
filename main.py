
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import click
from models import Student,Profile, Course

engine= create_engine("sqlite:///students_mngmt.db")

SessionLocal= sessionmaker(bind=engine)

@click.group()
def cli():
    """
    CLI  for the student management System 

    """
    pass

#command to add a new student 

@cli.command()
@click.option('--name',prompt='Student Name')
@click.option('--age',prompt='Student Age',type=int)
def add_student(name,age):
    session=SessionLocal()
    student=Student(name=name, age=age)
    session.add(student)
    session.commit()
    click.echo(f"Added student: {student.name}")
    session.close()

@cli.command()
@click.option('--student-id',prompt='Student ID',type=int)
@click.option('--bio',prompt='Student Bio')
@click.option('--location',prompt='Student location')
def add_profile(student_id,bio,location):
    session=SessionLocal()
    student = session.query(Student).filter(Student.id==student_id).first()
    if not student:
        click.echo("Student Not Found")
        session.close()
        return
    profile=Profile(bio=bio, location=location,student=student)
    session.add(profile)
    session.commit()
    click.echo(f"Added profile for {student.name}:Bio:{profile.bio}, Location:{profile.location}")
    session.close()

@cli.command()   
@click.option('--title',prompt='Course Title')
def add_course(title):
    session=SessionLocal()
    course= Course(title =title)
    session.add(course)
    session.commit()
    click.echo(f"Added course:{course.title} (ID:{course.id}")
    session.close()
    
@cli.command() 
def list_students():
    session=SessionLocal()
    students=session.query(Student).all()
    for s in students:
        profile_details= f"Bio:{s.profile.bio},Location:{s.profile.location}"if s.profile else "No Profile"
        courses= ",".join([course.title for course in s.courses]) if s.courses else "No course found"
        click.echo(f"ID:{s.id},Name:{s.name},Age:{s.age} | {profile_details} | Courses:{courses}")

    session.close()

if __name__=='__main__':
    cli()


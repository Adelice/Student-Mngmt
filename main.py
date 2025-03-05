
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import click
from models import Student,Profile, Course

engine= create_engine("sqlite:///student_managements.db")

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


def add_profile():
    pass

def add_course():
    pass

def list_students():
    pass 


if __name__=='__main__':
    cli()


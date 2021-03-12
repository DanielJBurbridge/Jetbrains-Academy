from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Table(Base):

    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
session = Session()


def program_loop():
    options = ["Today's tasks", "Add task"]
    while True:
        for i, option in enumerate(options):
            print(f'{i+1}) {option}')
        print("0) Exit")

        selection = input()
        main_menu_switcher(selection)


def main_menu_switcher(selection):
    if selection == '0':
        quit_program()
    elif selection == '1':
        output_tasks()
    elif selection == '2':
        add_task()
    else:
        print('Invalid input')


def quit_program():
    print("Bye!")
    exit()


def output_tasks():
    rows = session.query(Table).all()

    if len(rows) != 0:
        for row in rows:
            print(f'{row.id}. {row.task}')
    else:
        print("Nothing to do!")


def add_task():
    new_task = input('\nEnter task')
    date = ''
    if date != '':
        new_row = Table(task=new_task, deadline=datetime.strptime(date, '%m-%d-%Y').date())
    else:
        new_row = Table(task=new_task)
    session.add(new_row)
    session.commit()


program_loop()








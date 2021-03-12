from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
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
    options = ["Today's tasks", "Week's tasks", "All tasks", "Missed tasks", "Add task", "Delete task"]
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
        output_todays_tasks()
    elif selection == '2':
        output_weeks_tasks()
    elif selection == '3':
        output_all_tasks()
    elif selection == '4':
        missed_tasks()
    elif selection == '5':
        add_task()
    elif selection == '6':
        delete_task()
    else:
        print('Invalid input')


def quit_program():
    print("Bye!")
    exit()

def output_todays_tasks():
    print(f'Today {datetime.today().day} {datetime.today().strftime("%b")}')

    today = datetime.today().date()
    rows = session.query(Table).filter(Table.deadline == today).all()

    if len(rows) != 0:
        for i, row in enumerate(rows):
            print(f'{i+1}. {row.task}')
    else:
        print("Nothing to do!")

    print()


def output_weeks_tasks():

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i1 in range(7):
        day = datetime.today() + timedelta(days=i1)
        day = day.date()
        rows = session.query(Table).filter(Table.deadline == day).all()
        print(f'{days[day.weekday()]} {day.day} {day.strftime("%b")}')

        if len(rows) != 0:
            for i2, row in enumerate(rows):
                print(f'{i2+1}. {row.task}')
        else:
            print("Nothing to do!")

        print()


def output_all_tasks():

    print("All tasks:")

    rows = session.query(Table).order_by(Table.deadline).all()

    if len(rows) != 0:
        for i, row in enumerate(rows):
            print(f'{i+1}. {row.task}. {row.deadline.day} {row.deadline.strftime("%b")}')
    else:
        print("Nothing to do!")


def add_task():
    new_task = input('\nEnter task\n')
    date = input('Enter deadline\n')

    if date != '':
        new_row = Table(task=new_task, deadline=datetime.strptime(date, '%Y-%m-%d').date())
    else:
        new_row = Table(task=new_task)
    session.add(new_row)
    session.commit()

    print('The task has been added\n')


def missed_tasks():
    print("Missed tasks:")

    today = datetime.today().date()
    rows = session.query(Table).filter(Table.deadline < today).order_by(Table.deadline).all()

    if len(rows) != 0:
        for i, row in enumerate(rows):
            print(f'{i+1}. {row.task}. {row.deadline.day} {row.deadline.strftime("%b")}')
    else:
        print("Nothing is missed!")

    print()


def delete_task():

    print("Choose the number of the task you want to delete:")
    rows = session.query(Table).order_by(Table.deadline).all()

    if len(rows) != 0:
        for i, row in enumerate(rows):
            print(f'{i+1}. {row.task}. {row.deadline.day} {row.deadline.strftime("%b")}')

        usr_input = int(input())
        if usr_input <= len(rows):
            row_to_delete = rows[usr_input-1]
            session.delete(row_to_delete)
            session.commit()
            print("The task has been deleted!")
    else:
        print("Nothing to delete!")


program_loop()








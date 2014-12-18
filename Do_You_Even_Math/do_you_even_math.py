from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy import desc
import random

Base = declarative_base()


class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Score(Base):
    __tablename__ = 'score'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("player.id"))
    score = Column(Integer)

engine = create_engine("sqlite:///do_you_even_math_db.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)


def get_simbol():
    simbols = ['+', '-', '*']

    return random.choice(simbols)


def get_number():
    return random.randrange(1, 100)


def get_problem():
    problem = []

    problem.append(get_number())
    problem.append(get_simbol())
    problem.append(get_number())

    return problem


def problem_slove():
    problem = get_problem()
    answer = input("{0} {1} {2} = ".format(problem[0], problem[1], problem[2]))

    if problem[1] == '+' and int(answer) == problem[0] + problem[2]:
        print("Correct!")
        return True

    elif problem[1] == '+' and int(answer) != problem[0] + problem[2]:
        print("Wrooooooong!")
        return False

    if problem[1] == '-' and int(answer) == problem[0] - problem[2]:
        print("Correct!")
        return True

    elif problem[1] == '-' and int(answer) != problem[0] - problem[2]:
        print("Wrooooooong!")
        return False

    if problem[1] == '*' and int(answer) == problem[0] * problem[2]:
        print("Correct!")
        return True

    elif problem[1] == '*' and int(answer) != problem[0] * problem[2]:
        print("Wrooooooong!")
        return False


def score(n):
    return n*n


def play():
    name = input("Insert name: ")
    n = 0
    player = Player(name=name)

    try:
        session.add(player)
        session.commit()
        print("Hi {}".format(name))

    except Exception:
        session.rollback()
        print("Hi again {} :)".format(name))

    while problem_slove():
        n += 1

    player_id = session.query(Player.id).filter(Player.name == name).one()

    current_scorr = Score(score=score(n), player_id=player_id[0])
    session.add(current_scorr)
    session.commit()

    print("Your score is {0} {1}".format(score(n), name))


def highscore():
    results = session.query(Player.name, Score.score).order_by(desc(Score.score
                                                                    )).all()
    lengh = 0

    if len(results) < 10:
        lengh = len(results)

        for index in range(lengh):
            print("{0} - {1} - {2}".format((index + 1), results[index][0],
                                           results[index][1]))

    else:
        for index in range(10):
            print("{0} - {1} - {2}".format((index + 1), results[index][0],
                                           results[index][1]))


def game_menu():
    print('Main Menu')
    print('  -"play"')
    print('  -"highscore"')
    command = input('Chose by typing the command:')

    while command != 'play' and command != 'highscore':
        print("Bad input, wrong command, try again!")
        command = input('Chose by typing the command:')

    if command == 'play':
        play()

    elif command == 'highscore':
        highscore()


def main():
    game_menu()


if __name__ == '__main__':
    main()

# Напишите определение класса SoccerPlayer
class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goal=1):
        self.goals += goal

    def make_assist(self, assist=1):
        self.assists += assist

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

# Ниже код для проверки методов класса SoccerPlayer
leo = SoccerPlayer('Leo', 'Messi')
assert isinstance(leo, SoccerPlayer)
assert leo.__dict__ == {'name': 'Leo', 'surname': 'Messi', 'goals': 0, 'assists': 0}
leo.score(700)
assert leo.goals == 700
leo.make_assist(500)
assert leo.assists == 500

leo.statistics()

kokorin = SoccerPlayer('Alex', 'Kokorin')
assert isinstance(kokorin, SoccerPlayer)
assert kokorin.name == 'Alex'
assert kokorin.surname == 'Kokorin'
assert kokorin.assists == 0
assert kokorin.goals == 0
kokorin.score()
assert kokorin.goals == 1
kokorin.score(5)
assert kokorin.goals == 6
kokorin.make_assist()
assert kokorin.assists == 1
kokorin.make_assist(10)
assert kokorin.assists == 11

kokorin.statistics()

obi = SoccerPlayer('Оби-Ван', 'Кеноби')
obi.make_assist()
assert obi.name == 'Оби-Ван'
assert obi.surname == 'Кеноби'
assert obi.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'goals': 0, 'assists': 1}
obi.statistics()

mila = SoccerPlayer('Mila', 'Kunis')
mila.make_assist()
mila.statistics()

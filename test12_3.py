from runner import Runner
from tournament import Tournament
from unittest import TestCase
import unittest

class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner('Test Runner') # создаем объект класса Runner с произвольным именем

        for _ in range(10): # вызываем метод walk 10 раз
            runner.walk()

        self.assertEquals(runner.distance, 50) # сравниваем distance этого объекта со значением 50

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.run()
        self.assertEquals(runner.distance, 100) # сравниваем distance этого объекта со значением 100

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner('Test Runner1')
        runner2 = Runner('Test Runner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {} # Создаём словарь для хранения результатов всех тестов

    def setUp(self):
        # создаем три объекта
        self.usein = Runner('Усейн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов в столбец
        for result in cls.all_results.values():
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Usein_Nik(self): #создаем турнир для участников Усейн и Ник
        tournament = Tournament(90, self.usein, self.nik)
        # запускаем турнир
        results = tournament.start()
        TournamentTest.all_results['test_usein_nik_race'] = {k: v.name for k, v in results.items()}
        # проверяем что Ник финишировал последний
        self.assertTrue(results[max(results)].name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Andrew_Nik(self):
        tornament = Tournament(90, self.andrew, self.nik)
        results = tornament.start()
        TournamentTest.all_results['test_andrew_nik_race'] = {k: v.name for k, v in results.items()}
        self.assertTrue(results[max(results)].name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Usein_Andrew_Nik(self):
        tornament = Tournament(90, self.usein, self.andrew, self.nik)
        results = tornament.start()
        TournamentTest.all_results['test_usein_andrew_nik_race'] = {k: v.name for k, v in results.items()}
        self.assertTrue(results[max(results)].name == 'Ник')


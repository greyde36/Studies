import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @unittest.skip("Тесты в этом кейсе заморожены")
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usein = Runner("Усэйн", 10)
        self.Andrey = Runner("Андрей", 9)
        self.Nik = Runner("Ник", 3)
        self.is_frozen = True

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def test_run_1(self):
        self.tournament = Tournament(90, self.Usein, self.Nik)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[1] = self.all_results

    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.Andrey, self.Nik)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[2] = self.all_results

    def test_run_3(self):
        self.tournament_3 = Tournament(90, self.Usein, self.Andrey, self.Nik)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()

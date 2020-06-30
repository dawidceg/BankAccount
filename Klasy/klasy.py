import linecache
import pickle



class Account():

	def __init__(self, name):
		self.name = name

	def wplata(self, nazwauzytkownika):
		from Funkcje import funkcje 
		self.nazwauzytkownika = nazwauzytkownika
		
		print("Ile chcesz wpłacić na konto?")
		kwota = int(input())

		with open (nazwauzytkownika, 'rb+') as f:
			stan = pickle.load(f)
			stan += kwota
		with open (nazwauzytkownika, 'rb+') as f:
			pickle.dump(stan, f)
			print("Wpłacono {} zł, na koncie pozostało {} zł\n".format(kwota, stan))
		return funkcje.start()



	def wyplata(self, nazwauzytkownika):
		from Funkcje import funkcje 
		self.nazwauzytkownika = nazwauzytkownika
		
		print("Ile chcesz wypłacić z konta?")
		kwota = int(input())

		while True:

			with open (nazwauzytkownika, 'rb+') as f:
				stan = pickle.load(f)
				if stan >= kwota:
					stan -= kwota
					with open (nazwauzytkownika, 'rb+') as f:
						pickle.dump(stan, f)
						print("Wypłacono {} zł, na koncie pozostało {} zł\n".format(kwota, stan))
					return funkcje.start()
				else:
					print("Nie posiadasz takiej kwoty na swoim koncie!\nObecnie posiadasz {} zł.\nSpróbuj jeszcze raz:".format(stan))
					kwota = int(input())


	def sprawdz(self, nazwauzytkownika, konto):
		self.nazwauzytkownika = nazwauzytkownika

		with open (nazwauzytkownika, 'rb+') as f:
			stan = pickle.load(f)
		return print("Na Twoim koncie znajduję się: {} zł.\n".format(stan))

	

	

class SaveAccount(Account):

	def __init__(self):
		pass

class StandardAccount(Account):

	def __init__(self):
		pass
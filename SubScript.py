import linecache
import getpass
import pickle

def start():
	print("\t\t Witaj w Banku")
	print("\t\t -----------------------")
	print("\t\t|       FSOCIETY       |")
	print("\t\t -----------------------")
	print("\n\tWpisz: 1 - Zaloguj		2 - Załóż Konto		3 - Wyjście")
	
	akcja = input()
	if akcja == '1':
		logowanie()
	elif akcja == '2':
		new_account()
	elif akcja == '3':
		exit()
	else:
		print("\nOpcja nie istnieje. Proszę wpisać: 1- Zaloguj	2- Załóż Konto	3- Wyjście")
		start()


def new_account():

	print("Witamy w trybie zakładania konta. \nNajpierw musisz podać login. Nie może mieć mniej niż 4 i więcej niż 8 znaków:\n")

	wyjscie = True

	while wyjscie:
		print("Podaj login: ")
		name = getpass.getpass()

		if len(name) > 8:
			print("Przepraszam za długa nazwa. Możesz użyć maksymalnie 8 znkaów. Spróbuj ponowanie lub 1 aby wyjść")
		elif len(name) < 4:
			print("Przepraszam za krótka nazwa. Musisz użyć minimalnie 4 znkaów. Spróbuj ponowanie lub 1 aby wyjść")
		#elif len(name) < 8 and len(name) > 4:
			#Sprawdź czy dany login już istnieje
		else:
			print('Login poprawny!')
			while True:
				print('Proszę podać 4 liczbowy kod PIN. Lub 1 aby anulować zakładanie konta.')
				pin = getpass.getpass()
				if pin == '1':
					print('Anulowano zakładanie konta!')
					wyjscie = False
					return name, pin 
				elif len(pin) < 4:
					print("Przepraszam za krótki kod PIN. Proszę wpisać 4 liczby")
				elif len(pin) > 4:
					print("Przepraszam za długi kod PIN. Proszę wpisać 4 liczby")
				else:
					accountslist = open('accountslist.txt', 'a')
					accountslist.write(name+pin+'\n')

					accountslist.close()

					nazwakonta_save = open(name+'save.txt', 'w+')
					nazwakonta_standard = open(name+'standard.txt', 'w+')
					with open (name+'save.txt', 'rb+') as f:
						pickle.dump(0, f)
					with open (name+'standard.txt', 'rb+') as f:
						pickle.dump(0, f)

					
					# nazwakonta_save.write(name+'save')
					# nazwakonta_standard.write(name+'standard')

					nazwakonta_standard.close()
					nazwakonta_save.close()

					return start()

def logowanie():
	print("\t -----------------------")
	print("\t|		FSOCIETY BANK    |")
	print("\t -----------------------")
	print("LOGIN: ")
	name = getpass.getpass()
	print("PIN: ")
	pin = getpass.getpass()

	
	accountslist = open('accountslist.txt', 'r')
	line = accountslist.readline()
	log = False
	name_pin = name+pin
	while line:
		if line == name_pin+'\n':
			log = True
			accountslist.close()
			break
		else:
			line = accountslist.readline()
			log = False
	
	accountslist.close()
	if log == True:
		print("Logowanie Poprawne!")
		kontosave = SaveAccount()
		kontostandard = StandardAccount()
		return menu(name, kontosave, kontostandard)
	else:
		print("\tNieprawodiłowy login lub kod PIN.\n\tCzy chcesz spróbować ponownie?\n\tWpisz: 1 - Tak\n\t       2 - Nie")
		kolejna_proba = input()
		while True:
			if kolejna_proba == '1':
				return logowanie()
			elif kolejna_proba == '2':
				return start()
			else:
				print("Proszę wpisać 1 - Tak lub 2 - Nie")
				kolejna_proba = input()


def menu(nazwauzytkownika, kontosave, kontostandard):

	print("\t -----------------------")
	print("\t|		FSOCIETY BANK    |")
	print("\t|         MENU:         |")
	print("\t -----------------------")
	print("1	-	Sprawdź saldo kont")
	print("2	-	Konto Standard")
	print("3	-	Konto oszczędnościowe")
	print("4	-	Przelew wewnętrzny")
	print("5	-	Wyloguj")

	wybor = input()

	while True:
		if wybor == '1':
			print("STANDARD: ")
			kontostandard.sprawdz(nazwauzytkownika+'standard.txt', kontostandard)
			print("OSZCZĘDNOŚCIOWE: ")
			kontosave.sprawdz(nazwauzytkownika+'save.txt', kontosave)
			wybor = input()

		elif wybor == '2':
			podmenu(nazwauzytkownika+'standard.txt', kontostandard)

		elif wybor == '3':
			podmenu(nazwauzytkownika+'save.txt', kontosave)

		elif wybor == '4':
			przelew(nazwauzytkownika, kontosave, kontostandard)

		elif wybor == '5':
			start()

		else:
			print("Proszę wpisać 1, 2, 3, 4 lub 5: ")
			wybor = input()


def podmenu(nazwauzytkownika, konto):
	print("\t -----------------------")
	print("\t|		FSOCIETY BANK    |")
	print("\t|       MENU KONTA      |")
	print("\t -----------------------")
	print("1	-	Wpłać pieniądze")
	print("2	-	Wypłać pieniądze")
	print("3	-	Cofnij")

	konto.sprawdz(nazwauzytkownika, konto)

	wybor = input()

	while True:
		if wybor == '1':
			konto.wplata(nazwauzytkownika)

		elif wybor == '2':
			konto.wyplata(nazwauzytkownika)

		elif wybor == '3':
			return start()

		else:
			print("Proszę wpisać 1, 2, 3 lub 4: ")
			wybor = input()

def przelew(nazwauzytkownika, kontostandard, kontosave):

		print("Witaj w opcji transferu między kontami!")
		print("STANDARD: ")
		kontostandard.sprawdz(nazwauzytkownika+'standard.txt', kontostandard)
		print("OSZCZĘDNOŚCIOWE: ")
		kontosave.sprawdz(nazwauzytkownika+'save.txt', kontosave)
		print("Z jakiego konta chcesz przelać pieniądze? 1-	STANDARD 	2- OSZCZĘDNOŚCIOWE")
		wybor = input()

		while True:
			if wybor == '1':
				print("Jaką kwotę chciałbyś przelać z konta STANDARD na konto OSZCZĘDNOŚCIOWE?")
				kwota = int(input())
				with open (nazwauzytkownika+'standard.txt', 'rb+') as f:
					stan = pickle.load(f)
					while True:
						if kwota > stan:
							print("Nie posiadasz tyle pieniędzy na koncie STANDARD!\nPodaj inną kwotę!")
							kwota = int(input())
						else:
							with open (nazwauzytkownika+'standard.txt', 'rb+') as f:
								stan = pickle.load(f)
								stan -= kwota
							with open (nazwauzytkownika+'standard.txt', 'rb+') as f:
								pickle.dump(stan, f)
							with open (nazwauzytkownika+'save.txt', 'rb+') as f:
								stan_dwa = pickle.load(f)
								stan_dwa += kwota
							with open (nazwauzytkownika+'save.txt', 'rb+') as f:
								pickle.dump(stan_dwa, f)
							
							return start()
			elif wybor == '2':
				print("Jaką kwotę chciałbyś przelać z konta OSZCZĘDNOŚCIOWEGO na konto STANDARD?")
				kwota = int(input())
				with open (nazwauzytkownika+'save.txt', 'rb+') as f:
					stan = pickle.load(f)
					while True:
						if kwota > stan:
							print("Nie posiadasz tyle pieniędzy na koncie OSZCZĘDNOŚCIOWYM!\nPodaj inną kwotę!")
							kwota = int(input())
						else:
							with open (nazwauzytkownika+'save.txt', 'rb+') as f:
								stan = pickle.load(f)
								stan -= kwota
							with open (nazwauzytkownika+'save.txt', 'rb+') as f:
								pickle.dump(stan, f)
							with open (nazwauzytkownika+'standard.txt', 'rb+') as f:
								stan_dwa = pickle.load(f)
								stan_dwa += kwota
							with open (nazwauzytkownika+'standard.txt', 'rb+') as f:
								pickle.dump(stan_dwa, f)
							
							return start()
			else:
				print("Proszę wybrać konto!")
				print("Z jakiego konta chcesz przelać pieniądze? 1-	STANDARD 	2- OSZCZĘDNOŚCIOWE")
				wybor = input()
					



class Account():

	def __init__(self, name):
		print("ACCOUNT CLASS")
		self.name = name

	def wplata(self, nazwauzytkownika):
		self.nazwauzytkownika = nazwauzytkownika
		
		print("Ile chcesz wpłacić na konto?")
		kwota = int(input())

		with open (nazwauzytkownika, 'rb+') as f:
			stan = pickle.load(f)
			stan += kwota
		with open (nazwauzytkownika, 'rb+') as f:
			pickle.dump(stan, f)
			print("Wpłacono {} zł, masz teraz {} zł".format(kwota, stan))
		return start()



	def wyplata(self, nazwauzytkownika):
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
						print("Wypłacono {} zł, masz teraz {} zł".format(kwota, stan))
					return start()
				else:
					print("Nie posiadasz takiej kwoty na swoim koncie!\nSpróbuj jeszcze raz.")
					kwota = int(input())


	def sprawdz(self, nazwauzytkownika, konto):
		self.nazwauzytkownika = nazwauzytkownika

		with open (nazwauzytkownika, 'rb+') as f:
			stan = pickle.load(f)
		return print("Na Twoim koncie znajduję się: {} zł.".format(stan))

	

	

class SaveAccount(Account):

	def __init__(self):
		print("SAVEACCOUNT CLASS")


class StandardAccount(Account):

	def __init__(self):
		print("STANDARDACCOUNT CLASS")









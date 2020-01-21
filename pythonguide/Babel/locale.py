from babel import Locale

locale = Locale('es')
print(locale.territories['FR'])

month_names = locale.months
print(Locale('fr').months['format']['wide'][10].capitalize())

weekday_names = locale.months
print(Locale('fr').months['format']['wide'][10].capitalize())
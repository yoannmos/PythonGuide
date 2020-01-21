from datetime import date
from babel.dates import format_date

d = date(2019, 12, 20)

en_date_form = format_date(d, locale='en')
print("\n",en_date_form)

de_date_form = format_date(d, locale='de')
print("\n",de_date_form)

it_date_form = format_date(d, locale='it')
print("\n",it_date_form)

fr_date_form1 = format_date(d, locale='fr')
print("\n",fr_date_form1)

fr_date_form2 = format_date(d, "EEEE, dd.MMMM.yyyy", locale='fr')
print("\n",fr_date_form2)

fr_month_form1 = format_date(d, "MMMMM", locale='fr')
print("\n",fr_month_form1)

fr_month_form2 = format_date(d, "MMMM", locale='fr')
print("\n",fr_month_form1)

fr_month_form3 = format_date(d, "MMM", locale='fr')
print("\n",fr_month_form2)

fr_month_form4 = format_date(d, "MM", locale='fr')
print("\n",fr_month_form3)


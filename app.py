import datetime

data_str = input("Įveskite datą (YYYY-MM-DD): ")
data = datetime.datetime.strptime(data_str, "%Y-%m-%d")
delta = datetime.datetime.today() - data

print(f"Nuo įvestos datos praėjo: {delta.days} dienų")

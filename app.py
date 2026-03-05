import pendulum

data_str = input("Įveskite datą (YYYY-MM-DD): ")
data = pendulum.from_format(data_str, "YYYY-MM-DD")
delta = data.diff(pendulum.today())

print(f"Nuo įvestos datos praėjo: {delta.in_years()} metų")
print(f"Nuo įvestos datos praėjo: {delta.in_days()} dienų")

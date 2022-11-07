import psycopg2
import matplotlib.pyplot as plt

username = 'ivanyk'
password = 'postgres'
database = 'ivanyk_DB'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT name, capacity FROM powerplants 
WHERE country = 'United States of America'
ORDER BY capacity DESC;
'''

query_2 = '''
SELECT fuel_name, COUNT(powerplants.id) FROM fuels
JOIN powerplants ON fuels.fuel_id = powerplants.fuel_type
GROUP BY fuel_name;
'''

query_3 = '''
SELECT COUNT(fuel_name), SUM(powerplants.capacity) FROM fuels
JOIN powerplants ON fuels.fuel_id = powerplants.fuel_type
GROUP BY fuel_name
ORDER BY SUM(powerplants.capacity);
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur1 = conn.cursor()
    cur1.execute(query_1)
    names = []
    capacities = []

    for row in cur1:
        names.append(row[0])
        capacities.append(row[1])

    cur2 = conn.cursor()
    cur2.execute(query_2)
    fuels = []
    fuels_amount = []

    for row in cur2:
        fuels.append(row[0])
        fuels_amount.append(row[1])

    cur3 = conn.cursor()
    cur3.execute(query_3)
    fuel = []
    capacity = []

    for row in cur3:
        fuel.append(row[0])
        capacity.append(row[1])


x_range = range(len(names))
bar = plt.bar(x_range, capacities, width=0.5)
plt.title('Потужність виробленої енергії кожною електростанцією в США')
plt.xlabel('Електростанції')
plt.xticks(x_range, names, rotation=75)
plt.ylabel('Потужність, МегаВатт')
plt.bar_label(bar, label_type='center')
plt.tight_layout()
plt.show()


plt.pie(fuels_amount, labels=fuels, autopct='%1.1f%%')
plt.title('Частка кількості електростанцій за типом джерела енергії')
plt.show()


x_range = range(len(fuels))
plt.plot(x_range, capacity, marker='o')
plt.xticks(x_range, fuels)
plt.title('Загальний обсяг потужності для кожного джерела енергії')
plt.ylabel('Потужність, МегаВатт')
plt.xlabel('Джерело енергії')

for x,y in zip(x_range,capacity):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,4.5), ha='center')

plt.tight_layout()
plt.show()

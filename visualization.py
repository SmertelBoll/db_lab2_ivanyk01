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


    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3, figsize=(11, 8))

    x_range = range(len(names))
    bar = bar_ax.bar(x_range, capacities, label='capacities', width=0.5)
    bar_ax.set_title('Потужність виробленої енергії\nкожною електростанцією в США')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(names, fontdict={'rotation': 75})
    bar_ax.set(xlabel='Електростанції', ylabel='Потужність, МегаВатт')
    bar_ax.bar_label(bar)

    cur2 = conn.cursor()
    cur2.execute(query_2)
    fuels = []
    fuels_amount = []

    for row in cur2:
        fuels.append(row[0])
        fuels_amount.append(row[1])

    pie_ax.pie(fuels_amount, labels=fuels, autopct='%1.1f%%')
    pie_ax.set_title('Частка кількості електростанцій\nза типом джерела енергії')

    cur3 = conn.cursor()
    cur3.execute(query_3)
    fuel = []
    capacity = []

    for row in cur3:
        fuel.append(row[0])
        capacity.append(row[1])

    x_range = range(len(fuels))
    graph_ax.plot(x_range, capacity, marker='o')
    graph_ax.set_xticks(x_range)
    graph_ax.set_xticklabels(fuels)
    graph_ax.set_title('Загальний обсяг потужності\nдля кожного джерела енергії')
    graph_ax.set(xlabel='Джерело енергії', ylabel='Потужність, МегаВатт')

    for x, y in zip(x_range, capacity):
        label = "{:.2f}".format(y)
        graph_ax.annotate(label, (x, y), textcoords="offset points", xytext=(0, 4.5), ha='center')


figure.tight_layout()
plt.show()
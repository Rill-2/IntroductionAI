
def add_routes():
    c = int(input("Введите количество маршрутов: "))
    i = 0
    while i < c:
        start_point = input("Введите начальную точку ")
        end_point = input("Введите конечную точку ")
        num = int(input("Введите номер маршрута "))
        route = {
        'start_point': start_point,
        'end_point': end_point,
        'num': num
        }
        routes.append(route)
        i += 1
        global sorted_routes
    if len(routes) > 1:
        sorted_routes = sorted(routes, key=lambda row: row['num'])

def print_routes():
    for route in sorted_routes:
        print(route['num'], route['start_point'], '-', route['end_point'])
		
def get_point():
    point = input("Ведите название пункта маршрута ")
    s = ''
    for route in sorted_routes:
        if route['start_point'] == point or route['end_point'] == point:
            s += str(route['num']) + route['start_point'] + ' - ' + route['end_point'] + '\n'
    if s == '':
        s = 'Не найдено маршрутов в пункте'
    print(s)



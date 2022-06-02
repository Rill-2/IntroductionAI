import os
import inf
from os import s

routes = []
global sorted_routes
sorted_routes = []
add_routes()
print_routes()
get_point()

while True:
    os.system('cls')
    print("Заполнить и вывести >> [1]")
    print("Вывести >> [2]")
    
    cmd = int(input(">>"))
    
    if cmd == 1:
        routes = inf.add_routes(routes)
		inf.print_routes(routes)
		inf.get_point(routes)               
    elif cmd == 2:
        break
    else:
        print(f"Неизветсная команда: {cmd}\n")
        input("Нажмите 'Enter' для продолжения")
    
    if __name__ == '__main__':
         inf.main()

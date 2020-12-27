from prettytable import PrettyTable  
def add_rows():
    fi = ['№','Имя, Фамилия','Ид страницы','Токен']    
    tbl = PrettyTable(fi)
    tbl.add_row([1, 'Тест Тестов', '832587356', 'Токен сюда впиши да'])
    
    print(tbl)
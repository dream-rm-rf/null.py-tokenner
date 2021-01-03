from prettytable import PrettyTable 
token = 'null' 
def add_rows():
    fi = ['№','Имя, Фамилия','Ид страницы','Токен']    
    tbl = PrettyTable(fi)
    tbl.add_row([1, 'Матвей Усов', '536178108', '1eea9314257a148b4b554857d37f4cdrghthhfjwes78rd6g8d688d815e5996b7a342119c6cd0f789da4d29d90a8b44345e1ed0ba32a02b'])
    
    print(tbl)
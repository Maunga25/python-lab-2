import csv
import os
import time

#Q.1
RED ='\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
END ='\u001b[0m'
length = ' '*30
print(f'флаг Таиланда')
print(f'{RED}{length}+{END}\n'
      f'{WHITE}{length}+{END}\n'
      f'{BLUE}{length}+{END}\n'
      f'{BLUE}{length}+{END}\n'      f'{WHITE}{length}+{END}\n'
      f'{RED}{length}+{END}')




#Q.2
def generate_pattern(x,с=1):
    pattern = ''
    if x > 10:
        x = 10

    y = 2*с*x
    square = f'{WHITE}   {END}'
    for i in range(x):
        for j in range(y):
            if j > (2*x)-1:
                times = j // (2*x)
                j = j-(times*2*x)
            if i < x//3 and j == (2*x//2)-1:
                pattern += square
            elif i < x//3 and j == x:
                pattern += square
            elif i == x-1 and 3*2*x/4 < j:
                pattern += square
            elif i == x-1 and j < (2*x/4)-1:
                pattern += square
            elif i+j == x+1 and i != 0:
                pattern += square
            elif j-x+2 == i and i != 0:
                pattern += square
            else:
                pattern += '   '
        pattern += '\n'
    print(pattern)
#print('Q.2 Вариант 6 (pattern)')
generate_pattern(6,2)





#Q.3 #вариант 6
def generate_graph(y,x):
   graph = ''
   for i in range(y, -3, -1):
       for j in range(-1, x+1, 1):
           if j == -1 and i > -1:
               graph += f' {i}|'
           elif i == -2 and j != -1:
               graph += f' {j} '
           elif i == -1 and j == -1:
               graph += '   '
           elif i == -1:
               graph += '---'
           elif i*j == 1 and i>= 0 and j>= 0:
               graph += '\33[31m * '
               graph += END
           else:
               graph += f'   '
       graph += '\n'
   print(graph)

print('Q3.f(x) = 1/x')
generate_graph(6,6)

#Q.4вариант 6 (Проценто )
def get_percent():
   to_50 = 0
   from_50 = 0
   with open('books-en (2).csv','r') as csv_file:
       table = list(csv.reader(csv_file, delimiter=';'))
       for row in table:
           if row == table[0]:
               continue
           if ',' in row[6]:
               row[6] = row[6].replace(',', '.')
           if float(row[6]) <= 50:
               to_50 += 1
           else:
               from_50 += 1
   from_50_percent = round(100*from_50/len(table), 2)
   to_50_percent = round(100*to_50/len(table), 2)
   data = [[' <=50',to_50_percent],[' >50',from_50_percent]]
   return data

#Q.5 Гистограм.
def generate_histogram(entries):
   graph = ''
   for i in range(len(entries)-1,-3,-1):
       for j in range(0,110,10):
           if j == 0 and i>= 0:
               graph += f'      |\n{entries[i][0]}|'
               num_of_times = int(entries[i][1])//10
               graph += BLUE
               graph += '    '*num_of_times
               graph += f'{END}{entries[i][1]}%'
           elif i <= -1 and j== 0:
               graph +='      '
           elif i == -1 and j> 0:
               graph += f'----'
           elif i == -2 and j> 0:
               graph += f' {j} '
       graph += '\n'
   print(graph)

data = get_percent()
generate_histogram(data)

#дополнително
def animation(x):
   for i in range(x):
       line = ''
       for j in range(x):
           if i == 0 and j >2:
               line += f'{WHITE}   {END}'
           else:
               line += '   '
       print(line)
       time.sleep(0.1)
   os.system('cls')
   for i in range(x):
       line = ''
       for j in range(x):
           if i == x // 2 and j == x // 2:
               line += f'{WHITE}   {END}'
           else:
               line += '   '
       print(line)
       time.sleep(0.1)
   os.system('cls')
   for i in range(x):
       line = ''
       for j in range(x):
           if i == j or i + j == x - 1:
               line += f'{WHITE}   {END}'
           else:
               line += '   '
       print(line)
       time.sleep(0.1)
   os.system('cls')

print('Q5 дополнително')
animation(15)


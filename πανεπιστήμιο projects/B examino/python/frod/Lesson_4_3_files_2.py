'''
                  ΔΙΑΧΕΙΡΙΣΗ ΑΡΧΕΙΩΝ
'''

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'w') as g:
    g.write('First new line\n') 
    g.write('Second new line\n') 
    g.write('Third new line\n')

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'r') as g:
    print(g.read())
    
with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'w') as g:  # Πολύ προσοχή με τη χρήση του ΄'w' γιατί διαγράφει τα προηγούμενα
    g.write('Fourth new line\n') 

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'r') as g:
    print(g.read())
   
print('********************')

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'r+') as g:  # Παράδειγμα διόρθωσης κειμένου
    g.seek(2)
    g.write('XX')

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'r') as g:
    print(g.read())



with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'w') as g:  # Πολύ προσοχή με τη χρήση του ΄'w' γιατί διαγράφει τα προηγούμενα
    g.seek(2)
    g.write('XX')
    
with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'r') as g:
    print(g.read())

print('********************')

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_append.txt', 'w') as g:  # Παράδειγμα δημιουργίας αρχείου
    for i in range(5):
        g.write('Line {} \n'.format(i+1))

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_append.txt', 'r') as g: # Διαβάζουμε το αρχείο
    print(g.read())


with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_append.txt', 'a') as g: #  # Παράδειγμα προσθήκης κειμένου στο τέλος του αρχικού μας αρχείου
    for i in range(2):
        g.write('Extra line {} \n'.format(i+1))

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_append.txt', 'r') as g:  # Διαβάζουμε το αρχείο
    print(g.read())
    

print('********************')
# Δημιουργία αντιγράφου αρχείου

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'w') as g:
    g.write('First new line\n') 
    g.write('Second new line\n') 
    g.write('Third new line\n')


with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'r') as f:
   with open('test_new.txt', 'w') as g:
        for x in f:
            g.write(x)

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_2.txt', 'r') as f:
    print(f.read())

with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_new.txt', 'r') as g:
    print(g.read())

print('********************')

# Μπορούμε να χρησιμοποιήσουμε τις εντολές/μεθόδους που υπάρχουν στις συμβολοσειρές. Για παράδειγμα:
with open('C:/Users/despo_000/Desktop/Φροντ 2022/test_new.txt', 'r+') as g:
    s=g.read()
    x = s.replace("line", "word")
    y=s.upper()

print(x) 
print(y)

#import pandas as pd
# Read the csv file
#df = pd.read_csv("C:/Users/despo_000/Desktop/Φροντ 2022/data1.csv")

# First 5 rows
#df.head()
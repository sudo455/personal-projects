'''
Pandas
Μια πολύ χρήσιμη και διαδεδομένη βιβλιοθήκη είναι η Pandas, που παρέχει υψηλής απόδοσης data structures για τον χειρισμό,
τον καθαρισμό και την προετοιμασία δεδομένων ώστε να αποτελέσουν input για την διαδικασία της μηχανικής μάθησης.
Η παροχή “καθαρών” δεδομένων με τη σωστή μορφή είναι ζωτικής σημασίας για την πραγματοποίηση σωστών προβλέψεων στο machine learning, 
και σίγουρα δεν πρέπει να παραβλεφθεί.
Το Pandas μας επιτρέπει να μορφοποιήσουμε αποτελεσματικά τα δεδομένα μας, ακριβώς με τη μορφή που τα χρειαζόμαστε, 
αποφεύγοντας την παγίδα να συμπεριλάβουμε προβληματικά ή ελλειπή δεδομένα στις αναλύσεις μας.
'''

import pandas as pd
import numpy as np

# Reference:
# https://pandas.pydata.org/docs/user_guide/index.html
'''
ΣΕΙΡΕΣ ΔΕΔΟΜΕΝΩΝ (Series)

Οι σειρές δεδομένων είναι λίστες τιμών δεδομένων που αντιστοιχών σε τιμές δεικτών.

Μπορούμε να δημιουργήσουμε μία σειρά δεδομένων αφήνοντας την pandas να δώσουν ως προεπιλεγμένες τιμές
στους δείκτες ακαίρεους αριθμούς:
'''

s = pd.Series([20, 100, 5, 4, 6, 8])

print(s)  # dtype('int64'),η Python αποθηκεύει κάθε τιμή σε αυτή τη στήλη ως ακέραιο αριθμό 64 bit.

'''
Μπορούμε να δημιουργήσουμε μία σειρά δεδομένων και να ορίσουμε εμείς τα ονόματα των δεικτών:
'''

x = pd.Series(index=range(5, 10), data=[1, 3, 9, 11, 12])
print(x)

print(x[7])  # Επιλογή δεδομένου της σειράς με δείκτη 7

x = pd.Series(data=[1, 3, 9, 11, 12], index=['a', 'b', 'c', 'd', 'e'])
print(x)

print(x['a'])  # Επιλογή δεδομένου της σειράς με δείκτη 'a'

# Παραδείγματα τεμαχισμού σειράς δεδομένων με τη χρήση των εντολών iloc και loc

print(x.iloc[:3])

print(x.loc['a':'d'])

'''
ΠΛΑΙΣΙΑ ΔΕΔΟΜΕΝΩΝ (DataFrames)

Ένα πλαίσιο δεδομένων (DataFrame) είναι μία δομή δεδομένων που μπορούν να αποθηκευτούν δεδομένα διαφορετικών τύπων
(χαρακτήρες, ακέραιοι αριθμοί, δεκαδικοί αριθμοί κλπ) σε στήλες. Είναι παρόμοιο με έναν πίνακα ενός φύλλου δεδομένω Excel 
ή με έναν SQL πίνακα.

Οι σειρές δεδομένων είναι στην πράξη μία απλή στήλη ενός πλαισίου δεδομένων.
'''

df = pd.DataFrame([[1, 3, 11, 2],
                   [9, 23, 0, 2]])

print(df)

df = pd.DataFrame({'col1': [1, 3, 11, 2],
                   'col2': [9, 23, 0, 2]})
print(df)

df = pd.DataFrame({'col1': [1, 3, 11, 2],
                   'col2': [9, 23, 0, 2]},
                  index=['Car A', 'Car B', 'Car C', 'Car D'])

print(df['col1'])  # indexing
print(df.col1)  # use dot notation

print(df['col1'][1])
print(df.col1[1])

print(df['col1'][:2])
print(df.col1[:2])

'''
Παραδείγματα δημιουργίας Πλαισίων Δεδομένων
'''

data = [['John', 25, 'Engineer'], ['JIm', 28, 'Teacher'], ['George', 42, 'Manager'], ['Mary', 51, 'Doctor']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Job'], index=['a', 'b', 'c', 'd'])

print(df)

data = [{'c1': 21, 'c2': 13}, {'c1': 8, 'c2': 22, 'c3': 20}]
df = pd.DataFrame(data, index=['Jan', 'Feb'])
print(df)

df1 = pd.DataFrame(data, index=['Jan', 'Feb'], columns=['c1', 'c2'])  # Ονόματα στηλών ίδια με τα κλειδιά του λεξικού
print(df1)

df2 = pd.DataFrame(data, index=['Jan', 'Feb'],
                   columns=['c1', 'x'])  # Όνομα στήλης διαφορετικής από τα κλειδιά του λεξικού
print(df2)

data = {'Name': pd.Series(['John', 'JIm', 'George', 'Mary']),
        'Age': pd.Series([25, 28, 42, 51]),
        'Job': pd.Series(['Engineer', 'Teacher', 'Manager', 'Doctor'])
        }

df = pd.DataFrame(data)  # Δημιουργία πλαισίου δεδομένων
print(df)

# Παράδειγμα προσθήκης νέας στήλης σε ένα υφιστάμενο πλαίσιο δεδομένων με στοιχεία από μία νέα σειρά δεδομένων

df = pd.DataFrame({'col1': [1, 3, 11, 2],
                   'col2': [9, 23, 0, 2]},
                  index=['Car A', 'Car B', 'Car C', 'Car D'])

df['col3'] = pd.Series([1, 20, 50, 100], index=['Car A', 'Car B', 'Car C', 'Car D'])

print(df)

# Προσοχή αν χρησιμοποιήσω δείκτη διαφορετικό από αυτούς στο αρχικό πλαίσιο !

df = pd.DataFrame({'col1': [1, 3, 11, 2],
                   'col2': [9, 23, 0, 2]},
                  index=['Car A', 'Car B', 'Car C', 'Car D'])

df['col3'] = pd.Series([1, 20, 50, 100], index=['Car A', 'Car B', 'Car C', 'Car E'])

print(df)

# Παράδειγμα διαγραφής στήλης πλαισίου δεδομένων

del df['col1']  # Εντολή del
print(df)

df.pop('col3')  # Εντολή pop
print(df)

# Διαγραφή γραμμών και στηλών με την εντολή drop

df = pd.DataFrame({'col1': [1, 3, 11, 2],
                   'col2': [9, 23, 0, 2]})
print(df)
print(df.drop([0, 2]))

df = pd.DataFrame({'col1': [1, 3, 11, 2],
                   'col2': [9, 23, 0, 2],
                   'col3': [0, 1, 0, 1]},
                  index=['Car A', 'Car B', 'Car C', 'Car D'])

print(df.drop(index=['Car A', 'Car C'], columns=['col2', 'col3']))

# Παράδειγμα προσθήκης πλαισίου δεδομένων σε αρχικό πλαίσιο δεδομένων

df = pd.DataFrame([[10, 20], [30, 40]], index=[1, 2], columns=['c1', 'c2'])
df2 = pd.DataFrame([[1, 2], [3, 4]], index=['a', 'b'], columns=['c1', 'c2'])

df = df.append(df2)
print(df)

# Παράδειγμα προσθήκης γραμμής στο αρχικό πλαίσιο δεδομένων
df = pd.DataFrame([[1, 2], [3, 4]], index=[1, 2], columns=['c1', 'c2'])
df2 = pd.DataFrame({'c1': [5],
                    'c2': [7]},
                   index=[3])

df = df.append(df2)
print(df)

# H εντολή clip περιορίζει τα δεδομένα σε συγκεκριμένο εύρος τιμών

df = pd.DataFrame({'col1': [1, 3, 6, 2],
                   'col2': [9, 23, 0, 5]})
print(df)

df1 = df.clip(2, 8)
print(df1)

'''
H βιβλιοθήκη pandas έχει επιπρόσθετα δικές της εντολές πρόσβασης στα δεδομένα iloc και loc που επιτρέπουν 
πιο προχωρημένες λειτουργίες.

Και στις δύο loc και iloc πρέπει να μπαίνει πρώτα η γραμμή και μετά η στήλη.

Με τη λειτουργία iloc η πρόσβαση στα δεδομένα βασίζεται σε αριθμητικούς δείκτες. Παραδείγματα:

'''

df = pd.DataFrame({'col1': [1, 3, 11, 2],
                   'col2': [9, 23,  0, 2]},
                  index=['Car A', 'Car B', 'Car C', 'Car D'])

print(df.iloc[0])  # Επιλογή της πρώτης γραμμής στο πλαίσιο δεδομένων

print(df.iloc[:, 0])  # Επιλογή της πρώτης στήλης στο πλαίσιο δεδομένων

print(df.iloc[1:3, 1])  # Επιλογής τμήματος δεδομένων

print(df.iloc[[0, 1, 3], 0])

print(df.iloc[-1:])

'''
Με τη λειτουργία loc η πρόσβαση στα δεδομένα βασίζεται σε επιλογή δεικτών/στηλών που έχουν δοθεί συγκεκριμένα ονόματα. 

Παραδείγματα:

'''
print(df.loc['Car A'])  # Επιλογή της γραμμής που αντιστοιχεί στο δείκτη 'Car A'
print(df.loc[:, 'col2'])  # Επιλογή της στλήλης που αντιστοιχεί στη στήλη με όνομα 'col2'
print(df.loc[['Car A', 'Car C'], 'col2'])  # Επιλογής τμήματος δεδομένων

'''
Έλεγχος συνθηκών στα πλαίσια/σειρές δεδομένων
'''

print(df.loc[:, 'col2'] == 0)  # Εκτυπώνει True or False

print(df.iloc[2] < 5)  # Εκτυπώνει True or False

'''
Επιλογή δεδομένων που ικανοποιούν συγκεκριμένες συνθήκες πλαισίων/σειρών δεδομένων
'''

data1 = df.loc[df.col2 >= 5]
# data1 = df.loc[df['col2']>=5]

print(data1)

data2 = df.loc[(df['col1'] >= 5) | (df['col2'] >= 5)]  # Το σύμβολο | αντιστοιχεί στη συνθήκη OR
# data2 =df.loc[(df.col1>=5) | (df.col2>=5)]

print(data2)

data3 = df.loc[(df['col1'] >= 3) & (df['col2'] >= 3)]  # Το σύμβολο & αντιστοιχεί στη συνθήκη AND
# data3 =df.loc[(df.col1>=3) & (df.col2>=3)]

print(data3)

'''
H βιβλιοθήκη pandas έχει ενσωματωμένους τους ακόλουθους τρόπους επιλογής δεδομένων με βάση των έλεγχο συνθηκών:

Η εντολή isin επιλέγει τα δεδομένα των οποίων η τιμή βρίσκεται σε λίστα τιμών: 

'''

df = pd.DataFrame({'col1': [1, 3, 11, 2, 5],
                   'col2': [9, 23, 0, 2, 10],
                   'col3': ['Price 1', 'Price 1', 'Price 2', np.nan, 'Price 3']},
                  index=['Car A', 'Car B', 'Car C', 'Car D', 'Car E'])

# Παράδειγμα: Επιλογή των δεδομένων της στήλης 'col3' τα οποία έχουν τιμές 'Price 1'ή 'Price 2']
df1 = df.loc[df.col3.isin(['Price 1', 'Price 2'])]
print(df1)

'''
Η εντολή  isnull  επιλέγει τα δεδομένα των οποίων η τιμή είναι κενή (NaN): 
'''

df2 = df.loc[df.col3.isnull()]
print(df2)

'''
Η εντολή  notnull επιλέγει τα δεδομένα των οποίων η τιμή δεν είναι κενή (NaN): 
'''

df2 = df.loc[df.col3.notnull()]
print(df2)

'''
ΑΞΟΝΕΣ
'''

df = pd.DataFrame({'col1': [1, 3, 11, 2],
                   'col2': [9, 23, 0, 2]},
                  index=['Car A', 'Car B', 'Car C', 'Car D'])

print(df)
print(df.axes)

print(list(df.axes[0]))  # Δημιουργεί λίστα με στοιχεία τα ονόματα των δεικτών των γραμμών
print(list(df.axes[1]))  # Δημιουργεί λίστα με στοιχεία τα ονόματα των δεικτών των στηλών

'''
ΠΑΡΑΔΕΙΓΜΑΤΑ ΔΙΑΧΕΙΡΙΣΗΣ ΔΕΔΟΜΕΝΩΝ ΠΟΥ ΕΧΟΥΝ ΚΕΝΗ ΤΙΜΗ
'''

df = pd.DataFrame({'col1': [1, 3, 11, 2, 5],
                   'col2': [9, 23, 0, 2, 10],
                   'col3': ['Price 1', 'Price 1', 'Price 2', np.nan, 'Price 3']},
                  index=['Car A', 'Car B', 'Car C', 'Car D', 'Car E'])

df1 = df.dropna()  # Διαγράφει όλα τα δεδομένα που έχουν κενή τιμή
print(df1)

df = pd.DataFrame({'col1': [1, 3, 11, 2, 5],
                   'col2': [9, 23, 0, 2, 10],
                   'col3': ['Price 1', 'Price 1', 'Price 2', np.nan, 'Price 3']},
                  index=['Car A', 'Car B', 'Car C', 'Car D', 'Car E'])

df2 = df.fillna('XXXXXX')  # Αντικαθιστά όλα τα δεδομένα που έχουν κενή τιμή με την τιμή που δίνεται στην παρένθεση
print(df2)

'''
Διαγραφή διπλών καταγραφών
'''

df = pd.DataFrame({'col1': [3, 1, 2, 1, 3],
                   'col2': ['Price 1', 'Price 1', 'Price 2', 'Price 1', 'Price 3']})

print(df.drop_duplicates())  # Όλα τα στοιχεία των γραμμών πρέπει να είναι ίδια για να απομακρυνθούν οι γραμμές

# Απομάκρυνση των διπλοεγγραφών για συγκεκριμένη στήλη/στήλες
df = pd.DataFrame({'col1': [1, 3, 11, 2, 5],
                   'col2': [9, 23, 0, 2, 10],
                   'col3': ['Price 1', 'Price 1', 'Price 2', 'Price 1', 'Price 3']},
                  index=['Car A', 'Car B', 'Car C', 'Car D', 'Car E'])

print(df.drop_duplicates(subset=['col3']))

#  Απομάκρυνση των διπλοεγγραφών για συγκεκριμένη στήλη/στήλες κρατώντας την τελευταία τιμή
df = pd.DataFrame({'col1': [1, 3, 11, 2, 5],
                   'col2': [9, 23, 0, 2, 10],
                   'col3': ['Price 1', 'Price 1', 'Price 2', 'Price 1', 'Price 3']},
                  index=['Car A', 'Car B', 'Car C', 'Car D', 'Car E'])

print(df.drop_duplicates(subset=['col3'], keep='last'))

'''
ENTOΛΕΣ head και tail
'''

df = pd.DataFrame({'col1': [1, 3, 11, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 11],
                   'col2': [9, 23, 0, 2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]},
                  index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'])
print(df)

print(df.head(5))  # Εμφανίζει τις πρώτες 5 γραμμές
print(df.tail(2))  # Εμφανίζει τις τελευταίες 2 γραμμές

'''
ΠΑΡΑΔΕΙΓΜΑΤΑ ΑΛΛΑΓΗΣ ΔΕΔΟΜΕΝΩΝ ΣΕ ΠΛΑΙΣΙΑ ΔΕΔΟΜΕΝΩΝ
'''
df = pd.DataFrame({'col1': [1, 3, 11, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 11],
                   'col2': [9, 23, 0, 2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]})

df.col2 = 1000  # Δίνει σε όλα τα δεδομένα της στήλης col2 την ίδια τιμή 1000
print(df)

df.col1 = df.col1.replace(1, 50)  # Αλλάζει στη στή΄λη col1 την τιμή 1 με την τιμή 50
print(df)

df.col2 = range(10, 40, 2)  # Δίνει σε όλα τα δεδομένα της στήλης col2 διαβαθμισμένες τιμές
print(df)

'''
Παράδειγματα αλλαγής ονόματος στηλών ή δεικτών με τη χρήση της εντολής rename

'''

df2 = df.rename(columns={'col1': 'NEW 1', 'col2': 'NEW 2'})
print(df2)

df3 = df.rename(index={'A': 'Auto 1', 'B': 'Auto 2'})
print(df3)

''''
ΠΡΟΣΠΕΛΑΣΗ ΣΤΟΙΧΕΙΩΝ ΜΕ ΤΙΣ ΕΝΤΟΛΕΣ iteritems(), iterrows(), itertuples()
'''

df = pd.DataFrame({'col1': [1, 2, 5, 7, 12],
                   'col2': [9, 23, 0, 2, 8],
                   'col3': ['John', 'JIm', 'George', 'George', 'Mary']},
                  index=['A', 'B', 'C', 'D', 'E'])

print(df)

# Παράδειγμα χρήσης της εντολής iteritems()
for x, item in df.iteritems():
    print(x, item)

# Παράδειγμα χρήσης της εντολής iterrows()
for x, row in df.iterrows():
    print(x, row)

# Παράδειγμα χρήσης της εντολής itertuples()
for x in df.itertuples():
    print(tuple(x))

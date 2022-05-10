import pandas as pd # recommended convention
import numpy as np

'''
ΑΝΑΔΙΟΡΓΑΝΩΣΗ ΔΕΔΟΜΕΝΩΝ

'''
df = pd.DataFrame({'col1': [1,3,11,2,5], 
                   'col2': [9,23,0,2,10],
                   'col3': ['Price 1', 'Price 1', 'Price 2', np.nan,'Price 3']},
                   index=['Car A', 'Car B', 'Car C', 'Car D','Car E'])


print(df.size) # Επιστρέφει τον αριθμό των στοιχείων του πλαισίου/σειράς δεδομένων.

print(df.shape) # Επιστρέφει tuple με τις διαστάσεις του πλαισίου δεδομένων

print(df.col1.mean()) # Υπολογισμός μέσης τιμής δεδομένων στήλης πλαισίου δεδομέων

print(df.col3.unique()) # Δίνει λίστα με τις μοναδικές τιμές στη στήλη

print(df.col3.value_counts())  # Δίνει τις μοναδικές τιμές και πόσο συχνά εμφανίζεται η κάθε τιμή

print(df.index) # Δίνει τις τιμές των δεικτών

print(df.columns) # Δίνει τις τιμές των στηλών

print(df.values) # Επιστρέφει τα δεδομένα σε μορφή διανύσματος (array) της numpy. Καλύτερα όμως χρησιμοποιήστε την εντολή df.to_numpy() 
print(type(df.values))


z=df.T  # Μετατρέπει τις γραμμές του πλαισίου δεδομένων σε στήλες
print(z)

df2 = df.copy() # Δημιουργεί αντίγραφο του πλαισίου δεδομένων

print(df2)


'''
Ανάλυση δεδομένων ως προς άξονες
'''

df = pd.DataFrame({'col1': [1,2,0,1,2], 
                   'col2': [1,1,0,2,1],
                   'col3': [1,2,1,0,0]},
                   index=['A', 'B', 'C', 'D', 'E'])

print(df)


#Παράδειγμα αθροίσματος των τιμών όλων των γραμμών για κάθε στήλη (άθροισμα ως προς τον άξονα 0)  
print(df.sum(0)) # Η τιμή του άξονα=0 είναι η προεπιλεγμένη τιμή δηλαδή είναι ίδιο με: print(df.sum(0))

#Παράδειγμα αθροίσματος των τιμών όλων των στηλών για κάθε γραμμή (άθροισμα ως προς τον άξονα 1)  
print(df.sum(1))

# Aντίστοιχα για τη μέση τιμή
print(df.mean()) # Η τιμή του άξονα=0 είναι η προεπιλεγμένη τιμή 
print(df.mean(1))


'''
Χρήσιμες συναρτήσεις:

count() 	Αριθμός των μη μηδενικών στοιχείων
sum() 	    Άθροισμα τιμών 
mean() 	    Μέση τιμή των τιμών 
median() 	Ενδιάμεση τιμή 
std() 	    Τυπική απόκλιση
min() 	    Ελάχιστη τιμή 
max() 	    Μέγιστη τιμή
prod() 	    Γινόμενο τιμών
cumsum() 	Συσσωρευτικό άθροισμα
cumprod() 	Συσσωρευτικό γινόμενο

'''


print(df.describe())    # Γενική σύνοψη στατιστικών αποτελεσμάτων πλαισίου δεδομένων

print(df.col1.describe())  # Γενική σύνοψη στατιστικών αποτελεσμάτων στήλης πλαισίου δεδομένων

'''
Παράμετροι στην εντολή describe

number − Συνοψίζει τις στήλες με αριθμούς (Default τιμή) 
object − Συνοψίζει τις στήλες με συμβολοσειρές
all − Συνοψίζει όλες τις στήλες
'''

df = pd.DataFrame({'col1': [1,2,5,7,12], 
                   'col2': [9,23,0,2,8],
                   'col3': ['John','JIm','George','George','Mary']},
                   index=['A', 'B', 'C', 'D', 'E'])


print(df.describe(include='number')) # Ίδιο με : print(df.describe())
print(df.describe(include='object'))
print(df.describe(include='all'))


''' 
Παραδείγματα εφαρμογής της εντολής aggregate (agg)
'''


df = pd.DataFrame({'col1': [1,2,8], 
                   'col2': [1,1,5],
                   'col3': [1,2,1]},
                   index=['A', 'B', 'C'])

# Παραδείγματα εφαρμογής περισσότερων από μία συναρτήσεων στο Πλαίδιο δεδομένων
print(df)
# Με την εντολή aggregate μπορούμε να εφαρμόσουμε διαφορετικές συναρτήσεις σε διαφορετικές στήλες 
print(df.agg({'col1' : ['sum', 'min'], 'col2' : ['min', 'max']}))


'''
ΑΝΑΛΥΣΗ ΔΕΔΟΜΕΝΩΝ ΜΕ ΧΡΗΣΗ ΟΜΑΔΟΠΟΙΗΣΗΣ (groupby)

'''

df = pd.DataFrame({'col1': [1,1,1,2,2,3,3,5,4,11],
                   'col2': [9,9,0,2,0,0,2,5,4,1],
                   'col3': [2,5,8,2,0,2,2,5,4,1]})

print(df)

print(df.describe())

print(df.groupby('col1').col1.count()) # Δίνει τα ίδια αποτελέσματα όπως η εντολή: df.col1.value_counts()

#print(df.col1.value_counts())


# Για κάθε μία από τα στοιχεία των ομάδων της στήλης col1 δίνει την ελάχιστη τιμή που αντιστοιχεί στα στα στοιχεία της στήλης col2
print(df.groupby('col1').col2.min())


print(df.groupby('col1').col2.max()) # Αντίστοιχα δίνει την μέγιστη τιμή 
print(df.groupby('col1').col2.sum()) # Αντίστοιχα δίνει το άθροισμα των τιμών 
print(df.groupby('col1').col2.mean()) # Αντίστοιχα δίνει τη μέση τιμή 
print(df.groupby('col1').col2.std()) # Αντίστοιχα δίνει την τυπική απόκλιση 

'''
Παράδειγμα ανάλυσης δεδομένων με την εντολή .groupby σε πολλαπλά επίπεδα:
'''
print(df.groupby(['col1', 'col2']).col3.max())

'''
Παράδειγμα λήψης συγκεκριμένης ομάδας σε ξεχωριστό DataFrame:
'''
grp=df.groupby('col1')
data=grp.get_group(1)

print(data)

'''
Παράδειγμα δημιουργίας νέας στήλης δεδομένων από υπάρχουσες τιμές δεδομένων από διάφορες στήλες με τη χρήση 
της εντολής eval :
'''


df['Eval_col']=df.eval('col1+col2+2*col3')
print(df)



'''
Παραδείγματα χρήσης της εντολής apply :
'''

df = pd.DataFrame({'col1': [1,1,1,2,2,3,3,5,4,11], 
                   'col2': [9,9,0,2,0,0,2,5,4,1],
                   'col3': [2,5,5,2,3,2,2,5,4,1]})

print(df.apply(np.sqrt))
print(df.apply(lambda x: x.max() - x.min(), axis=0))

print(df['col1'].apply(lambda x:x*100))
print(df.apply(lambda x:x+2))


'''
Παραδείγματα χρήσης της εντολής pipe :
'''

def func (x1):
    return x1*10

def func2 (x1,x2):
    return x1*x2

print(df.pipe(func)) # π.χ. πολλαπλασιάζει όλα τα στοιχεία του πλαισίου δεδομένων με τον αριθμό 10

n=3
print(df.pipe(func2,n)) # π.χ. πολλαπλασιάζει όλα τα στοιχεία του πλαισίου δεδομένων με τον αριθμό n

'''
ΤΑΞΙΝΟΜΗΣΗ ΣΤΟΙΧΕΙΩΝ ΠΛΑΙΣΙΩΝ ΔΕΔΟΜΕΝΩΝ
'''

df = pd.DataFrame({'col2': [1,3,11,2,1,1,1,1,1,0,0,0,0,0,11],
                   'col1': [9,23,0,2,1,1,1,1,0,1,1,1,1,1,0],
                   'col3': [19,2,0,3,5,7,0,1,0,1,2,1,2,1,0]},
                    index=['A','C','B','E','F','D','G','H','I','J','K','L','M','N','O'])
print(df)


# Ταξινόμηση με βάση τους δείκτες των γραμμών
df1=df.sort_index()
print(df1)

df2=df.sort_index(ascending=False) # Φθίνουσα σειρά
print(df2)

# Ταξινόμηση με βάση τους δείκτες των στηλών

df3=df.sort_index(axis=1)
print(df3)


# Ταξινόμηση με βάση τις τιμές

df = pd.DataFrame({'col1': [1,3,1,2,1,1,1,1,1,0,0,0,0,0,1],
                   'col2': [9,23,0,2,1,1,1,1,0,1,1,1,1,1,0],
                   'col3': [19,2,0,3,5,7,0,1,0,1,2,1,2,1,0]},
                    index=['A','C','B','E','F','D','G','H','I','J','K','L','M','N','O'])
print(df)

df4 = df.sort_values(by='col2', ascending=False)
print(df4)


df = pd.DataFrame({'col1': [1,3,1,2,1,1,1,1,1,0,0,0,0,0,1],
                   'col2': [9,23,0,2,1,1,1,1,0,1,1,1,1,1,0],
                   'col3': [19,2,0,3,5,7,0,1,0,1,2,1,2,1,0]},
                    index=['A','C','B','E','F','D','G','H','I','J','K','L','M','N','O'])

df4 = df.sort_values(by=['col2','col3'], ascending=False)
print(df4)


'''
Reindex στα πλαίσια δεδομένων
'''


df = pd.DataFrame({'col1': [1,2,5,7,12], 
                   'col2': [9,23,0,2,8],
                   'col3': ['John','JIm','George','George','Mary']},
                   index=['A', 'B', 'C', 'D', 'E'])
print(df)


dfr = df.reindex(index=['A', 'B', 'C', 'H'], columns=['col1', 'col3', 'col8'])
print (dfr)


# Μπορούμε να συμπληρώσουμε τα κενά κελιά με συγκεκριμένη τιμή
df = pd.DataFrame({'col1': [1,2,5,7,12], 
                   'col2': [9,23,0,2,8],
                   'col3': ['John','JIm','George','George','Mary']},
                   index=['A', 'B', 'C', 'D', 'E'])

dfr = df.reindex(index=['A', 'B', 'C', 'H'], columns=['col1', 'col3', 'col8'], fill_value=100)
print (dfr)


# Μπορούμε να συμπληρώσουμε τα κενά κελιά με συγκεκριμένη μέθοδο π.χ. ffill (γεμίζει τα κελιά με την προηγούμενη τιμή)
df = pd.DataFrame({'col1': [1,2,5,7,12], 
                   'col2': [9,23,0,2,8],
                   'col3': ['John','JIm','George','George','Mary']},
                   index=['A', 'B', 'C', 'D', 'E'])

dfr = df.reindex(index=['A', 'B', 'C', 'H',], columns=['col1', 'col3', 'col8'], method='ffill')
print (dfr)


#reindex_like ενός μεγάλου πλαισίου δεδομένων σε μικρότερο
df1 = pd.DataFrame({'col1': [1,2,5,7,12], 
                   'col2': [9,23,0,2,8],
                   'col3': ['John','JIm','George','George','Mary']},
                   index=['A', 'B', 'C', 'D', 'E'])


df2 = pd.DataFrame({'col1': [1,2,5], 
                   'col2': [9,23,0],},
                   index=['A', 'B', 'C'])


df1 = df1.reindex_like(df2)
print (df1)


#reindex_like ενός μικρού πλαισίου δεδομένων σε μεγαλύτερο (δημιουργούνται κενά κελιά)
df1 = pd.DataFrame({'col1': [1,2,5,7,12], 
                   'col2': [9,23,0,2,8],
                   'col3': ['John','JIm','George','George','Mary']},
                   index=['A', 'B', 'C', 'D', 'E'])


df2 = pd.DataFrame({'col1': [1,2,5], 
                   'col2': [9,23,0],},
                   index=['A', 'B', 'C'])

df2 = df2.reindex_like(df1)
print (df2)

# Συμπλήρωση των κενών κελιών με την τιμή του προηγούμενου κελιού method='ffill' / method='pad'

df1 = pd.DataFrame({'col1': [1,2,5,7,12], 
                   'col2': [9,23,0,2,8],
                   'col3': ['John','JIm','George','George','Mary']})


df2 = pd.DataFrame({'col1': [1,2,5], 
                   'col2': [9,23,0]})
                   

print (df2.reindex_like(df1,method='ffill'))

# Συμπλήρωση των κενών κελιών με την τιμή του επόμενου κελιού method='bfill' / method='backfill'


df1 = pd.DataFrame({'col1': [1,2,5,7,12], 
                   'col2': [9,23,0,2,8],
                   'col3': ['John','JIm','George','George','Mary']},
                   index=['A', 'B', 'C', 'D', 'E'])


df2 = pd.DataFrame({'col2': [11,15,4], 
                   'col3': [2,2,3],},
                   index=['C', 'D', 'E'])
                          
print (df2.reindex_like(df1,method='bfill'))
                          

# Συμπλήρωση των κενών κελιών για περιορισμένο αριθμό διαδοχικών συμπληρώσεων

df1 = pd.DataFrame({'col1': [1,2,5,7,12], 
                   'col2': [9,23,0,2,8],
                   'col3': ['John','JIm','George','George','Mary'],
                   'col4': [12,2,10,12,8]})


df2 = pd.DataFrame({'col1': [1,2,5], 
                   'col2': [9,23,0]})
                   

print (df2.reindex_like(df1,method='ffill', limit=1))
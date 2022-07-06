import os

print(os.getcwd()) # Εκτυπώνει ως συμβολοσειρά τον τρέχοντα φάκελο εργασίας 

os.chdir('C:/Users/despo_000/Desktop/Φροντ 2022') # Αλλάζει το φάκελο εργασίας
print(os.getcwd())


print(os.listdir()) # Δείχνει τους φακέλους και τα αρχεία στο φάκελο εργασίας

os.mkdir('svisto') # Δημιουργεί νέο φάκελο στο φάκελο εργασίας
print(os.listdir())

os.rmdir('svisto') # Απομακρύνει έναν άδειο φάκελο
print(os.listdir())


#os.rename('svisto','svisto_new') # Μετονομάζει ένα φάκελο ή ένα αρχείο
#os.rename('untitled6.py','new.py')

#print(os.listdir())


print('*************************')
#os.remove('testsvisto.txt') # Διαγράφει ένα αρχείο
#print(os.listdir())


# Παράδειγμα συνένωσης διαδρομής με την εντολή os.path.join

#path ='C:/Users/despo_000/Desktop/Φροντ 2022' # ορίζουμε π.χ. τη διαδρομή

#filename= 'test_read.txt' # Δίνουμε το όνομα του αρχείου που θέλουμε να ανοίξουμε
#fullpath = os.path.join(path,filename)
#print(fullpath)

#with open(fullpath, 'r') as tr:
#    x = tr.read()

#print(x)


#print(os.path.exists(fullpath)) # Εκτυπώνει True/False αν υπάρχει η διαδρομή του αρχείου/φακέλου

# Παράδειγμα διαγραφής αρχείου
path ='C:/Users/despo_000/Desktop/Φροντ 2022' # ορίζουμε τη διαδρομή βρίσκεται το αρχείο
f= 'test_remove.txt' # Το όνομα του αρχείου που θέλουμε να σβήσουμε

fullpath = os.path.join(path,f)
print(fullpath)

if os.path.exists(fullpath):  # Έλεγχος αν υπάρχει το αρχείο στην παραπάνω διαδρομή)
    os.remove('test_remove.txt')
    print("File '{}' removed".format(f))
else:
    print('File does not exist!!!')



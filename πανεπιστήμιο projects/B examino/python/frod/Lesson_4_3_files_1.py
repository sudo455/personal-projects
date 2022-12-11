'''
                  ΔΙΑΧΕΙΡΙΣΗ ΑΡΧΕΙΩΝ

Τρόποι ανοίγματος αρχείων

r	Ανάγνωση (Read)
w 	Εγγραφή (write) -  Διαγραφή τυχόν προηγούμενων περιεχομένων
r+	Άνοιγμα αρχείου για Ανάγνωση/Εγγραφή
a	Προσθήκη (append) - Διατήρηση τυχόν προηγούμενων περιεχομένων
x   Δημιουργεί αρχείο - Επιστρέφει σφάλμα αν υπάρχει το αρχείο
b	Αρχείο δυαδικής μορφής
+	Προσθήκη δεδομένων στο τέλος του αρχείου

Αν δεν επιλεγεί κάποια παράμετρος, λαμβάνεται η τυπική τιμή 'r'

'''

f = open('/home/angelosmoraitis/Documents/projects/github/personal-projects/πανεπιστήμιο projects/B examino/python/frod/test_read.txt', 'r')

print(f)  # Εκτυπώνει το αντικείμενο του αρχείου f

for line in f :     # Εκτυπώνει το αρχείο ανά γραμμ΄΄η
    print (line)

f.close()


with open('/home/angelosmoraitis/Documents/projects/github/personal-projects/πανεπιστήμιο projects/B examino/python/frod/test_read.txt', 'r') as f: #Καλ΄΄υτερος τρόπος ανοίγματος αρχείων με εντολή with open
    for line in f :     # Εκτυπώνει το αρχείο ανά γραμμ΄΄η
        print (line)


with open('/home/angelosmoraitis/Documents/projects/github/personal-projects/πανεπιστήμιο projects/B examino/python/frod/test_read.txt', 'r') as f: #Καλ΄΄υτερος τρόπος ανοίγματος αρχείων με εντολή with open
    x = f.read()  # Διαβάζει το αρχείο
    
print(x)
print(len(x.split())) # Εκτυπώνει τον αριθμό των λέξεων του κειμένου

#with open('C:/Iordanis/IONIO_WORK/Python/TEST/test_read.txt', 'r') as f: # Ανοίγει το αρχείο aπό άλλη διαδρομή
#    x = f.read()  # Διαβάζει το αρχείο 

print(x)

with open('/home/angelosmoraitis/Documents/projects/github/personal-projects/πανεπιστήμιο projects/B examino/python/frod/test_read.txt', 'r') as f:  
    file = f.readline()    # Εκτυπώνει την πρώτη γραμμή
    print(file)
    file = f.readline()    # Εκτυπώνει την δεύτερη γραμμή
    print(file)


with open('/home/angelosmoraitis/Documents/projects/github/personal-projects/πανεπιστήμιο projects/B examino/python/frod/test_read.txt', 'r') as f:
    file = f.readline(11)  # Εκτυπώνει τους πρώτους 11 χαρακτήρες
    print(file)
    file = f.readline(1000)
    print(file)
    file = f.readline(10)
    print(file)

with open('/home/angelosmoraitis/Documents/projects/github/personal-projects/πανεπιστήμιο projects/B examino/python/frod/test_read.txt', 'r') as f:
    file = f.readlines()   # Εκτυπώνει σε λίστα, με στοιχεία της λίστας τις γραμμές του αρχείου
    print(file)
    print(file[2]) # Εκτυπώνει τη γραμμή με δείκτη 2
    print(len(file)) # Εκτυπώνει τον αριθμό των γραμμών
    print(len(file[1]))
    
    new_text = []     # Απομακρύνουμε τον χαρακτήρα \n που εμφανίζεται
    for line in file:
        if line[-1] =='\n':
            new_text.append(line[:-1])
        else:
            pass

print(file)
print(new_text)


with open('test_read.txt', 'r') as f:
    file = f.readlines()    
    new_text_2 = []
    for line in file:
        new_text_2.append(line.strip())  # Καλύτερος τρόπος απομάκρυνσης του χαρακτήρα \n
  
print(new_text_2)

print(len(new_text_2))  # Υπολογίζει των αριθμών των γραμμών
print(new_text_2[1])
print(len(new_text_2[1]))


print('*****************')
for x,line in enumerate(file):
    print(x, len(line), len(line.split())) # Εκτύπωση αριθμού γραμμής, αριθμού χαρακτήρων και λέξεων κάθε γραμμής


print('***************************')   

with open('test_read.txt', 'r') as f:
    Read_point = 5
    
    contents = f.read(Read_point)  # Διαβάζει τους πρώτους "Read_point" χαρακτήρες
    print(contents)
    print(f.tell()) #Eπιστρέφει την τρέχουσα θέση στο αρχείο
   
    contents = f.read(Read_point)   # Διαβάζει τους επόμενους "Read_point" χαρακτήρες
    print(contents)
    print(f.tell())
       
    f.seek(0)                    # Μετά από την εντολή αυτή διαβάζει ξανά από την αρχή
    contents = f.read(Read_point)   # Διαβάζει τους επόμενους "Read_point" χαρακτήρες
    print(contents)

    
    while len(contents) > 0 :        # Χωρίζει το κείμενο σε κάθε "Read_point" χαρακτήρες
        print(contents, end='//')
        contents = f.read(Read_point)




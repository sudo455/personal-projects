new_text = []     # Απομακρύνουμε τον χαρακτήρα \n που εμφανίζεται
    for line in file:
        if line[-1] =='\n':
            new_text.append(line[:-1])
        else:
            pass

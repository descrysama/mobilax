

def thread_asking():
    thread_amount = None;
    try:
        while thread_amount == None or thread_amount == 0 or thread_amount > 5 or thread_amount < 0 :
            thread_amount = int(input('Choisissez un nombre de thread (max : 5) : '))

        print("script initialisé avec", thread_amount, "threads" if thread_amount > 1 else "thread")
    except:
        print("entrez uniquement des chiffres")
        thread_asking()
    
    return thread_amount
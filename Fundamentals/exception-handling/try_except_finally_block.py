acronyms = {'LOL': 'laugh out loud',
            'IDK': "I don't Know",
            'TBH': 'to be honest'}
acronym = 'BTW'

# defi = acronyms[acronym]    # KeyError: 'BTW'
try:
    defi = acronyms[acronym]
    print('Definiton of', acronym, 'is', defi)
except:
    print("The key ", acronym, "doesn't exist")
finally:
    print("The acronyms we defined are:")
    for acronym in acronyms:
        print(acronym)

print("The program keeps going....")

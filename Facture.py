#create a function with parameters
def facture(price):
    #define variables
    babacar = 12
    ismaila = 7
    ndiaye = 7
    maty = 16
    totalpoints = 42
    #create a map
    map = {
        "babacar": babacar,
        "ismaila": ismaila,
        "ndiaye": ndiaye,
        "maty": maty   
    }
    print("Voici ci-dessous le montant que chaque personne doit payer:")
    #reach each value in the map
    for key, value in map.items():
        
        amount = price * value / totalpoints
        #print the value
        
        print(key, " = ", amount)

#call the function
facture(15000)
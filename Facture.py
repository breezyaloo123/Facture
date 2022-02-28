

#create a function with parameters
def facture(price):
    #define variables
    babspoints = 12
    ismaila = 7
    ndiaye = 7
    maty = 16
    totalpoints = 42
    #create a map
    map = {
        "babspoints": babspoints,
        "ismaila": ismaila,
        "ndiaye": ndiaye,
        "maty": maty   
    }
    #reach each value in the map
    for key, value in map.items():
        #print the value
        res = price * value / totalpoints
        print(key, ":", res)

#call the function
facture(13200)
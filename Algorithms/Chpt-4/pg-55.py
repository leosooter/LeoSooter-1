#Practice re-creating some algorithms in python- runs 50ms faster than identical javascript

animal = ["baboon","lion","leopard","bunny","hippo","hyena","buffalo","warthog","giraffe"]
danger = ["low","high","medium","none","highest","low","high","low"]

def zip_map(key_array, value_array):
    newDict = {}
    count = len(key_array)
    if(len(key_array) > len(value_array)):
        count = len(value_array)
    for index in range(0, count):
        newDict[key_array[index]] = value_array[index]
    return newDict


canIPetIt = zip_map(animal, danger)

for key in canIPetIt:
    print "\n", key , " | ", canIPetIt[key]
    if canIPetIt[key] is "none":
        print "You can pet it!"

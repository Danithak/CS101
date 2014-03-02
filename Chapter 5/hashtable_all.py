#!/usr/bin/python


# NOTE: This is a collection of all hash functions using lists throughout the video lectures in Chapter 5.
# The whole purpose of the lesson was to take a deep dive into how dictionaries function, as all of the
# functions created here are more or less inherent properties of dictionaries. 

def hashtable_add(htable,key,value):
    position = hash_string(key,len(htable))       # This function uses the same method to look up where
    htable[position].append([key, value])         # a keyword would fit into a bucket, and places it inside
    return htable  
    
    
def hashtable_get_bucket(htable,keyword):              # This function derives the hash value and returns
    return htable[hash_string(keyword,len(htable))]    # the appropriate bucket (list inside the list)


def hashtable_lookup(htable,key):                   
    bucket = hashtable_get_bucket(htable, key)      # This function finds the bucket that a key would be in     
    for i in bucket:                                # using the above function and then checks each key inside
        if key in i:                                # the bucket to see if it exists. It returns the value 
            return i[1]                             # associated with the key if it exists, and returns None if not. 
        else:
            None


def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)       # This function is very similar to the one above,
    for entry in bucket:                            # except that it will add the key with the value
        if key in entry:                            # if it does not exist, or update the 
            entry[1] = value                        # value if the key already exists.
            return htable
    hashtable_add(htable, key, value)

def hash_string(keyword,buckets):           # This function hashes keys into specific buckets by 
    out = 0                                 # looping through each character, adding the ordinal value to out,
    for s in keyword:                       # then taking the modulo of out, and returning out after it terminates.
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):               # This functiona simply creates a list with n number of lists
    table = []                              # inside. 
    for unused in range(0,nbuckets):
        table.append([])
    return table

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]


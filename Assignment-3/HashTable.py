import time
import random

class HashTable:

    def __init__(self, hashTableSize, collisionTechnique):
        self.hashTableSize, self.collisionsCount, self.probeLength, self.hashTable, self.collisionTechnique = hashTableSize, 0, 0, [() for _ in range(hashTableSize)], collisionTechnique

    # Get the value. Raise a KeyError if the key does not exist
    def __getitem__(self, key):
        for keyValuePairData in self.hashTable:
            if keyValuePairData != () and keyValuePairData[0] == key:
                return keyValuePairData[1]
        raise KeyError(key)

    # Insert the value. Raise a KeyError if the key does not exist
    def __setitem__(self, key, value):
        hashValue = self.hash(key)
        for hashTableIndex in range(self.hashTableSize):
            if self.hashTable[hashValue] == () or self.hashTable[hashValue][0] == key:
                self.hashTable[hashValue] = (key, value)
                self.probeLength = self.probeLength + hashTableIndex + 1
                return
            hash2 = 1 #linearProbing
            # Implementing quadratic probing
            if self.collisionTechnique == 'quadraticProbing' : hash2 = hashTableIndex * hashTableIndex
            # Implementing double hashing
            elif self.collisionTechnique == 'doubleHashing' : hash2 = 7 - (sum(ord(char) for char in key) % 7)
            self.collisionsCount, hashValue = self.collisionsCount + 1, (hashValue + hash2) % self.hashTableSize
        raise Exception(key)

    # Returns True if the key is in the table and False otherwise.
    def __contains__(self, key):
        for keyValuePairData in self.hashTable:
            if keyValuePairData != () and keyValuePairData[0] == key:
                return True
        return False

    # Calculates the hash value for the given key.
    def hash(self, key):
        hashValue = sum((ord(char) << (5 * index)) + index for index, char in enumerate(key)) % self.hashTableSize
        return hashValue

def main():

    """ sample testcases to test whether all functions working or not """
    
    ht = HashTable(3,'linearProbing') # for testing other collision techniques, replace 'linearProbing' with 'quadraticProbing' or 'doubleHashing'.

    ht['abactinally'] = 6
    ht['peevishness'] = 4
    ht['giantism'] = 3
    # uncomment below to test "Raise an exception if the hash table is full and the key does not exist in the table yet"
    # ht['rotovated'] = 8

    print(ht['giantism'])
    print(ht['peevishness'])
    print(ht['abactinally'])
    # uncomment below to test "Raise a KeyError if the key does not exist"
    # print(ht['nonpareil'])

    print(ht.__contains__('peevishness'))
    print(ht.__contains__('djeifhfiw'))

    """
    # uncomment to test the question 2 and 3
    start_time = time.time()

    # Add key-value pairs to the hash table until it is full
    ht = HashTable(200000,'linearProbing') # for testing other collision techniques, replace 'linearProbing' with 'quadraticProbing' or 'doubleHashing'.

    keys = []

    with open("english_large.txt", encoding="utf-8-sig") as f:
        for line in f: 
            key, ht[key] = line.strip(), random.randint(0, 30)
            keys.append(key)

    end_time = time.time()

    print(ht.hashTable)
    print("probe length : ",ht.probeLength)
    print("Average probe length : ",(ht.probeLength / len(keys)))
    print("Collisions : ",ht.collisionsCount)

    print(f"Time taken for reading the file and inserting key value pairs in hashtable: {end_time - start_time} seconds")
    """

if __name__ == "__main__":
    main()
class HashTable:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, value):
        hashvalue = self.hashfunction(key, len(self.keys))

        if self.keys[hashvalue] is None:
            self.keys[hashvalue] = key
            self.values[hashvalue] = value
        else:
            if self.keys[hashvalue] == key:
                self.values[hashvalue] = value  # replace the old value
            else:
                nexthash = self.rehash(hashvalue, len(self.keys))
                while self.keys[nexthash] is not None and self.keys[nexthash] != key:
                    nexthash = self.rehash(nexthash, len(self.keys))
                if self.keys[nexthash] is None:
                    self.keys[nexthash] = key
                    self.keys[nexthash] = value
                else:
                    self.keys[nexthash] = value  # replace the old value

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        start = self.hashfunction(key, len(self.keys))
        value = None
        stop = False
        found = False
        position = start
        while self.keys[position] is not None and not found and not stop:
            if self.keys[position] == key:
                found = True
                value = self.values[position]
            else:
                position = self.rehash(position, len(self.keys))
                if position == start:
                    stop = True
        return value

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"

    print(H.keys)
    print("_____________________")
    print(H.values)

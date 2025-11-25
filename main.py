class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, mystr):
        return sum(ord(c) for c in mystr)

    def add(self, key, value):
        collectiontoadd = {key: value}
        if self.hash(key) not in self.collection:
            self.collection[self.hash(key)] = collectiontoadd
        else:
            self.collection[self.hash(key)].update(collectiontoadd)
    
    def remove(self, key):
        if self.hash(key) in self.collection:
            del self.collection[self.hash(key)][key]

    def lookup(self, key):
        if self.hash(key) not in self.collection:
            return None
        else:
            return self.collection[self.hash(key)][key]

# Apply Usage Examples
myhashtable = HashTable()
myhashtable.add('golf','sport')
print(myhashtable.collection)
myhashtable.add('dear', 'friend')
myhashtable.add('read', 'book')
print(myhashtable.collection)
myhashtable.remove('read')
print(myhashtable.collection)
print(myhashtable.lookup('torch'))
print(myhashtable.lookup('golf'))
myhashtable.add('rose','flower')
print(myhashtable.collection)
myhashtable.add('fcc','coding')
myhashtable.add('cfc','chemical')
print(myhashtable.collection)

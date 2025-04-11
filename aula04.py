class HashItem:
    def __init__ (self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__ (self, size):
        self.size = size
        self.slots = [None for i in range (0, size)]
        self.count = 0

    def hash (self, s):
        mult = 1
        hash_value = 0

        for c in s:

            hash_value = hash_value + mult * ord(c)
            mult +=1
        return hash_value
    
    def put (self, key, value):
        
        hi = HashItem(key, value)
        hv = self.hash(key) % self.size

        while self.slots[hv] != None:
            hv = (hv + 1) % self.size

        self.slots[hv] = hi
        self.count += 1
        self.check_growth()

    def get (self, key, value):
        hv = self.hash(key) % self.size

        while self.slots[hv] != None:
            if self.slots[hv].key == key:
                return self.slots[hv].value
            hv = (hv + 1) % self.size
        return None
    
    def growth(self):
        new_table = HashTable(self.size * 2)
        for i in range (0, self.size):
            if self.slots[i] != None:
                new_table.put (self.slots[i].key, self.slots[i].value)

            self.size = self.size * 2
            
    def check_growth(self):
        fator_carga = self.count / self.size
        if fator_carga > 0.65:
            print ("aumentando o tamanho da tabela...")
            self.growth()
        
        
            

    

init python:

    class Player:
        def __init__(self, atb1, atb2, atb3, atb4):
            self.atb1 = atb1
            self.max_atb1 = atb1
            self.atb2 = atb2
            self.max_atb2 = atb2
            self.atb3 = atb3
            self.max_atb3 = atb3
            self.atb4 = atb4
            self.max_atb4 = atb4

        def addAtb1(self, amount):
            self.atb1 += amount
            if self.atb1 > self.max_atb1:
                self.atb1 = self.max_atb1
        
        def addAtb2(self, amount):
            self.atb2 += amount
            if self.atb2 > self.max_atb2:
                self.atb2 = self.max_atb2
        
        def addAtb1(self, amount):
            self.atb3 += amount
            if self.atb3 > self.max_atb3:
                self.atb3 = self.max_atb3
        
        def addAtb1(self, amount):
            self.atb4 += amount
            if self.atb4 > self.max_atb4:
                self.atb4 = self.max_atb4
    
        
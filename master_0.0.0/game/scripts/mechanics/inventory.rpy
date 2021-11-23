init python:
    
    class InventoryItem:
        def __init__(self, img, value):
            self.img = img
            self.value = value

  
    class KeyItem(InventoryItem):
        def __init__(self, img):
            InventoryItem.__init__(self, img, 0)
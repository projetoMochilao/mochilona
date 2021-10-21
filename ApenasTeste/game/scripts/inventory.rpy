init python:
    
    class InventoryItem:
        def __init__(self, img, value):
            self.img = img
            self.value = value

    class Consumable(InventoryItem):
        def __init__(self, img, value, hp_gain, mp_gain):
            InventoryItem.__init__(self, img, value)
            self.hp_gain = hp_gain
            self.mp_gain = mp_gain

        def use(self, target):
            inventory.remove(self)
            target.addHP(self.hp_gain)
            target.addMP(self.mp_gain)
            global selected_item
            selected_item = None
  
    class KeyItem(InventoryItem):
        def __init__(self, img):
            InventoryItem.__init__(self, img, 0)
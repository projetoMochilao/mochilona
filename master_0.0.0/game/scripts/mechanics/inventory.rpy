init python:
    
    class InventoryItem:
        def __init__(self, img, value):
            self.img = img
            self.value = value

    class Consumable(InventoryItem):
        def __init__(self, img, value, atb1_gain, atb2_gain, atb3_gain, atb4_gain):
            InventoryItem.__init__(self, img, value)
            self.atb1_gain = atb1_gain
            self.atb2_gain = atb2_gain
            self.atb3_gain = atb3_gain
            self.atb4_gain = atb4_gain

        def use(self, target):
            inventory.remove(self)
            target.addAtb1(self.atb1_gain)
            target.addAtb2(self.atb2_gain)
            target.addAtb3(self.atb3_gain)
            target.addAtb4(self.atb4_gain)

            global selected_item
            selected_item = None
  
    class KeyItem(InventoryItem):
        def __init__(self, img):
            InventoryItem.__init__(self, img, 0)
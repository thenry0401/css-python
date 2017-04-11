
# coding: utf-8

# In[1]:

from character import Character


# In[ ]:

class IceMonster(Character):
    def get_damaged(self, attack_power, attack_kind):
        if attack_kind == "ICE":
            self.hp += attack_power
        else:
            self.hp -= attack_power
        
    def __str__(self):
        return "Ice Monster's HP : {}".format(self.hp)

class FireMonster(Character):
    def get_damaged(self, attack_power, attack_kind):
        if attack_kind == "FIRE":
            self.hp += attack_power
        else:
            self.hp -= attack_power

    def __str__(self):
        return "Fire Monster's HP : {}".format(self.hp)


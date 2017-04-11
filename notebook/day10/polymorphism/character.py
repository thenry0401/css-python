
# coding: utf-8

# In[ ]:

# abstract_class : 객체를 만들 수 없는 클래스
#                  기본 클래스, 부모 클래스의 역할을 한다
#                  게임으로 따지면, 여러 캐릭터들이 공통적으로 가지는 속성 그 밑으로 상속받아서 여러 캐릭터를 만듬


from abc import * # abstract base class

class Character(metaclass = ABCMeta):
    def __init__(self):
        self.hp = 100
        self.attack_power = 20
        
    def attack(self, other, attack_kind):
        other.get_damaged(self.attack_power, attack_kind)
        
    @abstractmethod    # 앱스트랙트메소드를 쓰면: 이 클래스는 객체를 생성할순없지만, 이 클래스를 상속받는 클래스들은 이 밑의 메소드들을 구현해야한다는 뜻
    def get_damaged(self, attack_power, attack_kind):
        pass
        
    


from evaluate import Evaluate
import pickle
import math

class DataHandler:
    #클래스 멤버: 연산기 하나
    evaluator = Evaluate()
        
    #class method : 전역함수처럼 쓸 수 있다
    @classmethod
    def GetRawdataInDic(cls, filename):
        rawdata = {}
        with open(filename, 'rb') as f:
            while 1:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
            
                rawdata.update(data)
              
        return rawdata
    
    def __init__(self, filename, clsname):
        self.rawdata = DataHandler.GetRawdataInDic(filename)
        self.clsname = clsname
        
        #연산한 값을 저장해두는 저장소
        #필요할 떄 연산하되, 이미 연산된 값이면 연산없이 저장된 값을 반환
        self.cache = {}
        
    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())
        return self.cache.get('scores')
        
    #cache    
    def get_average(self):
        if 'average' not in self.cache:
            self.cache['average'] = self.evaluator.average(self.get_scores())
        return self.cache.get('average')
    
    def get_variance(self):
        if 'variace' not in self.cache:
            vari = round(self.evaluator.variance(self.get_scores(), self.get_average()))
            self.cache['variance'] = vari
        return self.cache.get('variance')
        
    def get_standard_deviation(self):
        if "standard_deviation" not in self.cache:
            std_dev = round(math.sqrt(self.get_variance()), 1)
            self.cache["standard_deviation"] = std_dev
            return self.cache.get("standard_deviation")


    def WhoIsHighest(self):
        if 'highest' not in self.cache:
            self.cache['highest'] = reduce(lambda a ,b:
                                           a if self.rawdata.get(a) > self.rawdata.get(b) else b,
                                           self.rawdata.keys()
                                           )
        return self.cache.get('highest')
        
    def GetHighestScore(self):
        return self.rawdata[self.WhoIsHighest()]
        
    def WhoIsLowest(self):
        if "lowest" not in self.cache:
            self.cache['lowest'] = reduce(lambda a, b:
                                          a if self.rawdata.get(a) < self.rawdata.get(b) else b,
                                          self.rawdata.keys()
                                          )
        return self.cache.get('lowest')
        
    def GetLowestScore(self):
        return self.rawdata[self.WhoIsLowest()]




    
    
    def get_evaluation(self):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print("{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".\
              format(self.clsname, self.get_average(), self.get_variance()\
                     , self.get_standard_deviation()))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        self.evaluateClass()

    def evaluateclass(self):
        avrg = self.get_average()
        std_dev = self.get_standard_deviation()
        
        if avrg <50 and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > 50 and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < 50 and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > 50 and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")
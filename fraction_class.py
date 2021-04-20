import sys
import os
class fraction:
    def __init__(self):
      self.sorat =int(input('vared kon sorat az kasr aval:'))
      self.makhrag = int(input('vared kon makhrag az kasr aval:'))
      self.a ={'n':self.sorat , 'd':self.makhrag}
   
      self.sorat =int(input('vared kon sorat az kasr dovom'))
      self.makhrag = int(input('vared kon makhrag az kasr dovom:'))
      self.b ={'n':self.sorat , 'd':self.makhrag}  


      self.result ={} 


      while True:
          select = input('1-sum\n 2-subtraction\n 3-mul\n 4-div \n 5-exit \n')   
          if select =='1':
             self.sum()
          if select =='2':
              self.subtraction()
          if select =='3':
              self.mul()
          if select =='4':
             self.div()
          else:
              exit() 

    def mul(self):
        self.result ={'n':self.a['n']*self.b['n'],'d':self.a['d']*self.b['d']}
        print(self.result['n'],'/',self.result['d'])

    def sum(self):
        self.result = {'n':self.a['n']*self.b['d']+self.b['n']*self.a['d'],'d':self.a['d']*self.b['d']}
        print(self.result['n'],'/',self.result['d'])
    
    def div(self):
        self.result ={'n': self.a['n'] * self.b['d'],'d':self.a['d']*self.b['n']}
        print(self.result['n'],'/',self.result['d'])

    def  subtraction(self):
        self.result ={'n':self.a['n']*self.b['d']-self.b['n']*self.a['d'],'d':self.a['d']*self.b['d']}
        print(self.result['n'],'/',self.result['d'])

    # def show(self):
    #     print(self.s ,'/' ,self.m)

# a = fraction(3,7)
# #a.start(3,7)
# a.show()

# b = fraction(2,7)
# #b.start(2,7)
# b.show()


fraction()

# The module for ch1 logic gates classes

# the base class of the gates
class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

### Then from the very base class, we can build two categories of classes for the 3 kinds of gates

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinA.getOutput()

    def getPinB(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinB.getOutput()
    def setNextPin(self,source):
        if self.pinA  == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
            

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        
        self.pin = None
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pin.getOutput()
        
    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

### Now we can build the exact logic gates classes

class AndGate(BinaryGate):
    def __init__(self,n):
        super(AndGate,self).__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        super(OrGate,self).__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self,n):
        super(NotGate,self).__init__(n)
    
    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

## Create a connector class to build the whole system

class Connector:
    def __init__(self,fgate,tgate):
        self.fgate = fgate
        self.tgate = tgate
        
        self.tgate.setNextPin(self.fgate)
    def getTo(self):
        return self.tgate

    def getFrom(self):
        return self.fgate
        

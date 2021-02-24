"""
Training and testing methods.
Author: Catherine Lin
"""
from DecisionTree import DecisionTree
import copy
class Stuff:
    def __init__(self, maxDepth):
        self.maxDepth=maxDepth

    def getMax(self):
        return self.maxDepth

    #create new decision tree branches
    def split(self,node):
        feature=node.getPartition().bestGain()
        for value in node.getPartition().getF().get(feature):
            part=copy.deepcopy(node.getPartition())
            child=DecisionTree(part,feature,value)
            child.getPartition().remove(feature,value)
            #create a new node and store the new partition in the node
            node.addChild(child)

    def train(self,node,currDepth):
        part=node.getPartition()
        if currDepth==self.maxDepth:
            return
        elif part.checkSame():
            return
        elif len(part.getF())==0:
            return
        elif len(part.getData())==0:
            return
        else:
            self.split(node)
            for child in node.getChildren():
                self.train(child,currDepth+1)
        return

    def testExample(self,example,currNode):
        if not currNode.getChildren():
            output=currNode.getPartition().guess()
            return output
        else:
            for child in currNode.getChildren():
                if example.features.get(child.getFeature())==child.getValue():
                    return self.testExample(example,child)

    def testData(self,data,tree):
        correct=0
        incorrect=0
        for example in data.getData():
            if str(example.label)==self.testExample(example,tree):
                correct=correct+1
            else:
                incorrect=incorrect+1
        sum=correct+incorrect
        print(str(correct)+" out of "+str(sum)+" correct")
        return correct/sum

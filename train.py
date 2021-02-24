"""
Decision tree data structure (recursive).
Author: Catherine Lin
Date:
"""

class Stuff:
    def __init__(self, maxDepth):
        self.maxDepth=maxDepth

    def split(self,node):
        part=node.getPartition()
        feature=part.bestGain()
        for value in part.getF().get(feature):
            subpartition=node.getPartition().copy()#create new partition that is a copy of the old
            subpartition.remove(feature,value)
            #create a new node and store the new partition in the node
            child=Node(subpartition,feature,value)
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
            split(node)
            for child in node.getChildren():
                train(child,currDepth+1)
        return


# def test():
# for all features in guess
# breadth first traversal of the tree

# guess <- most frequent answer in data
# if the labels in data are unambiguous then
# return Leaf(guess)
#
# else if remaining features is empty then
# return Leaf (guess)
#
# else
# for all f belonging in remaining features do
    # NO <- subset of data on which f= no
    # YES <- the subset of data on which F =YES
    # calculate i nformation gain
    # score[f]<- majority vote answers in no + majority vote answers in types
#
# end for
# f<- the feature with maximal score(f)
# NO <- the subset of data on which f=no
# YES <- the subset of data on which f=YES
#
# left <- decisionTREETRAIN(No, remaining features {f})
# right<- DecisionTreeTrain(YES, remaining features})
# return Node(f, left, right)

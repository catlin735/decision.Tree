"""
Decision tree data structure (recursive).
Author: Catherine Lin
Date:
"""
import queue


class DecisionTree:
    #key is the question it's asked
    #partition is the dataset it stores
    #children is the list of subpartitions
    def __init__(self, partition, feature, value):
        self.partition=partition
        self.feature=feature
        self.value=value
        self.children=[]

    #insert new nodes into tree
    def addChild(self,child):
        self.children.append(child)
        return child

    def getChildren(self):
        return self.children

    def getPartition(self):
        return self.partition

    def getFeature(self):
        return self.feature

    def getValue(self):
        return self.value


    def printPreorder(self,root,whitespace):
        output=whitespace+root.getFeature()+"="+root.getValue()
        output=output+root.getPartition().labelCount()

        if not root.getChildren():
            output=output+": "+root.getPartition().guess()
            print(output)
            return
        else:
            print(output)
            for child in root.getChildren():
                self.printPreorder(child,whitespace+"\t")

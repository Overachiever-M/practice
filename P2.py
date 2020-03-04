#P2
#Mars Li
#Feb.28.2020
#10:00
class node:
	def __init__(self,data,nextPointer = None):
		self.data = data
		self. nextPointer = nextPointer

	def getData (self):
		return(self.data)

	def setData(self,newData):
		self.data = newData

	def getNextPointer (self):
		return(self.nextpointer)

	def setNextPointer (self,newNextPointer):
		self.nextPointer = newNextPointer


class linkList:
	def __init__ (self, size= 0, head = None, tail = None):
		self.size = size
		self.head = head
		self.tail = tail

	def getSize (self):
		return(self.size)

	def setSize(self,newSize):
		self.size = newSize

	def getHead (self):
		return(self.head)

	def setHead(self,newHead):
		self.head = newHead

	def getTail (self):
		return(self.tail)

	def setTail(self,newTail):
		self.tail = newTail

	def isEmpty(self):
		if(self.size == 0):
			return(True)
		return(False)	

	def addNode(self,d):
		newNode = node(data = d)
		#Is this data same as the data in the node class?
		if (self.isEmpty()):
			self.setHead(newNode)

		else:
			self.getTail().setNextPointer(newNode)
		self.setTail(newNode)
		#Why this step
		self.setSize(self.size +1)
			
	def printLinkedList(self):
		currentNode = self.getHead()
		while(currentNode != None):
			print(currentNode.getData())
			currentNode = currentNode.getNextPointer()
			
	
def main():
 	linkList1 = linkList()
 	linkList1.addNode(1)
 	linkList1.addNode(2)
 	linkList1.addNode("American University")
 	print(linkList1.getTail().getData())
 	print(linkList1.isEmpty())
 	print(linkList1.getSize())

 	#Formatting isEmpty(): = self.size
 	#print out node1,node2,node2 = current

if __name__ == "__main__":
	main()
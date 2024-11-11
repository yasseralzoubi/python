class SLNode:
    def __init__(self,value):
        self.value=value
        self.next =None


class SList:
    def __init__(self):
        self.head=None

    def Add_to_head(self,value):
        new_node=SLNode(value)
        new_node.next=self.head
        self.head=new_node
        return self
    
    def Print(self):
        curr_head=self.head
        while(curr_head != None):
            print(curr_head.value)
            curr_head=curr_head.next
        return self



    def Add_to_Tail(self,value):
        new_node=SLNode(value)
        curr_head=self.head
        while(curr_head !=None):
            curr_head=curr_head.next
        curr_head.next=new_node
        

    def Add_to_index(self,index,value):
        new_node=SLNode(value)
        current=self.head
        for i in range (0,index,1):
            current=current.next
            temp=current.next
            current.next=new_node
            new_node.next=temp
        return self


node1=SList()
node1.Add_to_head("5").Add_to_head("9").Add_to_head("6").Add_to_head("9").Add_to_index(55,2).Print()

    




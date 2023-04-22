class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.deathh = set()  
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deathh.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        arr = []
        def successor(x):
            if x not in self.deathh:
                arr.append(x)
            
            if not self.graph[x]:
                return
            
            for person in self.graph[x]:
                successor(person)
        
        successor(self.kingName)
        
        return arr

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
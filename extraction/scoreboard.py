class ScoreBoard():
    def __init__(self,scorecard:list):
        self.scorecard=scorecard
        self.sorted_scorecard=sorted(scorecard,key= lambda x: -x[1])
    def __len__(self):
        return len(self.scorecard)
    def __str__(self):
        return "The Final Scorecard is:\n"+"\n".join(f"{name},{score}" for name,score in self.sorted_scorecard)
    #def __getitem__(self,index):
    #    return self.sorted_scorecard[index]
    def __contains__(self,player):
        return any(player==name for name,score in self.sorted_scorecard)
    def __iter__(self):
        return iter(self.sorted_scorecard)
    
if __name__=="__main__":
    sb=ScoreBoard([("Alice",18),("Mark",9),("Charlie",19)])
    print(len(sb))
    print(sb)
    #print(sb[0:2])
    print("Alice" in sb)
    for player,score in sb:
        print(player)

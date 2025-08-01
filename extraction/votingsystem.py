class VotingSystem():
    def __init__(self,votes: list):
        self.student_votes=votes
    def popular_by_votes(self):
        votes={}
        for v in self.student_votes:
            votes[v]=votes.get(v,0)+1
        max_vote= max(votes.items(),key=lambda x: (x[1]))
        return sorted([language for language,count in votes.items() if count==max_vote[1] ])
    def __str__(self):
        return (f"Most Popular vote goes to : {self.popular_by_votes()} langugae")

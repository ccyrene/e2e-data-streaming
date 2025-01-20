class AirflowConfig:
    def __init__(self, owner, start_date):
        self.owner = owner
        self.start_date = start_date

    def __repr__(self):
        return f"AirflowConfig(owner={self.owner}, start_date={self.start_date})"
    
    def to_dict(self):
        return {
            "owner": self.owner,
            "start_date": self.start_date,
        }
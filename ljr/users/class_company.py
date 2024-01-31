class Company:
    def __init__(self,**kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.catchPhrase = kwargs.get('catchPhrase')
        self.bs = kwargs.get('bs')

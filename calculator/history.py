import json

class CalcHistory:
    @staticmethod
    def serialize(self):
        return json.dumps(self.history)
    @staticmethod
    def deserialize(self, data):
        self.history = json.loads(data)
    @staticmethod
    def write(self, data):
        with open('history.json', 'a') as f:
            f.write(data)
    @staticmethod
    def read(self):
        with open('history.json', 'r') as f:
            return f.read()

    @staticmethod
    def append(self, data):
        current =self.serialize(self.read())
        # now append the new data
        current.append(data)
        self.write(self.serialize(current))
        
        
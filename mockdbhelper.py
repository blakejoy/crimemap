

class MockDBHelper:

    def connect(self,database="crimemap"):
        pass

    def add_crime(self,category,date,latitude,longitude,description):
        pass
    def get_all_crimes(self):
        return [{
                'latitude': 39.593092358692405,
                'longitude': -76.63972595214844,
                'date': "2000-01-01",
                'category': "mugging",
                'description': "This is a description"
                }]



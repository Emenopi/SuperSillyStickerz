class Populator():
    def __init__(self, reader, models):
        self.models = models # {"table name" : Model,}
        self.data = reader.get_data() # {"table name" : [{"column name" : "column content"}]}

    def populate(self):
        print("# populating started")
        for table_name, model in self.models.items():
            print("##",table_name)
            instance = model()
            table = self.data[table_name]
            for record in table:
                for attr_name, attr_content in record.items():
                    setattr(instance, attr_name, attr_content)
                print(" -",instance)
                instance.save()
        print("population complete")
                    

        
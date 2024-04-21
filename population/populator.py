class Populator():
    def __init__(self, reader, models,verbose=True):
        self.models = models # {"table name" : Model,}
        self.data = reader.get_data() # {"table name" : [{"column name" : "column content"}]}
        self.verbose = verbose

    def populate(self):
        if self.verbose:
            print("# populating started")
        for table_name, model in self.models.items():
            if self.verbose:
                print("##",table_name)
            self.create_record_from_model(table_name, model)
        if self.verbose:
            print("population complete")

    def create_record_from_model(self, table_name, model):
        instance = model()
        table = self.data[table_name]
        for record in table:
            for attr_name, attr_content in record.items():
                setattr(instance, attr_name, attr_content)
            if self.verbose:
                print(" -",instance)
            instance.save()
                    

        
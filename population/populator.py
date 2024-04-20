class Populator():
    def __init__(self, reader, models):
        self.models = models # {"table name" : Model,}
        self.data = reader.get_data() # {"table name" : [{"column name" : "column content"}]}

    def populate(self, verbose=True):
        if verbose:
            print("# populating started")
        for table_name, model in self.models.items():
            if verbose:
                print("##",table_name)
            instance = model()
            table = self.data[table_name]
            for record in table:
                for attr_name, attr_content in record.items():
                    setattr(instance, attr_name, attr_content)
                if verbose:
                    print(" -",instance)
                instance.save()
        if verbose:
            print("population complete")
                    

        
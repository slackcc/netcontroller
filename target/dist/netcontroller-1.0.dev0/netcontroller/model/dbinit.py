from model.config import Database_Config


class Dbinit:
    Database_Config.db.generate_mapping(create_tables=True)

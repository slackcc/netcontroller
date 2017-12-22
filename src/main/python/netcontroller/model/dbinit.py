from model.config import DatabaseConfig


class Dbinit:
    DatabaseConfig.db.generate_mapping(create_tables=True)

import cx_Oracle


class ConnectionError(Exception):
    pass

class UseDatabase:
    def __init__(self,config:dict)->None:
        self.configuration=config


    def __enter__(self):
        try:
            self.conn = cx_Oracle.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except Exception as e:
            print('Exception is {} '.format(e))
            raise ConnectionError(e)


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        # cursor.close()
        self.conn.close()
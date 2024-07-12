from pyspark import SparkSession
class MetadataUtil:
    __instance = None

    def __new__(cls ,spark: SparkSession ,v_catalog: str, v_space: str, v_table:str):
        if cls.__instance is None:
            cls.__instance = super(MetadataUtil, cls).__new__(cls)

        return cls.__instance

    def __init__(self, spark: SparkSession,
                        v_catalog: str,
                        space: str ,
                        pipeline: str,
                        vendor: str ):
        self.spark = spark
        self.catalog = v_catalog
        self.space = space
        self.pipeline = pipeline
        self.vendor = vendor
        self.db_name = f"{self.space}.'silver'.'md'"
        self.md_table = f'{v_catalog}.{self.space}.we_metadata'


    def create_md_table(self):
        self.spark.sql(f"create schema if not exists {self.db_name}")
        self.spark.sql(f"""
                            create table if not exists  {self.md_table}
                            (pipeline string , vendor string , batch_id int )
                        """)

    def read_batch_id(self,object_type:str , layer:str , task:str , description:str ="Na"):
        df = self.spark.sql(f"""
                            select batch_id from {self.md_table}
                            where lower(pipeline) = '{self.pipeline}' and
                                  lower(vendor) = '{self.vendor}'   and
                                  lower(object_type)  = '{object_type.lower()}' and
                                  lower(layer) = '{layer.lower()}' and
                                  lower(task)  = '{task.lower()}'                          
                        """)

        if not df.first():
            self.insert_record(object_type , 20240101,layer , task ,description)
            return 20240101
        return df.first().asDict().get("batch_id")


    def insert_record(self,object_type:str , batch_id :int,layer:str , task:str ,description:str = "Na"):
        self.spark.sql(f"""
                    insert into {self.md_table} 
                    (pipeline , vendor , object_type , batch_id , layer , task , description)
                    values(
                      '{self.pipeline}' , '{self.vendor}' ,'{object_type.lower()}' ,
                      '{batch_id}','{layer.lower()}','{task.lower()}','{description.capitalize()}'
                    )
                       """)

    @staticmethod
    def get_task_executed_status(new_batch_id:int , previous_batch_id:int):
        if previous_batch_id > new_batch_id:
            return False
        elif new_batch_id == previous_batch_id:
            return True
        else:
            raise ValueError(" new_batch_id is invlaid")






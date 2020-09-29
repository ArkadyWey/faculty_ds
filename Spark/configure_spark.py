import sys
import os

import pyspark


def get_session(memory_fraction=0.9):
    """Configure a single-server Spark session on Faculty platform.
    
    To get the underlying Spark context, use the `.sparkContext` attributed of
    the returned session.
    """

    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    number_cores = int(os.environ["NUM_CPUS"])
    memory_gb = int(os.environ["AVAILABLE_MEMORY_MB"])
    memory_gb *= memory_fraction
    memory_gb = int(memory_gb) // 1000
    
    spark_builder = (
        pyspark.sql.SparkSession.builder
        .master('local[{}]'.format(number_cores))
        .config("spark.driver.memory", '{}g'.format(memory_gb))
        .config("spark.driver.maxResultSize", '{}g'.format(memory_gb // 2))
    )
    
    spark = spark_builder.getOrCreate()
    return spark
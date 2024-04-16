import sys
import pytest
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

@pytest.fixture
def create_dataframe():
    df = spark.read.parquet("s3://sampledata9873/mongo_smaple_data/*.parquet")
    return df
    
def test_col_name():
    assert "id" in df.columns
    print("passed1")
job.commit()

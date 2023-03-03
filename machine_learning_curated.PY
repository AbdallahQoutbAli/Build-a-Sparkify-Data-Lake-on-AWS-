import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node  step_trainer
step_trainer_node1677866070069 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://setid-lake-house/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="step_trainer_node1677866070069",
)

# Script generated for node accelerometer  trusted
accelerometertrusted_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://setid-lake-house/accelerometer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="accelerometertrusted_node1",
)

# Script generated for node Renamed keys for join
Renamedkeysforjoin_node1677866269357 = ApplyMapping.apply(
    frame=step_trainer_node1677866070069,
    mappings=[
        ("sensorReadingTime", "bigint", "sensorReadingTime", "long"),
        ("serialNumber", "string", "`(right) serialNumber`", "string"),
        ("distanceFromObject", "int", "`(right) distanceFromObject`", "int"),
    ],
    transformation_ctx="Renamedkeysforjoin_node1677866269357",
)

# Script generated for node join
join_node2 = Join.apply(
    frame1=accelerometertrusted_node1,
    frame2=Renamedkeysforjoin_node1677866269357,
    keys1=["timeStamp"],
    keys2=["sensorReadingTime"],
    transformation_ctx="join_node2",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=join_node2,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://setid-lake-house/step_trainer/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()

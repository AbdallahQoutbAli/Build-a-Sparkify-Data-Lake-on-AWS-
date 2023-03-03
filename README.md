# STEDI-Human-Balance-Analytics


### Project Details : 

The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that:

    trains the user to do a STEDI balance exercise;
    and has sensors on the device that collect data to train a machine-learning algorithm to detect steps;
    has a companion mobile app that collects customer data and interacts with the device sensors.

STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.

The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.


###  Project Environment

AWS Environment

You'll use the data from the STEDI Step Trainer and mobile app to develop a lakehouse solution in the cloud that curates the data for the machine learning model using:

    Python and Spark
    AWS Glue
    AWS Athena
    AWS S3

On the next page, you'll find instructions for accessing a temporary AWS account you can use to complete the project. This account has a budget of $25 you should be aware of when creating resources on the AWS platform. Pay special attention to what you are creating and running and the cost of these services.

### Project Data:

1. Customer Records (from fulfillment and the STEDI website):

AWS S3 Bucket URI - s3://cd0030bucket/customers/

contains the following fields:

    serialnumber
    sharewithpublicasofdate
    birthday
    registrationdate
    sharewithresearchasofdate
    customername
    email
    lastupdatedate
    phone
    sharewithfriendsasofdate

2. Step Trainer Records (data from the motion sensor):

AWS S3 Bucket URI - s3://cd0030bucket/step_trainer/

contains the following fields:

    sensorReadingTime
    serialNumber
    distanceFromObject

3. Accelerometer Records (from the mobile app):

AWS S3 Bucket URI - s3://cd0030bucket/accelerometer/

contains the following fields:

    timeStamp
    serialNumber
    x
    y
    z
    
   

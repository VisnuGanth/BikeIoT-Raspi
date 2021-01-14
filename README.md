# BikeIoT-Raspi

An IoT project that receives 9-axis IMU (Inertial Measurement Unit) data from the SenseHAT emulator in the Raspberry Pi via the AWS IoT Core service and displays the retreived data by means of a dynamic graph made using Python. This project was done to model a system that gets data from sensors attached to a motorbike. The data retreived from the SenseHAT emulator are: 3-axis gyroscope, 3-axis accelerometer and 3-axis magnetometer. This project has the code present on the Raspberry Pi which connects to AWS cloud and sends the real-time data generated from the SenseHAT emulator on the Raspberry Pi.

- IMU_data.py - Has the Python code to get the data from the SenseHAT emulator and attaches it with a timestamp(which will be used as the x-axis during display) and stores it in a local text file.
- AWSPubSub.py - Python file that publishes the 9-axis data along with a device id and timestamp to the AWS IoT Core service under a specific topic name

**Note:**
The **Documentation** folder in the [BikeIoT-PC repository](https://github.com/VisnuGanth/BikeIOT-PC) has the documents that explain how to setup the AWS cloud service and how the sent data is being stored in the cloud.
- [Doc1 - (IMU_Data.py) Get data from Emulator.docx](https://github.com/VisnuGanth/BikeIOT-PC/blob/master/Documentation/Doc1%20-%20(IMU_Data.py)%20Get%20data%20from%20Emulator.docx) explains how to get the data from the emulator and store in a file
- [Doc2 - (AWSPubSub.py) AWS IoT and Pi setup.docx](https://github.com/VisnuGanth/BikeIOT-PC/blob/master/Documentation/Doc2%20-%20(AWSPubSub.py)%20AWS%20IoT%20and%20Pi%20setup.docx) has the explanation to set up an AWS IoT resource with the necessary certificates and permissions and install the SDK in the Raspi.
- [Doc3 - Receiving Data in AWS IoT Core, Setting up a rule.docx](https://github.com/VisnuGanth/BikeIOT-PC/blob/master/Documentation/Doc3%20-%20Receiving%20Data%20in%20AWS%20IoT%20Core%2C%20Setting%20up%20a%20rule.docx) shows the sending and receiving of data in the cloud and also about how to set up a Lambda rule which gets the incoming data in the cloud and stores in a database.
- [Doc4 - (cloud - lambda_function.py) Making a lambda function & policies.docx](https://github.com/VisnuGanth/BikeIOT-PC/blob/master/Documentation/Doc4%20-%20(cloud%20-%20lambda_function.py)%20Making%20a%20lambda%20function%20%26%20policies.docx) shows how to create a Lambda function and manage the relevant permissions to connect it to DynamoDB.

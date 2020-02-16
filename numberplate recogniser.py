# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:34:19 2019
@author: Arnab Das
"""

import datetime
import authentication
import capture
import numberplate


now = datetime.datetime.now() ; car_count = 0  

"""THE BELOW CAN BE MODIFIED"""

photo = "first.jpg"

with open(photo , 'rb') as source_image:
    source_bytes = source_image.read()
    
"""AWS Rekognition"""    
response = authentication.clientrek.detect_text(Image={'Bytes':source_bytes})
                              
result = []   #contains all the text detected by AWS Rekognition

textDetections=response['TextDetections']
print ('\nDetected text\n----------')
for text in textDetections:
    print ('Detected text:' + text['DetectedText'] + '     Confidence: '+ str(text['Confidence']))
    if text['Confidence'] > 50 and text['DetectedText'] not in result:
        #text['DetectedText'] = text['DetectedText'].replace(" ","")
        result.append(text['DetectedText'].replace(" ",""))
    
print(result)

for word in result:
    x = numberplate.number_plate_verify(word)

"""uploading file to AWS S3
local_file = open(str(now.day) + "-" + str(now.strftime("%B"))+ "-" + str(now.year)+'.txt')
#numberplatedata is the Bucket name
s3_file = local_file 
with open(local_file, 'r') as f:
    for line in f:
        car_count += 1
if car_count > -2:
    print("\n...Uploading to S3...")
    authentication.clients3.upload_file(local_file,'numberplatedata',s3_file)
    print("\nS3 bucket updated!!!")"""



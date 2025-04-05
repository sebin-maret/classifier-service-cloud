# Classifier Service for Federated learning Model


##  Description

This is a simple fast api backedn service that load the selected model that was trained using the federated learning model. The API this service exposes expects a picture (X-Ray) and produces a classification Covid, Pneumonia or Normal.


##  Deploying

The service can be locally run using the following command.
```shell script
python3 main.py
```

This service was deployed on AWS ECS after dockerization. To containerize the application the following command can be used


```shell script
docker build -t <image-tag> . && docker push <image-tag>
```

After pushing the image, the image can be deployed using any containerization platforms.



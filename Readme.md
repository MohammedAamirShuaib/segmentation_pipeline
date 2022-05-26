# Segmentation Pipeline
## Overview
The main objective of this project is to build and showcase an end-to-end MLOps pipeline for segmentation, which includes ML Development and Deployment. 
In this example we are using Student survey dataset in which the students have ranked the exam questions based on its perceived difficulty. We are looking to take this data and group the students into different segments based on their responses. We are using techniques like Principal Component Analysis and k-means clustering for classifying the students into different segments. Principal component analysis (PCA) is a technique for reducing the dimensionality of datasets with many variables, to increasing interpretability but at the same time minimizing information loss. The k-means clustering method is an unsupervised machine learning technique used to identify clusters of data objects in a dataset. Once we have developed a model, we are serving the model to make predictions on new data through a Rest API build using FastAPI.

 ![image](https://user-images.githubusercontent.com/98326079/170496729-67e2116a-5afd-4b54-8fb0-c2bbd0fd6f93.png)

## Implementation 
#### Required Libraries:
•	pandas
•	scikit-learn
•	seaborn
•	matplotlib
•	pycaret
•	pandas-profiling
•	wandb
•	fastapi
•	uvicorn
•	python-multipart
•	requests

clone the GitHub repository: https://github.com/MohammedAamirShuaib/segmentation_pipeline.git
for stating the API run the command: “uvicorn main:app –host 0.0.0.0 –port 8000 –reload”
once the API is running you can send data to the API to get predictions of cluster segment.
## Technologies used:
#### Python
Python is an opensource programming language that allows to build applications. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects

#### Weights & Biases
Weights & Biases is a machine learning platform geared towards developers for building better models faster. It is designed to support and automate key steps in the MLOps life cycle, such as experiment tracking, dataset versioning and model management.

#### FastAPI
FastAPI is a Web framework for developing RESTful APIs in Python. FastAPI is based on Pydantic and type hints to validate, serialize, and deserialize data, and automatically auto-generate OpenAPI documents. It fully supports asynchronous programming and can run with Uvicorn and Gunicorn.

#### Gunicorn
The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server. It is a pre-fork worker model, ported from Ruby's Unicorn project. The Gunicorn server is broadly compatible with several web frameworks, simply implemented and light on server resources.

#### Docker
Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. The software that hosts the containers is called Docker Engine. Docker containers allow applications to run on an isolated environment which contains all the resources required to run the application.

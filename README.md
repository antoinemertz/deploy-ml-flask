# Deploy Machine learning API using Flask and Docker

In this tutorial, we create a containerized machine learning application. It is a simple application but it can be used as a template to build a more serious one.

## Create your model

We create a SVM classifier on iris dataset and stored the fitted model in a file.

`python model.py`

It stores the model in a file in `models/` folder and we will use this file to deploy our model.

## Deploy your docker image

```
# run it where you have you Dockerfile
docker build . -t demo
```

And then just run your image

```
docker run -p 5000:5000 --rm demo
```

And if you go to `http://127.0.0.1:5000` you will see your application running!

(If not use `nmap localhost -p 5000` to see if the port is open and `http http://127.0.0.1:5000` to see what's responding)

## Use your ML model

Now you can use your model.

```python
>>> import json
>>> import requests
>>> url = "http://127.0.0.1:5000/predict"
>>> data = json.dumps({'sl': [5.84, 4.38], 'sw': [3.0, 2.16], 'pl': [3.75, 7.65], 'pw': [1.1, 1.23]})
>>> r = requests.post(url, data)
>>> print(r.json())
```

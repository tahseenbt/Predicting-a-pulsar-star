# Predicting a pulsar star

Final project for McGill AI Society Bootcamp (MAIS202) Fall 2020.

Using training data from [UCI Machine Learning Repo](https://archive.ics.uci.edu/ml/datasets/HTRU2)

## Project description

This is a web app that astronomers can use to predict the existence of a pulsar star given 8 features. They could use the prediction to further investigate and confirm the discovery of the star.

## Running the app

You can either import this github repo into heroku or install the packages in requirements.txt and then run
```
python app.py
```
Next, navigate to the webpage http://127.0.0.1:5000.

If the app is already active, it should be available at https://predicting-a-pulsar-star.herokuapp.com/

## Repository organization

This repo contains the scripts used to test and train various models, the dataset used for it and the scripts used to have the webapp up and running.

1. deliverables and model training/
    * The deliverables submitted to the MAIS202 bootcamp (to receive feedbacks from the TPM associated) and the python notebooks used for testing and finalizing a model.
2. templates/
    * It includes the HTML landing page
3. SVM_model.pkl
    * It is the saved version of the trained SVM model which is used to avoid retraining the model for each use.

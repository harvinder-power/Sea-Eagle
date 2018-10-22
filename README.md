# Project Sea Eagle
System to classify chest x-rays based on diagnosis

## How does it work?
Using a TensorFlow backend, the system is trained on a dataset of chest x-rays which either have pneumonia, or are normal. The system trains itself, and is then able to be used to classify images the user feeds into the system.

## Model
The model structure is a simple 4 layer CNN, with added dropouts in each stage (`0.1`, and `0.3` at layers 4) and a final dropout value of `0.5` at the end to prevent over-fitting of the model.

## Running the model
Whilst all code can be downloaded from the GitHub website, it is highly suggested to use the Docker download method listed below to run the code. The dataset is not available on GitHub, but is pubically available from here (https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).

## Docker Container
The dataset and code is publically available through the Docker system (https://www.docker.com/), and can be run using the following command in Terminal:

```bash
docker pull harvinderpower/xrayclassifier
```

NB. The full image is 2GB so may take some time depending on your internet speed.

## Metrics
```
loss: 0.2293 - acc: 0.9185 - val_loss: 0.3434 - val_acc: 0.8562
```
#### 85.62% Validation Accuracy


## Next Steps
- Retrain model with additional classifications (requires more data)

# Project Sea-Eagle
An image classifier to classify Chest X-Rays using Transfer Learning.

<p align="center">
  <img src="https://i.ibb.co/VY9G76d/eagle.png" alt="Project Sea Eagle logo"/>
</p>

## Background
Chest X-Rays are notoriously difficult to interpret when starting out for any new doctor. By using an classifier, we can help with
the triage process to risk stratify x-rays into high suspicion of pneumonia, or low suspicion.

## Methods
This model was trained using [this dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia), using Transfer Learning to retrain the last layer of a MobileNet model.

## Accuracy
| Class     | Accuracy | # Samples |
|-----------|----------|-----------|
| Normal    | 0.94     | 202       |
| Pneumonia | 0.98     | 582       |

## Implementation
The model is implemented using Tensorflow.js, which enables local classification rather than sending data to a server.

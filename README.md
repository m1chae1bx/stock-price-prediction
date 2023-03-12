# Overview

This project aims to predict the stock price of a company using a Long Short-Term Memory (LSTM) neural network. The LSTM model is trained using the historical stock price data of a company. The model is trained using the Tensorflow framework and the Keras API.

# Setup

## Install Requirements

Install the requirements using the following command:
`pip install -r setup/requirements.txt`

The Tensorflow version used in this project is for Mac OS. If you are using a different OS, please install the correct version of Tensorflow. In addition, the Tensorflow Metal plugin is used to accelerate the training process on Mac OS using Mac GPUs.

Are you having an error with Tensorflow? Make sure tensorflow-macos and tensorflow-metal versions are compatible. Working versions of tensorflow-macos and tensorflow-metal for Macbook Pro M1 are 2.10.0 and 0.6.0 respectively [1].

To test if your tensorflow environment is properly setup, run the following command:
`python setup/test_tensorflow_env.py`

## Install a Jupyter kernel in a Python virtual environment

Run the following command in your virtual environment:
`ipython kernel install --user --name=stock-price-model`

# Dataset

## Source

The dataset used in this project is extracted from MarketWatch.com [2]. The stocks are listed in the Philippine Stock Exchange (PSE).

## Data Preprocessing

Data preprocessing is a crucial step in preparing data for analysis or machine learning. In this project, data preprocessing is performed in two phases, the first of which is detailed in the Jupyter notebook `1_preprocess_data.ipynb`. This phase uses a configuration file to specify various parameters, such as the directory of the raw data, the features to be used, and the transformations to be applied to the whole dataset. Additionally, a metadata file is created to store information about the preprocessed data, and the configuration file must also specify how this metadata file is to be created.

A sample configuration file is provided at `data/preprocess_config_v_0_1.py`. After this initial preprocessing phase, further processing is performed at a feature level, which discussed in a separate section. To change the configuration file, update the `CONFIG_FILE` variable in `1_preprocess_data.ipynb`.

# Training

## Feature Level Preprocessing

Before we train the model in `2_train_model.ipynb`, further preprocessing is performed at the feature level. A separate configuration file is used for this purpose where we specify the features to be used and the transformations to be applied to each feature. The metadata file created in the previous section is used in this phase. To set the configuration file, update the `CONFIG_FILE` variable in `2_train_model.ipynb`.

These transformations are applied to the training set first, and then the same transformations are applied to the validation set. This ensures that the validation set is not used to determine the parameters of the transformations. Currently, z-score normalization is the only transformation that is applied to the features.

## Model Training Parameters and Architecture

The parameters specified in the configuration file such as the learning rate determine how the model is trained. Below is the list of the notable parameters and an explanation of their purpose.

- `learning_rate`: The learning rate determines how much the model changes in response to the estimated error each time the model weights are updated. A higher learning rate will cause the model to learn faster, but it may also cause the model to overshoot and never find a good solution. A lower learning rate will cause the model to learn slower, but it will also be more likely to converge to an optimal solution.
- `max_epochs`: The maximum number of epochs to train the model. An epoch is a single pass through the entire training dataset. The model will stop training once the maximum number of epochs is reached, or if the validation loss stops improving.
- `patience`: The number of epochs to wait for the monitored metric to improve before stopping the training. This is used to prevent overfitting. If the metric, validation loss for example, does not improve for the specified number of epochs, the training will stop.
- `loss function`: The loss function is used to measure how well the model is performing. The loss function is minimized during training. The loss function is also used to determine the model's performance during testing. See https://www.tensorflow.org/api_docs/python/tf/keras/losses for a list of available loss functions.
- `metrics`: Additional metrics used to evaluate the model. See https://www.tensorflow.org/api_docs/python/tf/keras/metrics for a list of available metrics.

Other parameters currently have fixed values such as the following:
- Early stopping metric: Validation loss
- Early stopping mode: Minimize
- Restore best weights: True
- Optimizer: Adam
- Model Architecture: Sequential model with 1 LSTM layer and 2 hidden Dense layers and 1 output Dense layer

# Testing

The testing phase uses the same configuration file as the training phase. The same transformations are applied to the test set as were applied to the training set. The model is loaded from the saved model file and the test set is used to evaluate the model. To set the configuration file, update the `CONFIG_FILE` variable in `3_test_model.ipynb`.

To evaluate the model, the loss function and other metrics specified in the configuration file are calculated. The predictions are also plotted against the actual values. See `3_test_model.ipynb` for more details.

# References

[1] https://developer.apple.com/metal/tensorflow-plugin/
[2] https://www.marketwatch.com/
[3] https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM
[4] https://www.youtube.com/watch?v=CbTU92pbDKw

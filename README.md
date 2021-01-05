# CNN

## Table of Contents

- [Introduction](#introduction)
  * [Exploratory Data Analysis](#exploratory-data-analysis)
- [Methodology](#methodology)
  * [I. CNN model for single attribute](#i.-cnn-model-for-single-attribute)
  * [II. CNN model for multiple attribute](#ii.-cnn-model-for-multiple-attributes)
- [Results](#results)
- [Discussions](#discussions)
- [Conclusions](#conclusions)
- [Moreover](#moreover)

## Introduction

Use CNN models to analyze the **CelebFaces Attributes** Dataset.

### Exploratory Data Analysis

* Ratio of each face attribute.

* Use correlation matrix and PCA to analyze the highly connected face attributes.
    + Correlation matrix implies the highly connected attributes.
    + PCA implies different aspects of connections in the attributes.
    + Demonstrate the PCA loading plots and a table to summarise the study.

## Methodology

### I. CNN model for single attribute

1. Strategic
    a. Input shape
    b. Convolutional layer
        i. number of block
        ii. number of layers in each block
        iii. dropout
        iv. hyperparameters
    c. Fully connected layer
        i. number of layers
        ii. units
        iii. dropout
2. Purpose
    a. Check the effect of the hyperparameters
    b. Find the best combination of convolutional layer and fully connected layer
    c. Hint to futher adjust CNN models
3. Predict the rank of the candidate models
    a. Motivation
        i. Time consuming
        ii. Memory consuming
        iii. Highly restricted to PC's specifications
        iv. Sampling unbiased data is suitable for representing the population
    b. Method
        i. Sampling a properly small dataset for model training process
        ii. Use metrics in each epoch to compare the performance with other models
        iii. Hypotheses testing result will suggest the rank of the performance of the candidate models
    c. Validation
        i. Whether the proposed rank of the candidate models matches the original dataset training result.

### II. CNN model for multiple attributes

## Results

## Discussions

## Conclusions

* Including the application of our CNN models

## Moreover

You can review our code and examine our data on [GitHub](https://github.com/Hochia/ml-final).

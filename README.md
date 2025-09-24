# DVC-intro: A Guide to Reproducible Data Science 

Hey there! Welcome to my `DVC-intro` project. This repository is more than just code; it's a journey into the world of **Data Version Control (DVC)**. Think of it as a personal notebook where I've figured out how to make data science projects **reproducible**, **collaborative**, and a whole lot less messy.

The goal here was simple: to learn how to manage large datasets and machine learning models without bloating my Git repository. DVC is the hero that makes this possible.

## What's Inside? 

This project contains a simple, yet complete, machine learning pipeline built with DVC.

* `iris.json`: Our dataset, a JSON version of the famous Iris dataset. It's the "data" part of our data science.
* `src/preprocess.py`: A Python script that performs a basic preprocessing step on our raw data.
* `src/train.py`: A Python script that takes the preprocessed data and trains a simple Random Forest model.
* `dvc.yaml` & `dvc.lock`: These are the magic files! `dvc.yaml` defines our **pipeline stages** (preprocess and train), telling DVC what to do, while `dvc.lock` acts as a **recipe**, recording the exact versions of the data and code used to create our final model.

## The Secret Sauce: DVC + Git 

Here's the cool part:

* **Git** tracks all my code and the small `dvc.yaml` and `dvc.lock` files. My repository stays tiny and easy to clone.
* **DVC** manages the heavy lifting—our large dataset (`iris.json`) and the generated model (`model.pkl`). The actual data files live in a separate **remote storage**, not in the Git repo. 

This means that anyone can clone this project, run a couple of DVC commands, and get the exact same data and results I did. No more "it worked on my machine!" debates.

## How to Get Started (Reproduce This Project) 

Want to see it in action? Follow these simple steps.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/CodeWithSagomb/DVC-intro.git](https://github.com/CodeWithSagomb/DVC-intro.git)
    cd DVC-intro
    ```

2.  **Pull the data:** DVC will pull the dataset and the trained model from the remote storage.
    ```bash
    dvc pull
    ```

3.  **Run the pipeline:** This will execute the `preprocess` and `train` stages, recreating `iris_clean.csv` and `model.pkl`.
    ```bash
    dvc repro
    ```


# Spam SMS Detection
**Overview**

As part of my machine learning internship, I have been tasked with creating a model that predicts whether an SMS message is spam or legitimate. The model utilizes word embeddings, specifically Word2Vec, in conjunction with Support Vector Machine (SVM) for performing the classification. A graphical user interface has been developed using PySide6 to make the application user-friendly.

**Project Structure**

 - `data/`: Contains the dataset used for training the model.
 - `model/`: Stores the trained machine learning and Word2Vec models.
 - `ui/`: Stores .ui files created using pyside6-designer.
 - `main.py`: Main code for data preprocessing, feature extraction and model training.
 - `mainui.py`: The code for the GUI.

**Prerequisites**

 1. Python
 2. Required libraries: pandas, numpy, scikit-learn, gensim, PySide6

**Running the Application**
1) Clone or download the repository.
2) If downloaded then extract it to a folder, if cloned then just skip this step.
3) Install dependencies if needed.
4) Open the terminal in the extracted folder and run the following:
`python -u "main.py"`

**Demo**

https://github.com/AkanshGrover/Spam-SMS-Detection/assets/163346711/ecaa9c7d-0c09-46d1-8665-a8a1a36a743a

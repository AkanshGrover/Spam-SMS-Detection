from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from mainui import Ui_MainWindow
from sklearn.svm import SVC
from gensim.models import Word2Vec
import pandas as pd
import numpy as np
import sys, re, chardet, pickle, os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.font = QFont()
        self.font.setPointSize(11)
        self.ui.message_ip.setFont(self.font)
        self.ui.check_btn.clicked.connect(self.check_spam)
        self.ui.clear_btn.clicked.connect(self.clear)

        data_loc = os.path.join("data", "spam.csv")
        with open(data_loc, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']

        train_data = pd.read_csv(data_loc, delimiter=",", encoding=encoding)
        train_data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True, axis=1)
        train_data.rename({"v1":"label","v2":"message"}, inplace=True, axis=1)

        train_data["message"] = train_data["message"].apply(self.clear_data)

        x_train = train_data["message"] #this is like a question
        y_train = train_data["label"] #this is like an answer

        texts = []
        for text in x_train:
            texts.append(text.split())

        w2v_model_path = os.path.join("model", "w2v_model.model")
        if os.path.isfile(w2v_model_path):
            self.w2v_model = Word2Vec.load(w2v_model_path)
        else:
            self.w2v_model = Word2Vec(texts, window=50, min_count=5, workers=12, epochs=10)
            self.w2v_model.save(w2v_model_path)
        l = []
        for text in x_train:
            l.append(self.vectorize(text))
        x_train = np.array(l)

        m_path = os.path.join("model", "model.pkl")
        if os.path.isfile(m_path):
            with open(m_path, 'rb') as f:
                self.model = pickle.load(f)
        else:
            self.model = SVC(kernel="rbf", gamma=0.5, C=1.0)
            self.model.fit(x_train, y_train)
            with open(m_path, 'wb') as f:
                pickle.dump(self.model, f)

    def vectorize(self, text):
        words = text.split()
        l = []
        for word in words:
            if word in self.w2v_model.wv:
                l.append(self.w2v_model.wv[word])
        words_vecs = l
        if len(words_vecs) == 0:
            return np.zeros(self.w2v_model.vector_size)
        words_vecs = np.array(words_vecs)
        return words_vecs.mean(axis=0)


    def clear_data(self, txt):
        txt = txt.lower()
        txt = re.sub(r'[^\w\s]', "", txt)
        return txt


    def clear(self):
        self.ui.message_ip.clear()


    def check_spam(self):
        textip = self.ui.message_ip.toPlainText()
        cleaned_text = self.clear_data(textip)
        texts = cleaned_text.split('.')
        l = []
        for text in texts:
            if text.strip():
                l.append(self.vectorize(text))
        sentences_vecs = np.array(l)
        if sentences_vecs.size != 0:
            x_input = sentences_vecs.mean(axis=0).reshape(1, -1)
            predict = self.model.predict(x_input)
            if predict == "spam":
                QMessageBox.information(self, "Spam or ham", "Entered message is spam")
            else:
                QMessageBox.information(self, "Spam or ham", "Entered message is not spam")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
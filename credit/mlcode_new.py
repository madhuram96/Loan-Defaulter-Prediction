import pandas as pd
import numpy as np
import warnings
warnings.simplefilter('ignore')
from catboost import CatBoostClassifier



def CatBoostingClassification(imputed_train_new,train_labels):
	X = imputed_train_new
	y = train_labels 
	classifier = CatBoostClassifier(iterations=500,learning_rate=0.1,depth=8,loss_function='Logloss',bootstrap_type='Bernoulli',eval_metric='AUC',class_weights=[1, 2],random_seed=9, verbose=False)
	classifier = classifier.fit(X, y)
	return classifier	
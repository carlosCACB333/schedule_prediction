from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, RobustScaler, LabelEncoder
import pandas as pd


def train_test_val_split(
    df, random_state=42, shuffle=True, stratify=None, test_size=0.3
):
    """
    This function splits a dataframe into train, validation and test sets.
    """
    stf = df[stratify] if stratify else None

    train, test = train_test_split(
        df,
        test_size=test_size,
        random_state=random_state,
        shuffle=shuffle,
        stratify=stf,
    )

    stf = test[stratify] if stratify else None

    test, val = train_test_split(
        test,
        test_size=0.5,
        random_state=random_state,
        shuffle=shuffle,
        stratify=stf,
    )

    return train, test, val


def X_y_split(df, target):
    """
    This function splits a dataframe into X and y.
    """
    X = df.drop(target, axis=1)
    y = df[target]
    return X, y


class CustomRobustScaler(BaseEstimator, TransformerMixin):
    """
    This class is used to scale the data.
    """

    def __init__(self, attrs):
        self.attrs = attrs

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        scaler = RobustScaler()
        X_scaled = scaler.fit_transform(X.copy()[self.attrs])
        X_scaled = pd.DataFrame(X_scaled, columns=self.attrs, index=X.index)
        for attr in self.attrs:
            X[attr] = X_scaled[attr]
        return X


class CustomOneHotEncoder(BaseEstimator, TransformerMixin):
    """
    This class is used to one hot encode the data.
    """

    def __init__(self):
        self._oh = OneHotEncoder(sparse=False)
        self._columns = None

    def fit(self, X, y=None):
        X_cat = X.select_dtypes(include=["object"])
        self._columns = pd.get_dummies(X_cat).columns
        self._oh.fit(X_cat)
        return self

    def transform(self, X, y=None):
        X_cat = pd.DataFrame(
            self._oh.transform(X.select_dtypes(include=["object"])),
            columns=self._columns,
            index=X.select_dtypes(include=["object"]).index,
        )
        X = pd.concat([X, X_cat], axis=1)
        X.drop(X.select_dtypes(include=["object"]).columns, axis=1, inplace=True)
        return X


class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    """
    This class is used to label encode the data.
    """

    def __init__(self, cols):
        self.cols = cols
        self._le = None

    def fit(self, X, y=None):
        self._le = LabelEncoder()
        self._le.fit(X[self.cols])
        return self

    def transform(self, X, y=None):
        X[self.cols] = self._le.transform(X[self.cols])
        return X

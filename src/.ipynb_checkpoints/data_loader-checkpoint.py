 import pandas as pd

 def load_data():
     """
    5. Loads the Iris dataset from an online source.
    6.
    7. Returns:
    8. pandas.DataFrame: The loaded dataset containing
    features and labels.
    9. """
    url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/mas
    ter/iris.csv"
     data = pd.read_csv(url)
    return data
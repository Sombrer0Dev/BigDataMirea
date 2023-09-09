from sklearn.datasets import fetch_california_housing
import pandas as pd
from pandas import DataFrame

if __name__ == '__main__':
    data = fetch_california_housing(as_frame=True)
    data: DataFrame = pd.DataFrame(data.data,columns=data.feature_names)

    data.isna()
import os
import pathlib

import pandas as pd
import streamlit as st


@st.cache_data
def create_df() -> pd.DataFrame:
    filepath: pathlib.Path = pathlib.Path(os.getcwd(), "data", "small.csv")
    return pd.read_csv(filepath_or_buffer=filepath, sep=",")


def main():
    st.title("Huggingface Insights")

    df: pd.DataFrame = create_df()

    st.dataframe(df)
    st.text(df.shape)


if __name__ == "__main__":
    main()

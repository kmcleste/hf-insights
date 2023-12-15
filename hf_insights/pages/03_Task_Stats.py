import os
import pathlib

import pandas as pd
import plotly.express as px
import streamlit as st


@st.cache_data
def create_df() -> pd.DataFrame:
    filepath: pathlib.Path = pathlib.Path(os.getcwd(), "data", "models.csv")
    return pd.read_csv(filepath_or_buffer=filepath, sep=",")


@st.cache_data
def group_df(df: pd.DataFrame, by: str, to_aggregate: str) -> pd.DataFrame:
    return df.groupby(by)[to_aggregate].sum().reset_index()

def create_metrics(df: pd.DataFrame):
    col1, col2 = st.columns(2)
    current_supported_tasks = col1.metric(label="Num. Supported Tasks", value=df["pipeline_tag"].nunique())
    top_task = col2.metric(label="Most Popular Task", value=df["pipeline_tag"].value_counts().sort_values(ascending=False).index[0])

def create_chart(df: pd.DataFrame, to_aggregate: str, title: str):
    grouped_df = group_df(df, "parent_category", to_aggregate)
    # Create a bar chart
    fig = px.bar(grouped_df, x="parent_category", y=to_aggregate, title=title)
    # Update layout
    fig.update_layout(
        xaxis_title="Task Group",
        yaxis_title=f"Sum of {to_aggregate}",
        xaxis={
            "categoryorder": "total descending"
        },
    )
    st.plotly_chart(fig, use_container_width=True)

def create_category_counts_chart(df: pd.DataFrame):
    category_counts =  df["parent_category"].value_counts().reset_index()
    category_counts.columns = ["parent_category", "count"]

    fig = px.bar(
        category_counts,
        x="parent_category",
        y="count",
        title="Count of Models in Each Parent Category"
    )
    fig.update_layout(
        xaxis_title="Parent Category",
        yaxis_title="Model Count"
    )
    st.plotly_chart(fig, use_container_width=True)

def main():
    df = create_df()
    with st.sidebar:
        category_filters = st.multiselect(
            label="Category Filter",
            options=df["parent_category"].unique(),
            default=df["parent_category"].unique(),
            help="Select which categories to include in analysis"
        )
        filtered_df = df[df["parent_category"].isin(category_filters)]
    if not category_filters:
        st.warning("No category filter(s) selected.")
        return
    create_metrics(df)
    create_chart(filtered_df, "likes", "Sum of Likes by Task Group")
    create_category_counts_chart(filtered_df)


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()

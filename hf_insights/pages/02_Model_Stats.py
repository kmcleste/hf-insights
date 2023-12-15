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
    return df.groupby(by).apply(lambda row: row.nlargest(5, to_aggregate)).reset_index(drop=True)


def create_scatter(df: pd.DataFrame):
    fig = px.scatter(
        df,
        x="likes",
        y="downloads",
        color="parent_category",  # This will color points by the 'parent_category' column
        template="ggplot2",
        title="Model Likes VS Downloads",
        hover_data=[
            "id",
            "likes",
            "downloads",
            "parent_category",
            "pipeline_tag",
        ]
    )

    # Adjust the layout
    fig.update_layout(
        width=512, height=512, xaxis_title="Likes", yaxis_title="Downloads"
    )
    st.plotly_chart(fig, use_container_width=True)

def create_bar(df: pd.DataFrame, by: str, to_aggregate: str, title: str):
    grouped_df = group_df(df, "parent_category", to_aggregate)
    fig = px.bar(
        grouped_df,
        x=by,
        y=to_aggregate,
        color="id",
        barmode="group",
        title=title,
        hover_data=[
            "id",
            "likes",
            "downloads",
            "parent_category",
            "pipeline_tag",
        ]
    )
    # Update layout
    fig.update_layout(
        xaxis_title=by.replace("_", " ").capitalize(),
        yaxis_title=to_aggregate.capitalize(),
    )
    fig.update_xaxes(tickmode="linear", ticklabelmode="period")
    st.plotly_chart(fig, use_container_width=True)

def create_metrics(df: pd.DataFrame):
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Num. Models 📈", value=df.shape[0])
    col2.metric(label="Total Downloads 💾", value=df["downloads"].sum())
    col3.metric(label="Total Likes 👍", value=df["likes"].sum())


def main():
    df = create_df()
    with st.sidebar:
        category_filters = st.multiselect(
            label="Category Filter",
            options=df["parent_category"].unique(),
            default=["natural-language-processing", "computer-vision", "multimodal"],
            help="Select which categories to include in analysis"
        )
        filtered_df = df[df["parent_category"].isin(category_filters)]
    if not category_filters:
        st.warning("No category filter(s) selected.")
        return
    
    create_metrics(df)
    create_scatter(filtered_df)
    create_bar(filtered_df, by="parent_category", to_aggregate="likes", title="Top 5 Models by Likes in Each Category")
    create_bar(filtered_df, by="parent_category", to_aggregate="downloads", title="Top 5 Models by Downloads in Each Category")
    


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()

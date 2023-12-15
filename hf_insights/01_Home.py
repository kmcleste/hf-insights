import streamlit as st


def main():
    st.title("Huggingface Insights")

    st.markdown("""
    ## Background

    The goal of this analysis is to perform a high level overview of which models and tasks are most popular on Huggingface.
    Seeing as Huggingface is currently the defacto standard for model hosting and sharing,
    it is safe to assume any patterns observed should be a good indicator of industry trends and user interests.
    These simple metrics can also provide insight into the current "model market" saturation that exists -- models are being
    pumped out daily and it's no wonder MLE's and Data Scientists might be feeling overwhelemed!
    There's an incredible amount of information and buzz regarding SOTA models to wade through; hopefully this dashboard
    can help you narrow down some areas of interest.
            
    ## The Data
    
    The data used in this project was scraped from [https://huggingface.co/models](https://huggingface.co/models). Various statistics,
    such as likes, downloads, model author, model id, repo type, and task, were collected. The data scrape occurred September 22nd.
    At the rate the AI/ML industry moves, that means this data is wildly outdated at this point -- but should serve as a reference point
    for the overall interest the community has particular types of models and which authors are most active.
                
    ## Future Work
                
    If I were to continue working on this project, I would like to schedule perioding data collections to get a better view
    into model/author/task trends. To be frank, bar charts aren't very interesting to look at and time series data could tell us
    a lot more about hype cycles, velocity of model adoption and the markets changing risk tolerance regarding open-source models.
                
    ## Getting Started
                
    To access the visualizations, select a page from the sidebar.
    """)


if __name__ == "__main__":
    st.set_page_config(layout="centered")
    main()

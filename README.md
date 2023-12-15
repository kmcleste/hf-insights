# Huggingface Insights

[![Streamlit badge](https://img.shields.io/badge/Streamlit-Cloud-red?style=flat-sqaure)](https://kmcleste-hf-insights-hf-insights01-home-ibivet.streamlit.app/)

The goal of this analysis is to perform a high level overview of which models and tasks are most popular on Huggingface. Seeing as Huggingface is currently the defacto standard for model hosting and sharing, it is safe to assume any patterns observed should be a good indicator of industry trends and user interests. These simple metrics can also provide insight into the current "model market" saturation that exists -- models are being pumped out daily and it's no wonder MLE's and Data Scientists might be feeling overwhelemed! There's an incredible amount of information and buzz regarding SOTA models to wade through; hopefully this dashboard can help you narrow down some areas of interest.

Here is a link to the [public tableau workbook](https://public.tableau.com/shared/8MNBSMBQC?:display_count=n&:origin=viz_share_link).

## Prerequisite

To download the dataset, you will need git-lfs. See [these instructions](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) on how to install.

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/kmcleste/huggingface-model-data.git
    ```

2. Inside the repo directory, download the dataset:

    ```bash
    git lfs pull
    ```

3. (Optional) To run the webscraping notebook or locally host the streamlit ui, you will need to install the python dependencies:

    ```bash
    # Create a virtual environment
    python -m venv venv
    # Source the environment
    source venv/bin/activate
    # Install dependencies
    pip install -r requirements.txt
    # Run the UI
    make ui
    ```

    Note: If you decide to run the notebook, scraping will take ~ 45 minutes

## Data

The data used in this project was scraped from [https://huggingface.co/models](https://huggingface.co/models). Various statistics, such as likes, downloads, model author, model id, repo type, and task, were collected. The data scrape occurred September 22nd. At the rate the AI/ML industry moves, that means this data is wildly outdated at this point -- but should serve as a reference point for the overall interest the community has particular types of models and which authors are most active.

| Column        | Type                |
| ------------- | ------------------- |
| downloads     | int                 |
| id            | str                 |
| lastModified  | datetime (iso-8601) |
| likes         | int                 |
| pipeline_tag  | str                 |
| private       | bool                |
| repoType      | str                 |
| author        | str                 |
| authorData    | dict                |

## Future Work

 If I were to continue working on this project, I would like to schedule perioding data collections to get a better view
 into model/author/task trends. To be frank, bar charts aren't very interesting to look at and time series data could tell us
 a lot more about hype cycles, velocity of model adoption and the markets changing risk tolerance regarding open-source models.

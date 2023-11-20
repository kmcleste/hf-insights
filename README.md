# Huggingface Insights

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

3. (Optional) To run the notebook, you will need to install the python dependencies:

    ```bash
    # Create a virtual environment
    python -m venv venv
    # Source the environment
    source venv/bin/activate
    # Install dependencies
    pip install -r requirements.txt
    ```

    Note: If you decide to run the notebook, scraping will take ~ 45 minutes

## Data

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

Given that this is just a first pass, there are many things I would like to explore going forward. For one, it would be incredibly beneficial to convert this data into a time series. To do so would be as simple as running a CRON job to pull the latest model metrics. With this, we would be able to better understand model hype. I would also be interested to explore the top N models, their respective companies (if applicable), the techniques used to train these models, funding required, and any novel approaches used.

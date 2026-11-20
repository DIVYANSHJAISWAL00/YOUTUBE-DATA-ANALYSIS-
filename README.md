# YouTube Multi-Channel Analytics (Python Data Analysis Project)

A step-by-step data analysis project in Python that cleans a YouTube video dataset and compares channels and categories using views, likes, comments and engagement rate.

> **Note:** The dataset is DEMO / sample data for learning, not real YouTube statistics.

## Objective

Clean a raw dataset, analyze performance by channel, category and month, create charts, and export the cleaned data.

**Engagement Rate (%) = (Likes + Comments) / Views x 100**

## Dataset

`YouTube_Multi_Channel_Analytics.xlsx` (sheet: `Video_Data`)

- 50 videos from 10 channels (Jan to May 2026)
- Columns: Video_ID, Channel_Name, Video_Title, Category, Published_Date, Views, Likes, Comments, Engagement_Rate_%

## Project steps

1. Import libraries
2. Load the Excel file
3. Understand the dataset
4. Check duplicate records
5. Remove exact duplicates
6. Clean text columns
7. Correct data types
8. Check missing values
9. Handle missing values
10. Create / verify the engagement rate column
11. Calculate key business metrics
12. Analyze performance by channel
13. Analyze performance by category
14. Analyze monthly performance
15. Visualize views by channel
16. Visualize views and engagement by category
17. Visualize monthly trend
18. Export cleaned data and summary reports
19. Interpretation and observations

## Key findings

- Total views: **23,603,659** across 50 videos and 10 channels
- Most views: **Travel Diaries** (3,301,294)
- Best engagement rate: **News Lens** (7.21%)
- Most views by category: **Science & Technology**; best engagement: **People & Blogs**
- Best month: **March 2026**, mainly because it had the most videos (17); average views per video stayed about the same every month
- Data quality: no duplicates or missing values, but category labels do not always match the channel

## Tools used

Python 3.12, Pandas, Matplotlib, OpenPyXL, VS Code

## How to run

1. Keep `youtube_data_analysis.py` and `YouTube_Multi_Channel_Analytics.xlsx` in the same folder.
2. Install the packages:
   ```
   pip install pandas matplotlib openpyxl
   ```
3. Run the script:
   ```
   python youtube_data_analysis.py
   ```
   (On Windows you can also use `py youtube_data_analysis.py`.)

The script prints the results, shows 3 charts (close one chart window to see the next), and saves 4 CSV files in the same folder.

## Output files

| File | Contents |
|---|---|
| `youtube_videos_cleaned.csv` | Cleaned video-level data |
| `views_summary_by_channel.csv` | Total views per channel |
| `views_summary_by_category.csv` | Total views per category |
| `monthly_views_summary.csv` | Total views per month |

## Limitations

The cleaning choices are teaching assumptions. In a real project, confirm business rules with the data owner before deleting or replacing records.

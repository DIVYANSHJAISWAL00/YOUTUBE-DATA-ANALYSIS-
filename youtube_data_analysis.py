"""
YouTube Multi-Channel Analytics - Step-by-Step Python Project
Keep YouTube_Multi_Channel_Analytics.xlsx in the same folder as this file.
Install if needed:  pip install pandas matplotlib openpyxl
Run:                python youtube_data_analysis.py
(Note: data in the workbook is DEMO / SAMPLE data.)
"""

try:
    from IPython.display import display
except ImportError:
    display = print   # plain Python fallback


# ============================================================
# Step 1 – Import libraries
# ============================================================
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# Step 2 – Load the Excel file
# ============================================================
df = pd.read_excel("YouTube_Multi_Channel_Analytics.xlsx", sheet_name="Video_Data")

print("Dataset loaded successfully")
print("Rows and columns:", df.shape)
display(df.head())

# ============================================================
# Step 3 – Understand the dataset
# ============================================================
print("Column names:")
print(df.columns.tolist())

print("\nData types and non-null counts:")
df.info()

print("\nSummary statistics:")
display(df.describe(include="all"))

# ============================================================
# Step 4 – Check duplicate records
# ============================================================
duplicate_count = df.duplicated().sum()
duplicate_ids = df["Video_ID"].duplicated().sum()

print("Exact duplicate rows:", duplicate_count)
print("Repeated Video_ID values:", duplicate_ids)

# ============================================================
# Step 5 – Remove exact duplicates
# ============================================================
df = df.drop_duplicates().copy()
df = df.drop_duplicates(subset="Video_ID", keep="first").copy()

print("Shape after removing duplicates:", df.shape)

# ============================================================
# Step 6 – Clean text columns
# ============================================================
for column in ["Channel_Name", "Video_Title", "Category"]:
    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

print(df[["Channel_Name", "Category"]].nunique())

# ============================================================
# Step 7 – Correct data types
# ============================================================
df["Published_Date"] = pd.to_datetime(df["Published_Date"], errors="coerce")
df["Views"] = pd.to_numeric(df["Views"], errors="coerce")
df["Likes"] = pd.to_numeric(df["Likes"], errors="coerce")
df["Comments"] = pd.to_numeric(df["Comments"], errors="coerce")
df["Engagement_Rate_%"] = pd.to_numeric(df["Engagement_Rate_%"], errors="coerce")

print(df.dtypes)

# ============================================================
# Step 8 – Check missing values
# ============================================================
display(df.isnull().sum())

# ============================================================
# Step 9 – Handle missing values
# ============================================================
rows_before = len(df)

df = df.dropna(
    subset=["Published_Date", "Channel_Name", "Category", "Views", "Likes", "Comments"]
).copy()

df["Views"] = df["Views"].astype(int)
df["Likes"] = df["Likes"].astype(int)
df["Comments"] = df["Comments"].astype(int)
df["Video_Title"] = df["Video_Title"].fillna("Unknown")

print("Rows removed:", rows_before - len(df))
print("Rows remaining:", len(df))
display(df.isnull().sum())

# ============================================================
# Step 10 – Create an engagement rate column
# ============================================================
df["Engagement_Calc_%"] = (df["Likes"] + df["Comments"]) / df["Views"] * 100

matches = (df["Engagement_Calc_%"] - df["Engagement_Rate_%"]).abs().max() < 0.01
print("Recalculated engagement matches the original column:", matches)

display(df.head())

# ============================================================
# Step 11 – Calculate key business metrics
# ============================================================
total_videos = df["Video_ID"].nunique()
total_channels = df["Channel_Name"].nunique()
total_views = df["Views"].sum()
total_likes = df["Likes"].sum()
total_comments = df["Comments"].sum()
average_engagement = df["Engagement_Calc_%"].mean()
overall_engagement = (total_likes + total_comments) / total_views * 100

print(f"Videos analysed: {total_videos}")
print(f"Channels: {total_channels}")
print(f"Total views: {total_views:,}")
print(f"Total likes: {total_likes:,}")
print(f"Total comments: {total_comments:,}")
print(f"Average engagement rate (per video): {average_engagement:.2f}%")
print(f"Overall engagement rate (all videos combined): {overall_engagement:.2f}%")

# ============================================================
# Step 12 – Analyze performance by channel
# ============================================================
channel_views = (
    df.groupby("Channel_Name")["Views"]
    .sum()
    .sort_values(ascending=False)
)

channel_engagement = (
    df.groupby("Channel_Name")["Engagement_Calc_%"]
    .mean()
    .sort_values(ascending=False)
)

display(channel_views)
display(channel_engagement)
print("Top channel by views:", channel_views.idxmax())
print("Top channel by engagement:", channel_engagement.idxmax())

# ============================================================
# Step 13 – Analyze performance by category
# ============================================================
category_views = (
    df.groupby("Category")["Views"]
    .sum()
    .sort_values(ascending=False)
)

category_engagement = (
    df.groupby("Category")["Engagement_Calc_%"]
    .mean()
    .sort_values(ascending=False)
)

display(category_views)
display(category_engagement)
print("Top category by views:", category_views.idxmax())
print("Top category by engagement:", category_engagement.idxmax())

print("\nTop 5 videos by views:")
display(
    df.nlargest(5, "Views")[["Channel_Name", "Video_Title", "Category", "Views", "Engagement_Calc_%"]]
)

# ============================================================
# Step 14 – Analyze monthly performance
# ============================================================
df["Month"] = df["Published_Date"].dt.to_period("M").astype(str)

monthly_views = df.groupby("Month")["Views"].sum().sort_index()
display(monthly_views)

print("Best month:", monthly_views.idxmax())

# ============================================================
# Step 15 – Visualize views by channel
# ============================================================
channel_views.plot(kind="bar", title="Total Views by Channel", ylabel="Views", figsize=(9, 5))
plt.xlabel("Channel")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# ============================================================
# Step 16 – Visualize views and engagement by category
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

category_views.plot(kind="bar", ax=axes[0], title="Total Views by Category", ylabel="Views")
category_engagement.plot(kind="bar", ax=axes[1], title="Average Engagement Rate by Category", ylabel="Engagement (%)", color="tab:orange")

for ax in axes:
    ax.set_xlabel("Category")
    ax.tick_params(axis="x", rotation=45)
    for label in ax.get_xticklabels():
        label.set_ha("right")

plt.tight_layout()
plt.show()

# ============================================================
# Step 17 – Visualize monthly trend
# ============================================================
monthly_views.plot(kind="line", marker="o", title="Monthly Views Trend", ylabel="Views", figsize=(8, 4))
plt.xlabel("Month")
plt.tight_layout()
plt.show()

# ============================================================
# Step 18 – Export cleaned data and summary reports
# ============================================================
df.to_csv("youtube_videos_cleaned.csv", index=False)
channel_views.to_csv("views_summary_by_channel.csv", header=["Views"])
category_views.to_csv("views_summary_by_category.csv", header=["Views"])
monthly_views.to_csv("monthly_views_summary.csv", header=["Views"])

print("Export complete!")

# ============================================================
# Step 19 – Student interpretation
# ============================================================
# Helper: quick answers to compare with your own observations
print("1. Most views (channel):", channel_views.idxmax())
print("2. Best engagement (channel):", channel_engagement.idxmax())
print("3. Most views (category):", category_views.idxmax())
print("4. Best month:", monthly_views.idxmax())

# Data quality check: do category labels match the channel?
print("\n5. Categories used by each channel:")
display(df.groupby("Channel_Name")["Category"].apply(lambda s: ", ".join(sorted(s.unique()))))

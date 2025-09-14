# Vancouver AI Hackathon Round 4: The Soundtrack of Us

Survey data from 1,261+ participants about music discovery, consumption, and attitudes toward AI-generated music.

## What's In The Dataset

### The Data
- **1,261+ complete responses** from music listeners across Canada
- **19 core questions** covering music discovery, format evolution, and AI attitudes
- **Rich demographics**: Age, location, education, income, household composition
- **3,000+ text responses** with sentiment analysis scores
- **Geographic distribution**: Ontario (40%+), BC (20%+), Alberta, Quebec, and more

### Question Categories
- **Music Discovery**: How people find new music (radio, streaming, social media, etc.)
- **Format Evolution**: Personal experiences with vinyl, cassettes, CDs, downloads, streaming
- **Listening Habits**: When and how people consume music in daily life
- **AI Music Attitudes**: Responses to AI-generated music and voice cloning
- **Social Sharing**: How people share music and their guilty pleasures
- **Personal Connection**: Life theme songs and meaningful lyrics

## Quick Start

### Explore the Data

```bash
# Open the main dataset
open "data/raw/music_survey_data.csv"
# or run the exploration script
python scripts/explore_data.py
```

### Python + Pandas
```python
import pandas as pd

# Load the data
df = pd.read_csv('data/raw/music_survey_data.csv')

# Basic exploration
print(f"Total responses: {len(df)}")
print(f"Columns: {len(df.columns)}")

# Find open-ended responses
oe_columns = [col for col in df.columns if '_OE' in col and 'sentiment' not in col]
print(f"Open-ended questions: {len(oe_columns)}")

# Sample responses
theme_songs = df['Q18_Life_theme_song'].dropna()
print(f"Life theme songs: {len(theme_songs)}")
```

### R + Tidyverse
```r
library(tidyverse)

# Load data
music_survey <- read_csv("data/raw/music_survey_data.csv")

# Quick overview
glimpse(music_survey)

# Find text responses
text_columns <- music_survey %>% 
  select(ends_with("_OE")) %>% 
  names()
```

## Data Structure

### Key Columns
- `Q1_Relationship_with_music`: Music engagement level
- `Q2_Discovering_music`: Primary music discovery method
- `Q4_Music_format_changes`: Experience with format transitions
- `Q7_New_music_discover_*`: Multiple discovery methods
- `Q8_Music_listen_time_GRID_*`: Listening habits by activity
- `Q10_Songs_by_AI`: Attitudes toward AI-generated music
- `Q11_Use_of_dead_artists_voice_feelings`: AI voice cloning opinions
- `Q12_Music_bingo_*`: Music-related behaviors
- `Q13_Share_the_music_you_love_*`: Music sharing methods
- `Q15_Music_guilty_pleasure`: Musical guilty pleasures
- `Q18_Life_theme_song`: Personal theme songs
- `Q19_Lyric_that_stuck_with_you`: Meaningful lyrics

### Demographics
- `AgeGroup_Broad`: 18-34, 35-54, 55+
- `Province`: Geographic distribution
- `Education`: Education level
- `HH_Income_Fine_23`: Household income
- `Gender`: Gender distribution

### Sentiment Analysis
- Sentiment scores included for open-ended responses
- Polarity and subjectivity measures available
- Percentage scores for emotional content

## File Structure

```
vanai-hackathon-004/
├── README.md                           # This guide
├── data/
│   ├── raw/
│   │   ├── music_survey_data.csv      # Main dataset
│   │   └── survey_questions.txt       # Original survey questions
│   ├── processed/                     # Cleaned/transformed data
│   └── analysis/                      # Analysis outputs
├── scripts/
│   ├── explore_data.py                # Basic data exploration
│   └── data_preprocessing.py          # Data cleaning utilities
├── notebooks/                         # Jupyter notebooks for analysis
├── src/                              # Source code for applications
├── frontend/                         # Web applications
├── submissions/                      # Hackathon submissions
└── docs/                            # Documentation
```

## Getting Started Scripts

### Basic Data Exploration
```bash
python scripts/explore_data.py
```

This script will:
- Load and display basic dataset information
- Show column names and data types
- Display summary statistics for key variables
- Identify open-ended response columns
- Show sample responses

### Data Preprocessing
```bash
python scripts/data_preprocessing.py
```

This script provides utilities for:
- Cleaning and standardizing responses
- Handling missing values
- Creating derived variables
- Preparing data for analysis

## Hackathon Challenge

Using this dataset, create an experience that's **interactive, visual, or narrative-driven**. The goal is to transform raw survey data into compelling insights about music, technology, and human behavior.

### Submission Requirements
- **Format Freedom**: Visual display, interactive demo, live performance, or unconventional approach
- **Bite-Sized Impact**: Engaging experience within 2-5 minutes
- **Technical Details**: Include all software, hardware, and instructions needed
- **Data Grounding**: Story must be grounded in the actual data
- **AI Integration**: Incorporate AI tools to enhance your narrative

### Judging Criteria
- **Creativity & Innovation (25%)**: Fresh, original approach
- **Clarity & Effectiveness (25%)**: Clear communication of insights
- **Engagement & Impact (20%)**: Compelling and memorable experience
- **Technical Execution (20%)**: Well-implemented solution
- **Community Value (10%)**: Open-source tools, shared methodologies

## License & Usage

This dataset is provided for hackathon use. Please respect participant privacy and use data responsibly.

## About

1,261+ music stories from across Canada. Your mission: transform these signals into prototypes, insights, and experiences that reveal how music connects us to technology, culture, and each other.

---

*Ready to explore? Start with the basic exploration script, then dive into the data to discover your own insights and stories.*

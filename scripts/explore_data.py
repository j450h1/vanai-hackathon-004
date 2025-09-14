#!/usr/bin/env python3
"""
Basic data exploration script for Vancouver AI Hackathon Round 4
The Soundtrack of Us - Music Survey Dataset
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_data():
    """Load the music survey dataset"""
    data_path = Path(__file__).parent.parent / "data" / "raw" / "music_survey_data.csv"
    
    try:
        df = pd.read_csv(data_path)
        print(f"✅ Dataset loaded successfully")
        return df
    except FileNotFoundError:
        print(f"❌ Dataset not found at {data_path}")
        print("Please ensure the dataset is in the correct location")
        return None
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

def basic_info(df):
    """Display basic dataset information"""
    print("\n" + "="*60)
    print("📊 DATASET OVERVIEW")
    print("="*60)
    
    print(f"Total responses: {len(df):,}")
    print(f"Total columns: {len(df.columns)}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
    
    print(f"\nDate range:")
    if 'engagement_started_EDT' in df.columns:
        start_dates = pd.to_datetime(df['engagement_started_EDT'], errors='coerce')
        print(f"  From: {start_dates.min()}")
        print(f"  To: {start_dates.max()}")
    
    print(f"\nGeographic distribution:")
    if 'Province' in df.columns:
        province_counts = df['Province'].value_counts().head()
        for province, count in province_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {province}: {count} ({percentage:.1f}%)")

def column_overview(df):
    """Display column information"""
    print("\n" + "="*60)
    print("📋 COLUMN OVERVIEW")
    print("="*60)
    
    print("Question columns:")
    question_cols = [col for col in df.columns if col.startswith('Q')]
    print(f"  Found {len(question_cols)} question columns")
    
    print("\nOpen-ended response columns:")
    oe_cols = [col for col in df.columns if '_OE' in col and 'sentiment' not in col]
    print(f"  Found {len(oe_cols)} open-ended response columns")
    for col in oe_cols[:5]:  # Show first 5
        non_null_count = df[col].notna().sum()
        print(f"    {col}: {non_null_count} responses")
    
    print("\nSentiment analysis columns:")
    sentiment_cols = [col for col in df.columns if 'sentiment' in col]
    print(f"  Found {len(sentiment_cols)} sentiment analysis columns")
    
    print("\nDemographic columns:")
    demo_cols = ['AgeGroup_Broad', 'Province', 'Education', 'Gender', 'HH_Income_Fine_23']
    available_demo_cols = [col for col in demo_cols if col in df.columns]
    for col in available_demo_cols:
        unique_values = df[col].nunique()
        print(f"    {col}: {unique_values} unique values")

def response_patterns(df):
    """Show response patterns for key questions"""
    print("\n" + "="*60)
    print("🎵 RESPONSE PATTERNS")
    print("="*60)
    
    # Music relationship
    if 'Q1_Relationship_with_music' in df.columns:
        print("\nMusic relationship levels:")
        relationship_counts = df['Q1_Relationship_with_music'].value_counts()
        for response, count in relationship_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {response}: {count} ({percentage:.1f}%)")
    
    # Music discovery methods
    if 'Q2_Discovering_music' in df.columns:
        print("\nPrimary music discovery methods:")
        discovery_counts = df['Q2_Discovering_music'].value_counts().head()
        for method, count in discovery_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {method}: {count} ({percentage:.1f}%)")
    
    # Age distribution
    if 'AgeGroup_Broad' in df.columns:
        print("\nAge distribution:")
        age_counts = df['AgeGroup_Broad'].value_counts()
        for age_group, count in age_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {age_group}: {count} ({percentage:.1f}%)")

def sample_responses(df):
    """Show sample responses from open-ended questions"""
    print("\n" + "="*60)
    print("💭 SAMPLE RESPONSES")
    print("="*60)
    
    # Find open-ended columns
    oe_cols = [col for col in df.columns if '_OE' in col and 'sentiment' not in col]
    
    for col in oe_cols[:3]:  # Show first 3 open-ended columns
        print(f"\n{col}:")
        responses = df[col].dropna()
        if len(responses) > 0:
            print(f"  Total responses: {len(responses)}")
            # Show a sample response
            sample_response = responses.iloc[0]
            preview = sample_response[:100] + "..." if len(sample_response) > 100 else sample_response
            print(f"  Sample: \"{preview}\"")
        else:
            print("  No responses available")

def missing_data_summary(df):
    """Show missing data summary"""
    print("\n" + "="*60)
    print("🔍 MISSING DATA SUMMARY")
    print("="*60)
    
    missing_data = df.isnull().sum()
    missing_percentage = (missing_data / len(df)) * 100
    
    # Show columns with most missing data
    missing_summary = pd.DataFrame({
        'Column': missing_data.index,
        'Missing_Count': missing_data.values,
        'Missing_Percentage': missing_percentage.values
    })
    
    missing_summary = missing_summary[missing_summary['Missing_Count'] > 0].sort_values('Missing_Percentage', ascending=False)
    
    if len(missing_summary) > 0:
        print("Top 10 columns with missing data:")
        for _, row in missing_summary.head(10).iterrows():
            print(f"  {row['Column']}: {row['Missing_Count']} ({row['Missing_Percentage']:.1f}%)")
    else:
        print("No missing data found!")

def main():
    """Main exploration function"""
    print("🎵 Vancouver AI Hackathon Round 4: The Soundtrack of Us")
    print("Data Exploration Script")
    print("="*60)
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Run exploration
    basic_info(df)
    column_overview(df)
    response_patterns(df)
    sample_responses(df)
    missing_data_summary(df)
    
    print("\n" + "="*60)
    print("✅ Exploration complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Examine specific columns of interest")
    print("2. Create visualizations of key patterns")
    print("3. Analyze relationships between variables")
    print("4. Develop your hackathon project idea")
    print("\nHappy exploring! 🚀")

if __name__ == "__main__":
    main()

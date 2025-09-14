#!/usr/bin/env python3
"""
Simple data exploration script (no external dependencies)
for Vancouver AI Hackathon Round 4: The Soundtrack of Us
"""

import csv
import os
from pathlib import Path

def load_data():
    """Load the music survey dataset using only standard library"""
    data_path = Path(__file__).parent.parent / "data" / "raw" / "music_survey_data.csv"
    
    if not data_path.exists():
        print(f"❌ Dataset not found at {data_path}")
        return None
    
    try:
        with open(data_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = list(reader)
        
        print(f"✅ Dataset loaded successfully")
        return headers, rows
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

def basic_info(headers, rows):
    """Display basic dataset information"""
    print("\n" + "="*60)
    print("📊 DATASET OVERVIEW")
    print("="*60)
    
    print(f"Total responses: {len(rows):,}")
    print(f"Total columns: {len(headers)}")
    
    # File size
    data_path = Path(__file__).parent.parent / "data" / "raw" / "music_survey_data.csv"
    file_size = data_path.stat().st_size / 1024 / 1024
    print(f"File size: {file_size:.1f} MB")
    
    print(f"\nColumn names (first 10):")
    for i, header in enumerate(headers[:10]):
        print(f"  {i+1}. {header}")
    if len(headers) > 10:
        print(f"  ... and {len(headers) - 10} more columns")

def find_question_columns(headers):
    """Find question columns and open-ended responses"""
    print("\n" + "="*60)
    print("📋 COLUMN OVERVIEW")
    print("="*60)
    
    question_cols = [h for h in headers if h.startswith('Q')]
    print(f"Question columns: {len(question_cols)}")
    
    oe_cols = [h for h in headers if '_OE' in h and 'sentiment' not in h]
    print(f"Open-ended response columns: {len(oe_cols)}")
    
    sentiment_cols = [h for h in headers if 'sentiment' in h]
    print(f"Sentiment analysis columns: {len(sentiment_cols)}")
    
    demo_cols = ['AgeGroup_Broad', 'Province', 'Education', 'Gender', 'HH_Income_Fine_23']
    available_demo_cols = [h for h in demo_cols if h in headers]
    print(f"Demographic columns: {len(available_demo_cols)}")
    
    return question_cols, oe_cols, sentiment_cols

def sample_responses(headers, rows, oe_cols):
    """Show sample responses from open-ended questions"""
    print("\n" + "="*60)
    print("💭 SAMPLE RESPONSES")
    print("="*60)
    
    for col in oe_cols[:3]:  # Show first 3
        col_index = headers.index(col)
        responses = [row[col_index] for row in rows if row[col_index].strip()]
        
        print(f"\n{col}:")
        print(f"  Total responses: {len(responses)}")
        if responses:
            sample = responses[0]
            preview = sample[:100] + "..." if len(sample) > 100 else sample
            print(f"  Sample: \"{preview}\"")

def main():
    """Main exploration function"""
    print("🎵 Vancouver AI Hackathon Round 4: The Soundtrack of Us")
    print("Simple Data Exploration Script (No Dependencies)")
    print("="*60)
    
    # Load data
    result = load_data()
    if result is None:
        return
    
    headers, rows = result
    
    # Run exploration
    basic_info(headers, rows)
    question_cols, oe_cols, sentiment_cols = find_question_columns(headers)
    sample_responses(headers, rows, oe_cols)
    
    print("\n" + "="*60)
    print("✅ Basic exploration complete!")
    print("="*60)
    print("\nTo install full analysis tools:")
    print("pip install -r requirements.txt")
    print("\nThen run:")
    print("python scripts/explore_data.py")
    print("\nHappy exploring! 🚀")

if __name__ == "__main__":
    main()

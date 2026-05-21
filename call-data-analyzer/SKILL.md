---
name: call-data-analyzer
description: |
  Analyze call center or voice AI bot data to understand customer sentiment, issue patterns, and support quality.
  
  Use this skill whenever you need to:
  - Analyze voice bot or call center CSV data for performance metrics
  - Understand customer sentiment and frustration patterns
  - Generate detailed Excel reports breaking down issues by type and sentiment
  - Extract call references and CSAT scores for specific customer issues
  - Identify what's driving negative customer experiences
  - Create multi-sheet Excel workbooks with call analysis
  - Analyze support bot effectiveness across different issue categories
  
  You provide the CSV file(s), the skill generates comprehensive analysis with visualizations and insights.
---

# Call Data Analyzer

Transform raw call center data into actionable insights with comprehensive sentiment analysis, issue categorization, and CSAT tracking.

## What This Skill Does

Analyzes CSV files containing call data (particularly from voice AI bots or call centers) and produces:

1. **Excel Workbook** with 5 analysis sheets:
   - **Issue Type Analysis**: Each issue category with call counts, sentiment breakdown, negative sentiment %, CSAT scores
   - **All Calls Data**: Complete call-by-call data with Call IDs, sentiment, CSAT, resolution status
   - **CSAT Analysis**: All CSAT responses with call references for quality auditing
   - **Negative Sentiment Calls**: Detailed view of frustrated customers with friction points
   - **Summary Statistics**: High-level metrics and KPIs

2. **Sentiment Insights**:
   - Automatic sentiment classification (Positive/Neutral/Negative)
   - Correlation with CSAT scores
   - Sentiment breakdown by issue type and resolution status

## Input Requirements

CSV file with:
- `Call ID` - Unique identifier
- `Summary` - JSON field with issue category, resolution status, CSAT score, friction points

## Output

- Excel workbook (5 sheets, all with call IDs for reference)
- Markdown analysis documents
- Color-coded sentiment data

## How to Use

Upload your call CSV file and request analysis. The skill will:
1. Parse call summaries and sentiment
2. Categorize by issue type
3. Calculate metrics by sentiment and CSAT
4. Generate Excel report with call references
5. Provide actionable insights

Example:
```
User: "Analyze my voice bot call data from May 20-21. I need to understand 
       what's causing negative sentiment and get an Excel report with call IDs."

Claude: "I'll analyze your 5,386 calls and generate a comprehensive Excel workbook..."
```

## Key Features

✓ Sentiment analysis with CSAT correlation
✓ Call-by-call reference data for auditing
✓ Issue categorization and severity ranking
✓ Friction point extraction (customer complaints)
✓ Multi-sheet Excel reports
✓ Support for multiple brands and providers
✓ Extensible for future enhancements

## Supported Languages

- English
- Hindi (and Hindi-English code-switching)


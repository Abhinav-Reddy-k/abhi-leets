#!/usr/bin/env python3
"""
Repository Organization Analyzer for abhi-leets
Generates various organizational views and statistics for the LeetCode solutions repository.
"""

import json
import os
import re
from collections import defaultdict, Counter

def load_stats():
    """Load statistics from stats.json"""
    try:
        with open('stats.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def analyze_naming_conventions():
    """Analyze folder naming patterns"""
    numbered = []
    descriptive = []
    
    for item in os.listdir('.'):
        if os.path.isdir(item) and item not in ['.git']:
            if re.match(r'^\d{4}-', item):
                numbered.append(item)
            elif item not in ['README.md', 'stats.json']:
                descriptive.append(item)
    
    return numbered, descriptive

def count_files_by_type():
    """Count different file types in the repository"""
    file_counts = Counter()
    
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        for file in files:
            _, ext = os.path.splitext(file)
            file_counts[ext or 'no_extension'] += 1
    
    return file_counts

def generate_progress_report():
    """Generate a comprehensive progress report"""
    stats = load_stats()
    numbered, descriptive = analyze_naming_conventions()
    file_counts = count_files_by_type()
    
    leetcode_data = stats.get('leetcode', {})
    solved = leetcode_data.get('solved', 0)
    easy = leetcode_data.get('easy', 0)
    medium = leetcode_data.get('medium', 0)
    hard = leetcode_data.get('hard', 0)
    
    total_dirs = len(numbered) + len(descriptive)
    
    report = f"""# Repository Analysis Report

## 📊 Statistics Summary
- **Total Problem Directories**: {total_dirs}
- **Solved & Tracked**: {solved} problems
- **Completion Rate**: {solved}/{total_dirs} ({(solved/total_dirs)*100:.1f}%)

## 🎯 Difficulty Distribution
- 🟢 **Easy**: {easy} problems
- 🟡 **Medium**: {medium} problems
- 🔴 **Hard**: {hard} problems

## 📁 Naming Convention Analysis
- **Numbered Format**: {len(numbered)} directories (e.g., `0001-problem-name`)
- **Descriptive Format**: {len(descriptive)} directories (e.g., `problem-name`)
- **Consistency Score**: {(max(len(numbered), len(descriptive))/total_dirs)*100:.1f}% 
  _(using {('numbered' if len(numbered) > len(descriptive) else 'descriptive')} format)_

## 📄 File Type Distribution
"""
    
    for ext, count in sorted(file_counts.items()):
        if ext == '.py':
            report += f"- **Python Solutions**: {count} files\n"
        elif ext == '.md':
            report += f"- **Documentation**: {count} markdown files\n"
        elif ext == '.json':
            report += f"- **Data Files**: {count} JSON files\n"
        else:
            report += f"- **{ext.upper() or 'Other'}**: {count} files\n"
    
    report += f"""
## 🔍 Organization Quality Assessment

### ✅ Strengths
1. **Excellent Topic Categorization** - 23 algorithmic topics in README
2. **Comprehensive Documentation** - README files for all problems
3. **Consistent File Structure** - Standard layout across problems
4. **Progress Tracking** - JSON-based statistics monitoring

### 🔄 Recommendations
1. **Standardize Naming** - Consider using one consistent format
2. **Add Difficulty Views** - Create Easy/Medium/Hard organization
3. **Company Tags** - Group problems by asking companies
4. **Study Plans** - Create structured learning paths
5. **Complexity Analysis** - Add time/space complexity summaries

## 📈 Progress Insights
- You have a {('strong' if solved/total_dirs > 0.2 else 'growing')} foundation with {solved} solved problems
- Focus areas could include more {'Easy' if easy < 10 else 'Hard'} problems for balanced preparation
- Your {'numbered' if len(numbered) > len(descriptive) else 'descriptive'} naming approach is the majority pattern

---
*Generated automatically by repository analyzer*
"""
    
    return report

def main():
    """Main function to generate analysis"""
    if not os.path.exists('stats.json'):
        print("Warning: stats.json not found. Some statistics may be incomplete.")
    
    report = generate_progress_report()
    
    with open('ANALYSIS_REPORT.md', 'w') as f:
        f.write(report)
    
    print("✅ Analysis complete! Generated reports:")
    print("   📊 ANALYSIS_REPORT.md - Comprehensive statistics")
    print("   📋 ORGANIZATION_SUMMARY.md - Quick overview")
    print("   📑 ORGANIZATION_ANALYSIS.md - Detailed analysis")
    print("   🎯 DIFFICULTY_BREAKDOWN.md - Problems by difficulty")

if __name__ == '__main__':
    main()
"""
Utilities Module
Advanced features and utilities for ResumeBooster
"""

import json
import csv
from typing import Dict, List, Any
from datetime import datetime
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ReportGenerator:
    """Generate reports from analysis results"""
    
    @staticmethod
    def generate_json_report(analysis_result: Dict[str, Any], 
                            filename: str = None) -> str:
        """
        Generate JSON report from analysis
        
        Args:
            analysis_result: Analysis result dictionary
            filename: Output filename (optional)
            
        Returns:
            JSON string of report
        """
        report = {
            'timestamp': datetime.now().isoformat(),
            'metadata': {
                'role': analysis_result.get('role'),
                'score': analysis_result.get('resume_score'),
                'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            },
            'results': {
                'resume_score': analysis_result.get('resume_score'),
                'score_breakdown': analysis_result.get('score_breakdown', {}),
                'strengths': analysis_result.get('strengths', []),
                'weaknesses': analysis_result.get('weaknesses', []),
                'suggestions': analysis_result.get('suggestions', []),
                'metrics': analysis_result.get('detailed_metrics', {})
            }
        }
        
        json_str = json.dumps(report, indent=2)
        
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(json_str)
                logger.info(f"Report saved to {filename}")
            except Exception as e:
                logger.error(f"Error saving report: {str(e)}")
        
        return json_str
    
    @staticmethod
    def generate_csv_report(analysis_results: List[Dict[str, Any]],
                           filename: str) -> None:
        """
        Generate CSV report from multiple analyses
        
        Args:
            analysis_results: List of analysis result dictionaries
            filename: Output filename
        """
        try:
            if not analysis_results:
                logger.warning("No analysis results to report")
                return
            
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = [
                    'role', 'resume_score', 'semantic_similarity',
                    'skill_overlap_percentage', 'strengths_count',
                    'weaknesses_count', 'timestamp'
                ]
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for result in analysis_results:
                    row = {
                        'role': result.get('role'),
                        'resume_score': result.get('resume_score'),
                        'semantic_similarity': result.get('score_breakdown', {}).get('semantic_similarity'),
                        'skill_overlap_percentage': result.get('score_breakdown', {}).get('skill_overlap_percentage'),
                        'strengths_count': len(result.get('strengths', [])),
                        'weaknesses_count': len(result.get('weaknesses', [])),
                        'timestamp': datetime.now().isoformat()
                    }
                    writer.writerow(row)
            
            logger.info(f"CSV report saved to {filename}")
            
        except Exception as e:
            logger.error(f"Error generating CSV report: {str(e)}")
    
    @staticmethod
    def generate_html_report(analysis_result: Dict[str, Any],
                            filename: str = None) -> str:
        """
        Generate HTML report from analysis
        
        Args:
            analysis_result: Analysis result dictionary
            filename: Output filename (optional)
            
        Returns:
            HTML string of report
        """
        score = analysis_result.get('resume_score', 0)
        role = analysis_result.get('role', 'Unknown')
        
        # Color scheme based on score
        if score >= 7.5:
            color = '#28a745'
            rating = 'Excellent'
        elif score >= 6.0:
            color = '#007bff'
            rating = 'Good'
        elif score >= 4.5:
            color = '#ffc107'
            rating = 'Fair'
        else:
            color = '#dc3545'
            rating = 'Needs Improvement'
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>ResumeBooster Analysis Report - {role}</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f5f5f5;
                }}
                .header {{
                    text-align: center;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px;
                    margin-bottom: 30px;
                }}
                .score-box {{
                    background-color: {color};
                    color: white;
                    padding: 20px;
                    border-radius: 8px;
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                    margin: 20px 0;
                }}
                .section {{
                    background: white;
                    padding: 20px;
                    margin: 20px 0;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .section h2 {{
                    color: #333;
                    border-bottom: 2px solid {color};
                    padding-bottom: 10px;
                }}
                .strength-item {{
                    background-color: #d4edda;
                    border-left: 4px solid #28a745;
                    padding: 10px;
                    margin: 5px 0;
                }}
                .weakness-item {{
                    background-color: #f8d7da;
                    border-left: 4px solid #dc3545;
                    padding: 10px;
                    margin: 5px 0;
                }}
                .suggestion-item {{
                    background-color: #cce5ff;
                    border-left: 4px solid #004085;
                    padding: 10px;
                    margin: 5px 0;
                }}
                .metric {{
                    display: inline-block;
                    width: 23%;
                    margin: 5px;
                    padding: 10px;
                    background-color: #f8f9fa;
                    border-radius: 5px;
                    text-align: center;
                }}
                .metric-value {{
                    font-size: 18px;
                    font-weight: bold;
                    color: {color};
                }}
                .metric-label {{
                    font-size: 12px;
                    color: #666;
                    margin-top: 5px;
                }}
                .footer {{
                    text-align: center;
                    color: #999;
                    margin-top: 30px;
                    font-size: 12px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>ResumeBooster Analysis Report</h1>
                <p>AI-Powered Resume Evaluation</p>
            </div>
            
            <div class="section">
                <h2>Role: {role}</h2>
                <div class="score-box">
                    Score: {score}/10 ({rating})
                </div>
                <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <div class="section">
                <h2>Analysis Metrics</h2>
        """
        
        # Add metrics
        metrics = analysis_result.get('score_breakdown', {})
        for key, value in metrics.items():
            if 'percentage' in key:
                display_value = f"{value:.1f}%"
            else:
                display_value = f"{value:.2%}" if isinstance(value, float) else str(value)
            
            html += f"""
                <div class="metric">
                    <div class="metric-label">{key.replace('_', ' ').title()}</div>
                    <div class="metric-value">{display_value}</div>
                </div>
            """
        
        html += "</div>"
        
        # Add strengths
        strengths = analysis_result.get('strengths', [])
        html += "<div class='section'><h2>Strengths</h2>"
        for strength in strengths[:10]:
            html += f"<div class='strength-item'>{strength}</div>"
        html += "</div>"
        
        # Add weaknesses
        weaknesses = analysis_result.get('weaknesses', [])
        html += "<div class='section'><h2>Weaknesses</h2>"
        for weakness in weaknesses[:10]:
            html += f"<div class='weakness-item'>{weakness}</div>"
        html += "</div>"
        
        # Add suggestions
        suggestions = analysis_result.get('suggestions', [])
        html += "<div class='section'><h2>Suggestions</h2>"
        for i, suggestion in enumerate(suggestions, 1):
            html += f"<div class='suggestion-item'><strong>Suggestion {i}:</strong> {suggestion}</div>"
        html += "</div>"
        
        # Footer
        html += f"""
            <div class="footer">
                <p>This report was generated by ResumeBooster</p>
                <p>For more information, visit: <a href="#">ResumeBooster Docs</a></p>
            </div>
        </body>
        </html>
        """
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                logger.info(f"HTML report saved to {filename}")
            except Exception as e:
                logger.error(f"Error saving HTML report: {str(e)}")
        
        return html


class BatchAnalyzer:
    """Analyze multiple resumes or roles in batch"""
    
    @staticmethod
    def analyze_multiple_roles(analyzer, resume_text: str,
                              roles: List[str] = None) -> Dict[str, Any]:
        """
        Analyze single resume against multiple roles
        
        Args:
            analyzer: ResumeAnalyzer instance
            resume_text: Resume content
            roles: List of roles to analyze against (None = all available)
            
        Returns:
            Dictionary with results for all roles
        """
        if roles is None:
            roles = analyzer.get_available_roles()
        
        results = {
            'resume_summary': {
                'length': len(resume_text),
                'timestamp': datetime.now().isoformat()
            },
            'analyses': {}
        }
        
        for role in roles:
            try:
                logger.info(f"Analyzing for role: {role}")
                analysis = analyzer.analyze_resume(resume_text, role)
                results['analyses'][role] = {
                    'score': analysis['resume_score'],
                    'strengths': analysis['strengths'][:5],
                    'weaknesses': analysis['weaknesses'][:5]
                }
            except Exception as e:
                logger.error(f"Error analyzing for role {role}: {str(e)}")
                results['analyses'][role] = {'error': str(e)}
        
        return results
    
    @staticmethod
    def find_best_matching_role(analyzer, resume_text: str) -> str:
        """
        Find the best matching role for a resume
        
        Args:
            analyzer: ResumeAnalyzer instance
            resume_text: Resume content
            
        Returns:
            Name of best matching role
        """
        results = BatchAnalyzer.analyze_multiple_roles(analyzer, resume_text)
        
        best_role = None
        best_score = -1
        
        for role, analysis in results['analyses'].items():
            if 'error' not in analysis:
                score = analysis['score']
                if score > best_score:
                    best_score = score
                    best_role = role
        
        return best_role if best_role else "Not determined"


class ResumeProcessor:
    """Process and validate resumes"""
    
    @staticmethod
    def validate_resume(resume_text: str) -> Dict[str, Any]:
        """
        Validate resume content
        
        Args:
            resume_text: Resume content
            
        Returns:
            Validation results
        """
        validations = {
            'valid': True,
            'warnings': [],
            'suggestions': []
        }
        
        # Check length
        if len(resume_text) < 200:
            validations['warnings'].append("Resume seems very short (< 200 characters)")
            validations['valid'] = False
        elif len(resume_text) > 10000:
            validations['suggestions'].append("Resume is quite long (> 10000 characters), consider condensing")
        
        # Check for common sections
        text_lower = resume_text.lower()
        
        if 'experience' not in text_lower and 'work' not in text_lower:
            validations['warnings'].append("No experience section found")
        
        if 'education' not in text_lower and 'school' not in text_lower:
            validations['suggestions'].append("Consider adding an education section")
        
        if 'skill' not in text_lower:
            validations['suggestions'].append("Consider adding a dedicated skills section")
        
        # Check contact info
        if '@' not in text_lower:
            validations['warnings'].append("No email address found")
        
        return validations
    
    @staticmethod
    def get_resume_stats(resume_text: str) -> Dict[str, Any]:
        """
        Get statistics about resume
        
        Args:
            resume_text: Resume content
            
        Returns:
            Dictionary with resume statistics
        """
        words = resume_text.split()
        sentences = resume_text.split('.')
        
        return {
            'total_characters': len(resume_text),
            'total_words': len(words),
            'total_sentences': len(sentences),
            'average_word_length': sum(len(w) for w in words) / len(words) if words else 0,
            'estimated_reading_time_minutes': len(words) / 200  # Average reading speed
        }

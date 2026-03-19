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
from io import BytesIO

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    logger_init = logging.getLogger(__name__)
    logger_init.warning("reportlab not installed. PDF export will be unavailable. Install with: pip install reportlab Pillow")

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
    
    @staticmethod
    def generate_pdf_report(analysis_result: Dict[str, Any], 
                           filename: str = None) -> bytes:
        """
        Generate PDF report from analysis result
        
        Args:
            analysis_result: Analysis result dictionary
            filename: Output filename (optional)
            
        Returns:
            PDF bytes
        """
        if not REPORTLAB_AVAILABLE:
            logger.error("reportlab is not installed. Install with: pip install reportlab Pillow")
            raise ImportError("reportlab is required for PDF export. Install with: pip install reportlab Pillow")
        
        try:
            # Create PDF buffer
            buffer = BytesIO()
            
            # Create PDF document
            doc = SimpleDocTemplate(
                buffer,
                pagesize=letter,
                rightMargin=0.75*inch,
                leftMargin=0.75*inch,
                topMargin=0.75*inch,
                bottomMargin=0.75*inch
            )
            
            # Container for PDF elements
            elements = []
            
            # Get styles
            styles = getSampleStyleSheet()
            
            # Custom styles
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#667eea'),
                spaceAfter=10,
                alignment=TA_CENTER,
                fontName='Helvetica-Bold'
            )
            
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                textColor=colors.HexColor('#764ba2'),
                spaceAfter=12,
                spaceBefore=12,
                fontName='Helvetica-Bold'
            )
            
            body_style = ParagraphStyle(
                'CustomBody',
                parent=styles['BodyText'],
                fontSize=11,
                alignment=TA_LEFT,
                spaceAfter=6
            )
            
            # Title
            elements.append(Paragraph("ResumeBooster Analysis Report", title_style))
            elements.append(Paragraph("AI-Powered Resume Evaluation", styles['Normal']))
            elements.append(Spacer(1, 0.2*inch))
            
            # Role and Score
            role = analysis_result.get('role', 'Unknown')
            score = analysis_result.get('resume_score', 0)
            
            # Color based on score
            if score >= 7.5:
                score_color = colors.HexColor('#28a745')
                rating = 'Excellent'
            elif score >= 6.0:
                score_color = colors.HexColor('#007bff')
                rating = 'Good'
            elif score >= 4.5:
                score_color = colors.HexColor('#ffc107')
                rating = 'Fair'
            else:
                score_color = colors.HexColor('#dc3545')
                rating = 'Needs Improvement'
            
            # Score table
            score_data = [
                ['Target Role', 'Resume Score', 'Rating', 'Generated At'],
                [role, f'{score}/10', rating, datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            ]
            
            score_table = Table(score_data, colWidths=[2*inch, 1.5*inch, 1.5*inch, 2*inch])
            score_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 11),
                ('ROWHEIGHT', (0, 0), (-1, -1), 30),
            ]))
            
            elements.append(score_table)
            elements.append(Spacer(1, 0.2*inch))
            
            # Score Metrics
            elements.append(Paragraph("Score Breakdown", heading_style))
            
            metrics = analysis_result.get('score_breakdown', {})
            metrics_data = [['Metric', 'Value']]
            
            for key, value in metrics.items():
                if 'percentage' in key:
                    display_value = f"{value:.1f}%"
                else:
                    display_value = f"{value:.2%}" if isinstance(value, float) else str(value)
                metrics_data.append([key.replace('_', ' ').title(), display_value])
            
            metrics_table = Table(metrics_data, colWidths=[3.5*inch, 2*inch])
            metrics_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 11),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0f0f0')),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
                ('ROWHEIGHT', (0, 0), (-1, -1), 25),
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                ('RIGHTPADDING', (0, 0), (-1, -1), 20),
            ]))
            
            elements.append(metrics_table)
            elements.append(Spacer(1, 0.2*inch))
            
            # Strengths
            elements.append(Paragraph("Strengths", heading_style))
            strengths = analysis_result.get('strengths', [])
            
            if strengths:
                strengths_table_data = [['✓ Strength']]
                for strength in strengths[:10]:
                    strengths_table_data.append([strength])
                
                strengths_table = Table(strengths_table_data, colWidths=[6.5*inch])
                strengths_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#28a745')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 11),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#e8f5e9')),
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#28a745')),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 10),
                    ('ROWHEIGHT', (0, 0), (-1, -1), 20),
                    ('LEFTPADDING', (0, 0), (-1, -1), 15),
                ]))
                elements.append(strengths_table)
            else:
                elements.append(Paragraph("No matching strengths found.", body_style))
            
            elements.append(Spacer(1, 0.15*inch))
            
            # Weaknesses
            elements.append(Paragraph("Areas for Improvement", heading_style))
            weaknesses = analysis_result.get('weaknesses', [])
            
            if weaknesses:
                weaknesses_table_data = [['⚠ To Develop']]
                for weakness in weaknesses[:10]:
                    weaknesses_table_data.append([weakness])
                
                weaknesses_table = Table(weaknesses_table_data, colWidths=[6.5*inch])
                weaknesses_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dc3545')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 11),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ffebee')),
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#dc3545')),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 10),
                    ('ROWHEIGHT', (0, 0), (-1, -1), 20),
                    ('LEFTPADDING', (0, 0), (-1, -1), 15),
                ]))
                elements.append(weaknesses_table)
            else:
                elements.append(Paragraph("No significant areas for improvement.", body_style))
            
            elements.append(Spacer(1, 0.15*inch))
            
            # Recommendations
            elements.append(Paragraph("Recommendations", heading_style))
            suggestions = analysis_result.get('suggestions', [])
            
            if suggestions:
                for i, suggestion in enumerate(suggestions[:5], 1):
                    suggestion_text = f"<b>{i}. </b>{suggestion}"
                    elements.append(Paragraph(suggestion_text, body_style))
            else:
                elements.append(Paragraph("Your resume is well-optimized!", body_style))
            
            elements.append(Spacer(1, 0.2*inch))
            
            # Learning Resources section if available
            learning_resources = analysis_result.get('learning_resources', {})
            if learning_resources:
                elements.append(PageBreak())
                elements.append(Paragraph("Personalized Learning Resources", heading_style))
                
                learning_path = analysis_result.get('learning_path', {})
                
                # Learning path overview
                learning_data = [
                    ['Skills to Learn', str(learning_path.get('total_skills_to_learn', 0))],
                    ['Estimated Hours', f"{learning_path.get('estimated_total_hours', 0)}+ hours"],
                    ['Target Role', learning_path.get('role', 'Unknown')]
                ]
                
                learning_table = Table(learning_data, colWidths=[3*inch, 3*inch])
                learning_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f0f8ff')),
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#667eea')),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                    ('ROWHEIGHT', (0, 0), (-1, -1), 25),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#667eea')),
                    ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
                ]))
                
                elements.append(learning_table)
                elements.append(Spacer(1, 0.15*inch))
                
                # Learning strategy
                elements.append(Paragraph("Learning Strategy", ParagraphStyle(
                    'SubHeading',
                    parent=styles['Heading3'],
                    fontSize=12,
                    textColor=colors.HexColor('#764ba2'),
                    spaceBefore=10,
                    spaceAfter=10,
                    fontName='Helvetica-Bold'
                )))
                
                for step in learning_path.get('learning_strategy', [])[:5]:
                    elements.append(Paragraph(f"• {step}", body_style))
                
                elements.append(Spacer(1, 0.15*inch))
                
                # Skills with resources
                elements.append(Paragraph("Recommended Resources by Skill", ParagraphStyle(
                    'SubHeading',
                    parent=styles['Heading3'],
                    fontSize=12,
                    textColor=colors.HexColor('#764ba2'),
                    spaceBefore=10,
                    spaceAfter=10,
                    fontName='Helvetica-Bold'
                )))
                
                skill_count = 0
                for skill, resources in list(learning_resources.items())[:5]:
                    skill_count += 1
                    elements.append(Paragraph(f"<u>{skill.title()}</u>", ParagraphStyle(
                        'SkillTitle',
                        parent=styles['Normal'],
                        fontSize=10,
                        textColor=colors.HexColor('#333333'),
                        spaceAfter=6,
                        fontName='Helvetica-Bold'
                    )))
                    
                    # Top course
                    courses = resources.get('courses', [])
                    if courses:
                        top_course = courses[0]
                        course_text = f"<b>Top Course:</b> {top_course.get('title', 'Unknown')}<br/>" \
                                     f"<b>Platform:</b> {top_course.get('platform', 'Unknown')} | " \
                                     f"<b>Duration:</b> {top_course.get('duration', 'N/A')} | " \
                                     f"<b>Level:</b> {top_course.get('level', 'N/A')}"
                        elements.append(Paragraph(course_text, ParagraphStyle(
                            'CourseText',
                            parent=styles['Normal'],
                            fontSize=9,
                            textColor=colors.HexColor('#555555'),
                            spaceAfter=6
                        )))
                    
                    elements.append(Spacer(1, 0.1*inch))
            
            elements.append(Spacer(1, 0.3*inch))
            
            # Footer
            footer_text = "This report was generated by ResumeBooster - AI-Powered Resume Analysis Engine<br/>" \
                         f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            elements.append(Paragraph(footer_text, ParagraphStyle(
                'Footer',
                parent=styles['Normal'],
                fontSize=9,
                textColor=colors.grey,
                alignment=TA_CENTER,
                spaceAfter=10
            )))
            
            # Build PDF
            doc.build(elements)
            
            # Get PDF bytes
            pdf_bytes = buffer.getvalue()
            buffer.close()
            
            # Save to file if filename provided
            if filename:
                try:
                    with open(filename, 'wb') as f:
                        f.write(pdf_bytes)
                    logger.info(f"PDF report saved to {filename}")
                except Exception as e:
                    logger.error(f"Error saving PDF report: {str(e)}")
            
            return pdf_bytes
            
        except Exception as e:
            logger.error(f"Error generating PDF report: {str(e)}")
            raise


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

"""
Example usage of ResumeBooster components
Demonstrates programmatic access and batch analysis capabilities
"""

from resume_analyzer import ResumeAnalyzer
from document_processor import DocumentProcessor
from utils import ReportGenerator, BatchAnalyzer, ResumeProcessor


def example_single_analysis():
    """Example 1: Analyze a single resume"""
    print("=" * 60)
    print("Example 1: Single Resume Analysis")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = ResumeAnalyzer("data")
    
    # Sample resume text (in practice, this comes from PDF extraction)
    sample_resume = """
    JOHN DOE
    Software Engineer | Python | Java | AWS
    
    EXPERIENCE
    Senior Software Engineer at Tech Corp (2020-2024)
    - Developed microservices using Python and Java
    - Implemented AWS cloud infrastructure
    - Led team of 5 engineers
    - Improved system performance by 40%
    
    SKILLS
    Technical: Python, Java, C++, SQL, AWS, Docker, Kubernetes, Git
    Soft Skills: Leadership, Communication, Problem Solving, Teamwork
    
    EDUCATION
    B.S. Computer Science, State University (2018)
    """
    
    # Analyze against specific role
    result = analyzer.analyze_resume(sample_resume, "ENGINEERING")
    
    print(f"\nRole: {result['role']}")
    print(f"Score: {result['resume_score']}/10")
    print(f"\nStrengths: {', '.join(result['strengths'][:5])}")
    print(f"Weaknesses: {', '.join(result['weaknesses'][:5])}")
    print(f"\nTop Suggestion: {result['suggestions'][0]}")


def example_multiple_roles():
    """Example 2: Analyze resume against multiple roles"""
    print("\n" + "=" * 60)
    print("Example 2: Multiple Role Analysis")
    print("=" * 60)
    
    analyzer = ResumeAnalyzer("data")
    
    sample_resume = """
    JANE SMITH
    Data Scientist | Python | Machine Learning | SQL | Statistics
    
    SKILLS
    Technical: Python, R, SQL, TensorFlow, PyTorch, Scikit-learn, Pandas
    Tools: Jupyter, Git, Docker, AWS, Tableau
    """
    
    # Analyze against multiple roles
    roles = analyzer.get_available_roles()[:5]  # First 5 roles
    results = BatchAnalyzer.analyze_multiple_roles(analyzer, sample_resume, roles)
    
    print("\nScores across different roles:")
    for role, analysis in results['analyses'].items():
        if 'error' not in analysis:
            print(f"  {role}: {analysis['score']:.1f}/10")


def example_find_best_role():
    """Example 3: Find the best matching role for a resume"""
    print("\n" + "=" * 60)
    print("Example 3: Find Best Matching Role")
    print("=" * 60)
    
    analyzer = ResumeAnalyzer("data")
    
    sample_resume = """
    ALEX JOHNSON
    Sales Manager | Business Development | Account Management
    
    EXPERIENCE
    Sales Director at Sales Corp (2018-2024)
    - Built and managed sales team of 15
    - Increased revenue by 200%
    - Managed key accounts with $5M+ revenue
    
    SKILLS
    Negotiation, Lead Generation, CRM, Customer Relationship Management,
    Presentation, Strategic Planning, Team Leadership
    """
    
    best_role = BatchAnalyzer.find_best_matching_role(analyzer, sample_resume)
    print(f"\nBest matching role: {best_role}")


def example_validate_resume():
    """Example 4: Validate resume content"""
    print("\n" + "=" * 60)
    print("Example 4: Resume Validation")
    print("=" * 60)
    
    resume_text = """
    JOHN DOE
    john@example.com
    
    EXPERIENCE
    Engineer at Company (2020-2024)
    
    SKILLS
    Python, Java, SQL
    """
    
    # Validate
    validation = ResumeProcessor.validate_resume(resume_text)
    stats = ResumeProcessor.get_resume_stats(resume_text)
    
    print(f"\nValidation Results:")
    print(f"  Valid: {validation['valid']}")
    if validation['warnings']:
        print(f"  Warnings: {', '.join(validation['warnings'])}")
    if validation['suggestions']:
        print(f"  Suggestions: {', '.join(validation['suggestions'])}")
    
    print(f"\nResume Statistics:")
    print(f"  Words: {stats['total_words']}")
    print(f"  Characters: {stats['total_characters']}")
    print(f"  Reading Time: {stats['estimated_reading_time_minutes']:.1f} minutes")


def example_generate_reports():
    """Example 5: Generate reports from analysis"""
    print("\n" + "=" * 60)
    print("Example 5: Report Generation")
    print("=" * 60)
    
    analyzer = ResumeAnalyzer("data")
    
    sample_resume = """
    PRODUCT MANAGER
    Product Management | Agile | Analytics | User Research
    
    SKILLS
    Agile, Scrum, User Research, Data Analysis, Strategic Planning
    """
    
    # Analyze
    result = analyzer.analyze_resume(sample_resume, "CONSULTANT")
    
    # Generate different report formats
    json_report = ReportGenerator.generate_json_report(result)
    print("\nJSON Report generated (first 200 chars):")
    print(json_report[:200] + "...")
    
    html_report = ReportGenerator.generate_html_report(result)
    print("\nHTML Report generated (first 200 chars):")
    print(html_report[:200] + "...")


def example_pdf_extraction():
    """Example 6: Extract text from PDF resume"""
    print("\n" + "=" * 60)
    print("Example 6: PDF Text Extraction")
    print("=" * 60)
    
    pdf_path = "sample_resume.pdf"  # Would be actual PDF file
    
    try:
        # Extract text (only works if sample_resume.pdf exists)
        text = DocumentProcessor.extract_text_from_pdf(pdf_path)
        
        if text:
            print(f"\nExtracted {len(text)} characters from PDF")
            print(f"First 200 characters:\n{text[:200]}")
        else:
            print(f"\nNo text extracted or file not found: {pdf_path}")
            
    except Exception as e:
        print(f"\nNote: PDF file not found - this is expected")
        print(f"In production, use: DocumentProcessor.extract_text_from_pdf(pdf_path)")


def example_available_roles():
    """Example 7: List available roles"""
    print("\n" + "=" * 60)
    print("Example 7: Available Roles")
    print("=" * 60)
    
    analyzer = ResumeAnalyzer("data")
    roles = analyzer.get_available_roles()
    
    print(f"\nTotal roles available: {len(roles)}")
    print("\nRoles:")
    for i, role in enumerate(roles[:10], 1):
        print(f"  {i}. {role}")
    
    if len(roles) > 10:
        print(f"  ... and {len(roles) - 10} more")


def main():
    """Run all examples"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " ResumeBooster - Example Usage ".center(58) + "║")
    print("╚" + "=" * 58 + "╝")
    
    try:
        # Run examples
        example_single_analysis()
        example_multiple_roles()
        example_find_best_role()
        example_validate_resume()
        example_generate_reports()
        example_pdf_extraction()
        example_available_roles()
        
        print("\n" + "=" * 60)
        print("All examples completed successfully!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\nError running examples: {str(e)}")
        print("\nMake sure:")
        print("  1. Dependencies are installed: pip install -r requirements.txt")
        print("  2. data/ directory exists with resume samples")
        print("  3. BERT model is downloaded")


if __name__ == "__main__":
    main()

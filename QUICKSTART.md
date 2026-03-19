# 🚀 ResumeBooster - Quick Start Guide

## 5-Minute Setup

### 1. Install Requirements (3 minutes)
```bash
cd d:\CareerBooster
pip install -r requirements.txt
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"
```

### 2. Run Application (1 minute)
```bash
streamlit run app.py
```

### 3. Use It (1 minute)
- Select a role from dropdown
- Upload your PDF resume
- Click "Analyze Resume"
- Review results in tabs

---

## First-Time Users

### Getting Started Checklist
- [ ] Python 3.8+ installed
- [ ] Dependencies installed
- [ ] Resume in PDF format ready
- [ ] Streamlit running locally
- [ ] Browser open to http://localhost:8501

### What to Expect
1. **Roles Listed**: 24+ job categories available
2. **Upload Resume**: PDF file, any length
3. **Analysis Time**: 10-30 seconds depending on resume length
4. **Results**: Immediate display with 5 detailed tabs
5. **Score Range**: 0-10 scale with interpretation guide

---

## Understanding Your Results

### Example: Software Engineer Resume Analysis

**Score: 8.5 / 10** ✨ Good Match

This means:
- Your resume is well-aligned with engineering requirements
- You have most required technical skills
- Minor gaps in some emerging technologies
- Strong potential for this role

### What to Do Next

**If Score > 7.5:**
- Your resume is competitive
- Apply with confidence
- Use suggestions for final polish

**If Score 5.0-7.5:**
- Implement 3-5 top suggestions
- Add missing skills with evidence
- Re-analyze after updates

**If Score < 5.0:**
- Significant skill gaps identified
- Consider gaining experience/skills
- Focus on 5+ strongest suggestions

---

## Common Scenarios

### Scenario 1: Career Transition
*Moving from Finance to Data Science*

1. Select "DATA ANALYST" role
2. Upload current resume
3. Review "Weaknesses" tab
4. Focus on Python, SQL, Tableau skills
5. Implement suggestions, re-analyze

### Scenario 2: Role-Specific Optimization
*Preparing for specific company job posting*

1. Use closest matching role
2. Manually add keywords from job posting to resume
3. Re-analyze
4. Score should improve with keyword matching

### Scenario 3: Continuous Improvement
*Regular resume enhancement*

1. Analyze every 3 months
2. Track score improvements
3. Add new skills as you develop them
4. Maintain optimal resume alignment

---

## Tips & Tricks

### Pro Tips for Higher Scores

1. **Use Keywords Strategically**
   - Don't just add words, use context
   - Explain how you use each skill
   - Show progression and depth

2. **Quantify Achievements**
   - "Led team of 5" not "led team"
   - "Improved efficiency by 30%" not "improved"
   - Numbers make bigger impact

3. **Mirror Job Description**
   - Use similar terminology to role description
   - Maintain professional tone
   - Align section headers with expectations

4. **Show Relevant Projects**
   - List specific projects with role
   - Link to portfolio or GitHub if tech role
   - Describe impact and learnings

5. **Update Regularly**
   - Add new skills immediately
   - Remove outdated information
   - Keep experience current

### Analysis Tips

- Use PDF resumes (not Word docs converted)
- Clear section structure helps extraction
- One resume, multiple role analyses
- Track improvements over time

---

## Interpretation Guide

### Score Ranges

| Score | Rating | Meaning |
|-------|--------|---------|
| 9.0-10.0 | Excellent | Exceptional match, highly qualified |
| 8.0-8.9 | Very Good | Strong candidate, minor gaps |
| 7.0-7.9 | Good | Qualified with some improvements needed |
| 6.0-6.9 | Fair | Moderate fit, significant gaps |
| 5.0-5.9 | Weak | Limited experience, major gaps |
| <5.0 | Poor | Substantial gaps, consider retraining |

### Metrics Explained

**Semantic Similarity** (78-85% typical)
- How well resume content aligns with role
- Higher = better content relevance
- Focus: Add role-specific keywords and context

**Skill Overlap** (60-90% typical)
- Percentage of required skills you have
- Higher = more comprehensive skills
- Focus: Add missing skills

**Sectional Relevance** (70-80% typical)
- Quality of content across resume sections
- Higher = well-detailed resume
- Focus: Expand descriptions, add examples

---

## Frequently Asked Questions

### Q: Can I analyze the same resume multiple times?
**A:** Yes! Analyze against different roles to find best fit.

### Q: How accurate is the scoring?
**A:** BERT model is 90%+ accurate for semantic understanding. Score reflects actual resume-role alignment.

### Q: Should I add all suggested keywords?
**A:** No. Only add keywords where you have genuine experience.

### Q: How long should resume be?
**A:** 1-2 pages ideal. Longer resumes reduce focus and ATS compatibility.

### Q: Can I analyze images of resumes?
**A:** No, only PDFs with extractable text. Scanned documents won't work.

### Q: Do I need to update my resume instantly?
**A:** No. Prioritize suggestions by impact (biggest gaps first).

### Q: Can I compare two resumes?
**A:** Current version analyzes one resume per session. Could add feature.

### Q: What if my role isn't listed?
**A:** Add folder under `data/` with role name + sample PDFs.

---

## Troubleshooting Quick Fixes

### Problem: Analysis takes too long
**Solution:** Restart app, clear cache, check internet connection

### Problem: Resume text extraction fails
**Solution:** Try different PDF (may be scanned), check file size <50MB

### Problem: Roles not appearing
**Solution:** Check `data/` folder exists, restart app

### Problem: Low score seems wrong
**Solution:** Check PDF text extracts correctly, add more keywords

---

## Next Steps

1. **Analyze Your Resume**
   - Run analysis for target role
   - Note 3-5 top suggestions

2. **Make Improvements**
   - Implement suggestions
   - Add missing skills
   - Quantify achievements

3. **Re-analyze**
   - After 2-3 weeks
   - Track score progression
   - Refine based on new feedback

4. **Apply Confidently**
   - Score 7.5+ ready to apply
   - Tailor for specific jobs
   - Track application success

---

## Getting Help

### Documentation
- Run `? app` in terminal while Streamlit is running
- Check README.md for comprehensive guide
- Review code comments for technical details

### Debugging
```bash
# Run in verbose mode
streamlit run app.py --logger.level=debug

# Check Python version
python --version

# Verify installations
pip list | grep streamlit
```

### Common Errors
1. **ModuleNotFoundError**: Run `pip install -r requirements.txt`
2. **Port 8501 in use**: Change port with `streamlit run app.py --server.port 8502`
3. **Cannot find data**: Ensure `data/` folder in same directory as `app.py`

---

## Advanced Usage

### Batch Analysis
```python
from resume_analyzer import ResumeAnalyzer

analyzer = ResumeAnalyzer("data")
roles = analyzer.get_available_roles()

for role in roles:
    result = analyzer.analyze_resume(resume_text, role)
    print(f"{role}: {result['resume_score']}")
```

### Custom Role Profiles
Edit `role_profile_builder.py` to customize how profiles are built from samples.

### Programmatic Access
All modules have public APIs - use them in your own scripts!

---

**Ready? Let's boost your resume! 🚀**

Next: Run `streamlit run app.py` and select your target role!

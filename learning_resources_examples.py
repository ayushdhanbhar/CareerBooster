"""
Learning Resources Feature Examples
Demonstrates how to use the personalized learning resource recommendations
"""

from learning_resources_recommender import LearningResourcesRecommender


def example_1_simple_recommendations():
    """
    Example 1: Get learning resources for a single missing skill
    """
    print("=" * 80)
    print("EXAMPLE 1: Get Learning Resources for Missing Skills")
    print("=" * 80)
    
    # Identify missing skills
    missing_skills = ['python', 'docker']
    
    # Get recommendations
    recommendations = LearningResourcesRecommender.get_recommendations(
        missing_skills, 
        num_resources=2
    )
    
    # Display results
    for skill, resources in recommendations.items():
        print(f"\n📚 {skill.upper()}")
        print("-" * 40)
        
        # Show courses
        print("Online Courses:")
        for course in resources['courses']:
            print(f"  ✓ {course['title']}")
            print(f"    Platform: {course['platform']}")
            print(f"    Duration: {course['duration']}")
            print(f"    Level: {course['level']}")
            print(f"    Rating: ⭐ {course ['rating']}")
        
        # Show YouTube tutorials
        print("\nYouTube Tutorials:")
        for tutorial in resources['youtube_tutorials']:
            print(f"  ✓ {tutorial['title']}")
            print(f"    Channel: {tutorial['channel']}")
            print(f"    Level: {tutorial['level']}")


def example_2_personalized_learning_path():
    """
    Example 2: Create a personalized learning path for a specific role
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Personalized Learning Path")
    print("=" * 80)
    
    missing_skills = [
        'python', 'docker', 'kubernetes', 'aws',
        'machine learning', 'problem solving', 'communication'
    ]
    role = 'DATA ENGINEER'
    
    # Create learning path
    learning_path = LearningResourcesRecommender.create_personalized_learning_path(
        missing_skills,
        role
    )
    
    # Display path overview
    print(f"\n📍 Target Role: {learning_path['role']}")
    print(f"📚 Skills to Learn: {learning_path['total_skills_to_learn']}")
    print(f"⏱️  Estimated Time: {learning_path['estimated_total_hours']}+ hours")
    
    # Display strategy
    print(f"\n🎯 Recommended Learning Strategy:")
    for step in learning_path['learning_strategy']:
        print(f"   {step}")


def example_3_skill_difficulty_assessment():
    """
    Example 3: Assess difficulty levels of skills
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Skill Difficulty Assessment")
    print("=" * 80)
    
    skills_to_assess = [
        'python',
        'communication',
        'machine learning',
        'kubernetes',
        'sql',
        'leadership'
    ]
    
    print("\nSkill Difficulty Levels:")
    print("-" * 40)
    
    for skill in skills_to_assess:
        level = LearningResourcesRecommender.get_skill_difficulty_level(skill)
        print(f"  • {skill.title():25} → {level}")


def example_4_multiple_skills_detailed():
    """
    Example 4: Get detailed recommendations for multiple skills
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 4: Detailed Recommendations for Multiple Skills")
    print("=" * 80)
    
    missing_skills = ['javascript', 'react', 'performance solving']
    
    recommendations = LearningResourcesRecommender.get_recommendations(
        missing_skills,
        num_resources=3
    )
    
    for skill, resources in recommendations.items():
        print(f"\n{'=' * 60}")
        print(f"SKILL: {skill.upper()}")
        print(f"{'=' * 60}")
        
        # Matched skill
        if resources['matched_skill'] != 'generic':
            print(f"Matched to: {resources['matched_skill']}")
        else:
            print("Generic recommendations for this skill")
        
        # Top course
        if resources['courses']:
            top_course = resources['courses'][0]
            print(f"\n🏆 TOP COURSE RECOMMENDATION:")
            print(f"   Title: {top_course['title']}")
            print(f"   Platform: {top_course['platform']}")
            print(f"   Duration: {top_course['duration']}")
            print(f"   Level: {top_course['level']}")
            print(f"   Rating: {top_course['rating']} stars")
            if 'url' in top_course:
                print(f"   Link: {top_course['url']}")
        
        # Top YouTube tutorial
        if resources['youtube_tutorials']:
            top_tutorial = resources['youtube_tutorials'][0]
            print(f"\n🎬 TOP YOUTUBE TUTORIAL:")
            print(f"   Title: {top_tutorial['title']}")
            print(f"   Channel: {top_tutorial['channel']}")
            print(f"   Duration: {top_tutorial['duration']}")
            print(f"   Level: {top_tutorial['level']}")


def example_5_role_specific_learning():
    """
    Example 5: Get specific learning recommendations for a role
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 5: Role-Specific Learning Recommendations")
    print("=" * 80)
    
    # Role: Software Engineer
    engineer_skills = [
        'python', 'java', 'system design',
        'docker', 'kubernetes', 'leadership'
    ]
    
    # Role: Data Scientist
    data_scientist_skills = [
        'python', 'machine learning', 'tensorflow',
        'data analysis', 'tableau', 'communication'
    ]
    
    # Role: Cloud Architect
    cloud_architect_skills = [
        'aws', 'kubernetes', 'docker',
        'terraform', 'problem solving', 'leadership'
    ]
    
    roles_data = [
        ('Software Engineer', engineer_skills),
        ('Data Scientist', data_scientist_skills),
        ('Cloud Architect', cloud_architect_skills)
    ]
    
    for role, skills in roles_data:
        print(f"\n{'=' * 60}")
        print(f"ROLE: {role.upper()}")
        print(f"{'=' * 60}")
        
        path = LearningResourcesRecommender.create_personalized_learning_path(
            skills, role
        )
        
        print(f"Target Role: {path['role']}")
        print(f"Total Skills: {path['total_skills_to_learn']}")
        print(f"Est. Hours: {path['estimated_total_hours']}+")
        
        print("\nTop 3 Learning Steps:")
        for step in path['learning_strategy'][:3]:
            print(f"  • {step}")


def example_6_learning_resources_export():
    """
    Example 6: Export learning resources as structured data
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 6: Export Learning Resources")
    print("=" * 80)
    
    missing_skills = ['python', 'docker']
    recommendations = LearningResourcesRecommender.get_recommendations(missing_skills)
    
    # Export as structured text
    print("\nEXPORTED LEARNING PLAN:")
    print("=" * 60)
    
    for skill, resources in recommendations.items():
        print(f"\n{skill.upper()}")
        print("-" * 30)
        
        print("COURSES TO TAKE:")
        for i, course in enumerate(resources['courses'], 1):
            print(f"  {i}. {course['title']}")
            print(f"     Duration: {course['duration']}")
            print(f"     Platform: {course['platform']}")
        
        print("\nTUTORIALS TO WATCH:")
        for i, tutorial in enumerate(resources['youtube_tutorials'], 1):
            print(f"  {i}. {tutorial['title']} ({tutorial['channel']})")
        
        print()


def example_7_comprehensive_analysis():
    """
    Example 7: Comprehensive learning analysis for career transition
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 7: Comprehensive Career Transition Learning Plan")
    print("=" * 80)
    
    print("\nSCENARIO: Transitioning from Frontend to Full-Stack Developer")
    print("-" * 60)
    
    # Skills to acquire
    missing_skills = [
        'backend development',
        'python',
        'django',
        'sql',
        'restapi',
        'devops',
        'docker',
        'git',
        'problem solving'
    ]
    
    target_role = 'FULL-STACK ENGINEER'
    
    # Generate personalized learning path
    learning_path = LearningResourcesRecommender.create_personalized_learning_path(
        missing_skills,
        target_role
    )
    
    # Display comprehensive plan
    print(f"\n📋 CAREER TRANSITION PLAN")
    print(f"Current Skills: Frontend Development (HTML, CSS, JavaScript, React)")
    print(f"Target Role: {learning_path['role']}")
    print(f"Total Skills Gap: {learning_path['total_skills_to_learn']}")
    print(f"Estimated Learning Time: {learning_path['estimated_total_hours']}+ hours")
    print(f"Estimated Timeline: {learning_path['estimated_total_hours'] // (5 * 7)} weeks (5 hrs/week)")
    
    print(f"\n🎯 LEARNING STRATEGY")
    for i, strategy in enumerate(learning_path['learning_strategy'], 1):
        print(f"  {strategy}")
    
    print(f"\n📚 SKILLS TO DEVELOP")
    recommendations = LearningResourcesRecommender.get_recommendations(missing_skills)
    for skill in recommendations.keys():
        difficulty = LearningResourcesRecommender.get_skill_difficulty_level(skill)
        print(f"  • {skill.title():25} ({difficulty})")


def run_all_examples():
    """Run all examples"""
    print("\n" + "🎓" * 40)
    print("LEARNING RESOURCES RECOMMENDER - EXAMPLES")
    print("🎓" * 40)
    
    example_1_simple_recommendations()
    example_2_personalized_learning_path()
    example_3_skill_difficulty_assessment()
    example_4_multiple_skills_detailed()
    example_5_role_specific_learning()
    example_6_learning_resources_export()
    example_7_comprehensive_analysis()
    
    print("\n" + "=" * 80)
    print("ALL EXAMPLES COMPLETED")
    print("=" * 80)


if __name__ == '__main__':
    # Run a specific example or all examples
    import sys
    
    if len(sys.argv) > 1:
        example_num = sys.argv[1]
        if example_num == '1':
            example_1_simple_recommendations()
        elif example_num == '2':
            example_2_personalized_learning_path()
        elif example_num == '3':
            example_3_skill_difficulty_assessment()
        elif example_num == '4':
            example_4_multiple_skills_detailed()
        elif example_num == '5':
            example_5_role_specific_learning()
        elif example_num == '6':
            example_6_learning_resources_export()
        elif example_num == '7':
            example_7_comprehensive_analysis()
        else:
            run_all_examples()
    else:
        run_all_examples()

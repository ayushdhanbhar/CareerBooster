"""
Learning Resources Recommender Module
Suggests online courses and YouTube tutorials for identified skill gaps
"""

from typing import Dict, List, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LearningResourcesRecommender:
    """Generate personalized learning resource recommendations for skill gaps"""
    
    # Comprehensive learning resources database
    LEARNING_RESOURCES = {
        # Programming Languages
        'python': {
            'courses': [
                {
                    'title': 'Python for Everybody',
                    'platform': 'Coursera',
                    'duration': '8 weeks',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/specializations/python',
                    'rating': 4.7
                },
                {
                    'title': 'Complete Python Bootcamp',
                    'platform': 'Udemy',
                    'duration': '22 hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/complete-python-bootcamp/',
                    'rating': 4.6
                },
                {
                    'title': 'Python Programming Masterclass',
                    'platform': 'Udemy',
                    'duration': '40+ hours',
                    'level': 'Beginner to Advanced',
                    'url': 'https://www.udemy.com/course/python-the-complete-python-developer-course/',
                    'rating': 4.5
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Python Tutorial for Beginners',
                    'channel': 'Corey Schafer',
                    'duration': 'Series (8+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Python Programming Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (4+ hours)',
                    'level': 'Beginner to Intermediate'
                },
                {
                    'title': 'Advanced Python Programming',
                    'channel': 'Tech With Tim',
                    'duration': 'Series (3+ hours)',
                    'level': 'Intermediate to Advanced'
                }
            ]
        },
        'java': {
            'courses': [
                {
                    'title': 'Java Programming MOOC',
                    'platform': 'Coursera',
                    'duration': '6-7 months',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/java-programming',
                    'rating': 4.6
                },
                {
                    'title': 'The Complete Java Development Bootcamp',
                    'platform': 'Udemy',
                    'duration': '35+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/the-complete-java-development-bootcamp/',
                    'rating': 4.5
                },
                {
                    'title': 'Java for Beginners',
                    'platform': 'Udemy',
                    'duration': '13 hours',
                    'level': 'Beginner',
                    'url': 'https://www.udemy.com/course/java-programming-basics/',
                    'rating': 4.4
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Java Tutorial for Beginners',
                    'channel': 'Programming with Mosh',
                    'duration': 'Series (10+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Java Full Course',
                    'channel': 'Telusko',
                    'duration': 'Series (12+ hours)',
                    'level': 'Beginner to Intermediate'
                }
            ]
        },
        'javascript': {
            'courses': [
                {
                    'title': 'The Complete JavaScript Course',
                    'platform': 'Udemy',
                    'duration': '69+ hours',
                    'level': 'Beginner to Advanced',
                    'url': 'https://www.udemy.com/course/the-complete-javascript-course-2/',
                    'rating': 4.6
                },
                {
                    'title': 'JavaScript Basics',
                    'platform': 'Coursera',
                    'duration': '4 weeks',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/javascript-basics',
                    'rating': 4.5
                },
                {
                    'title': 'Modern JavaScript From The Beginning',
                    'platform': 'Udemy',
                    'duration': '40+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/modern-javascript-from-the-beginning/',
                    'rating': 4.7
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'JavaScript Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (3+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'JavaScript Complete Course',
                    'channel': 'freeCodeCamp',
                    'duration': '20+ hours',
                    'level': 'Beginner to Advanced'
                }
            ]
        },
        'react': {
            'courses': [
                {
                    'title': 'React - The Complete Guide',
                    'platform': 'Udemy',
                    'duration': '48+ hours',
                    'level': 'Beginner to Advanced',
                    'url': 'https://www.udemy.com/course/react-the-complete-guide-incl-redux/',
                    'rating': 4.5
                },
                {
                    'title': 'React for Beginners',
                    'platform': 'Coursera',
                    'duration': '4 weeks',
                    'level': 'Intermediate',
                    'url': 'https://www.coursera.org/learn/react',
                    'rating': 4.4
                },
                {
                    'title': 'React 18 for Beginners',
                    'platform': 'Udemy',
                    'duration': '17+ hours',
                    'level': 'Beginner',
                    'url': 'https://www.udemy.com/course/react-for-beginners/',
                    'rating': 4.6
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'React Tutorial for Beginners',
                    'channel': 'Traversy Media',
                    'duration': 'Series (3+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'React Full Course',
                    'channel': 'freeCodeCamp',
                    'duration': '10+ hours',
                    'level': 'Beginner to Intermediate'
                }
            ]
        },
        'sql': {
            'courses': [
                {
                    'title': 'SQL for Data Analysis',
                    'platform': 'Coursera',
                    'duration': '4-6 weeks',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/sql-for-data-analysis',
                    'rating': 4.6
                },
                {
                    'title': 'The Complete SQL Bootcamp',
                    'platform': 'Udemy',
                    'duration': '13+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/the-complete-sql-bootcamp/',
                    'rating': 4.6
                },
                {
                    'title': 'Advanced SQL',
                    'platform': 'Udemy',
                    'duration': '14+ hours',
                    'level': 'Intermediate to Advanced',
                    'url': 'https://www.udemy.com/course/advanced-sql-for-professional-programmers/',
                    'rating': 4.5
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'SQL Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (3+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'SQL Full Course',
                    'channel': 'freeCodeCamp',
                    'duration': '4 hours',
                    'level': 'Beginner to Intermediate'
                }
            ]
        },
        'docker': {
            'courses': [
                {
                    'title': 'Docker for the Absolute Beginner',
                    'platform': 'Udemy',
                    'duration': '5+ hours',
                    'level': 'Beginner',
                    'url': 'https://www.udemy.com/course/docker-for-the-absolute-beginner-hands-on/',
                    'rating': 4.5
                },
                {
                    'title': 'Docker Mastery',
                    'platform': 'Udemy',
                    'duration': '22+ hours',
                    'level': 'Beginner to Advanced',
                    'url': 'https://www.udemy.com/course/docker-mastery/',
                    'rating': 4.6
                },
                {
                    'title': 'Containers & Kubernetes Essentials',
                    'platform': 'Coursera',
                    'duration': '3-4 months',
                    'level': 'Intermediate',
                    'url': 'https://www.coursera.org/learn/containers-kubernetes-essentials',
                    'rating': 4.4
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Docker Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (2+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Docker Basics',
                    'channel': 'freeCodeCamp',
                    'duration': '3+ hours',
                    'level': 'Beginner'
                }
            ]
        },
        'kubernetes': {
            'courses': [
                {
                    'title': 'Kubernetes for the Absolute Beginner',
                    'platform': 'Udemy',
                    'duration': '4+ hours',
                    'level': 'Beginner',
                    'url': 'https://www.udemy.com/course/learn-kubernetes/',
                    'rating': 4.5
                },
                {
                    'title': 'Certified Kubernetes Administrator (CKA)',
                    'platform': 'Udemy',
                    'duration': '20+ hours',
                    'level': 'Intermediate to Advanced',
                    'url': 'https://www.udemy.com/course/certified-kubernetes-administrator-cka/',
                    'rating': 4.6
                },
                {
                    'title': 'Containers & Kubernetes Essentials',
                    'platform': 'Coursera',
                    'duration': '3-4 months',
                    'level': 'Intermediate',
                    'url': 'https://www.coursera.org/learn/containers-kubernetes-essentials',
                    'rating': 4.4
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Kubernetes Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (2+ hours)',
                    'level': 'Intermediate'
                },
                {
                    'title': 'Kubernetes Complete Tutorial',
                    'channel': 'TechWorld with Nana',
                    'duration': 'Series (3+ hours)',
                    'level': 'Beginner to Intermediate'
                }
            ]
        },
        'aws': {
            'courses': [
                {
                    'title': 'AWS Certified Cloud Practitioner Training',
                    'platform': 'Udemy',
                    'duration': '22+ hours',
                    'level': 'Beginner',
                    'url': 'https://www.udemy.com/course/aws-certified-cloud-practitioner-new/',
                    'rating': 4.6
                },
                {
                    'title': 'AWS in 7 Days',
                    'platform': 'Coursera',
                    'duration': '1 week',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/aws-cloud-basics',
                    'rating': 4.3
                },
                {
                    'title': 'AWS Solutions Architect Associate Certification',
                    'platform': 'Udemy',
                    'duration': '28+ hours',
                    'level': 'Intermediate to Advanced',
                    'url': 'https://www.udemy.com/course/aws-solutions-architect-associate-saa-c03/',
                    'rating': 4.6
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'AWS Tutorial',
                    'channel': 'A Cloud Guru',
                    'duration': 'Series (4+ hours)',
                    'level': 'Beginner to Intermediate'
                },
                {
                    'title': 'AWS Certified Cloud Practitioner',
                    'channel': 'freeCodeCamp',
                    'duration': '10+ hours',
                    'level': 'Beginner'
                }
            ]
        },
        'machine learning': {
            'courses': [
                {
                    'title': 'Machine Learning A-Z',
                    'platform': 'Udemy',
                    'duration': '44+ hours',
                    'level': 'Beginner to Advanced',
                    'url': 'https://www.udemy.com/course/machinelearning/',
                    'rating': 4.5
                },
                {
                    'title': 'Machine Learning by Andrew Ng',
                    'platform': 'Coursera',
                    'duration': '4 weeks',
                    'level': 'Intermediate',
                    'url': 'https://www.coursera.org/learn/machine-learning',
                    'rating': 4.9
                },
                {
                    'title': 'Deep Learning Specialization',
                    'platform': 'Coursera',
                    'duration': '3-5 months',
                    'level': 'Advanced',
                    'url': 'https://www.coursera.org/specializations/deep-learning',
                    'rating': 4.8
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Machine Learning Tutorial',
                    'channel': 'Sentdex',
                    'duration': 'Series (6+ hours)',
                    'level': 'Beginner to Intermediate'
                },
                {
                    'title': '3Blue1Brown - Neural Networks',
                    'channel': '3Blue1Brown',
                    'duration': 'Series (4 videos)',
                    'level': 'Intermediate'
                }
            ]
        },
        'tensorflow': {
            'courses': [
                {
                    'title': 'TensorFlow for Beginners',
                    'platform': 'Coursera',
                    'duration': '4-7 weeks',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/introduction-tensorflow',
                    'rating': 4.6
                },
                {
                    'title': 'Complete TensorFlow 2 and Keras Deep Learning Bootcamp',
                    'platform': 'Udemy',
                    'duration': '22+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/complete-tensorflow-2-and-keras-deep-learning-bootcamp/',
                    'rating': 4.5
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'TensorFlow Tutorial',
                    'channel': 'Sentdex',
                    'duration': 'Series (5+ hours)',
                    'level': 'Beginner to Intermediate'
                },
                {
                    'title': 'TensorFlow Basics',
                    'channel': 'TensorFlow',
                    'duration': 'Official Series',
                    'level': 'Beginner'
                }
            ]
        },
        'data analysis': {
            'courses': [
                {
                    'title': 'Data Analysis with Python',
                    'platform': 'Coursera',
                    'duration': '3 months',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/data-analysis-with-python',
                    'rating': 4.6
                },
                {
                    'title': 'Data Analysis Bootcamp',
                    'platform': 'Udemy',
                    'duration': '22+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/the-data-analysis-bootcamp/',
                    'rating': 4.5
                },
                {
                    'title': 'Advanced Excel for Data Analytics',
                    'platform': 'Udemy',
                    'duration': '7+ hours',
                    'level': 'Intermediate',
                    'url': 'https://www.udemy.com/course/advanced-excel-for-data-analytics/',
                    'rating': 4.6
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Data Analysis with Pandas',
                    'channel': 'Corey Schafer',
                    'duration': 'Series (3+ hours)',
                    'level': 'Beginner to Intermediate'
                },
                {
                    'title': 'Data Analysis Full Course',
                    'channel': 'freeCodeCamp',
                    'duration': '3+ hours',
                    'level': 'Beginner'
                }
            ]
        },
        'tableau': {
            'courses': [
                {
                    'title': 'Tableau 2023 A-Z: Hands-On Tableau Training',
                    'platform': 'Udemy',
                    'duration': '13+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/tableau10/',
                    'rating': 4.5
                },
                {
                    'title': 'Getting Started with Tableau',
                    'platform': 'Coursera',
                    'duration': '3 weeks',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/tableau',
                    'rating': 4.4
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Tableau Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (2+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Tableau Full Training',
                    'channel': 'Edureka',
                    'duration': '3+ hours',
                    'level': 'Beginner to Intermediate'
                }
            ]
        },
        'communication': {
            'courses': [
                {
                    'title': 'Powerful Communication',
                    'platform': 'Coursera',
                    'duration': '4 weeks',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/powerful-communication',
                    'rating': 4.7
                },
                {
                    'title': 'Effective Communication for Better Management',
                    'platform': 'Udemy',
                    'duration': '5+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/effective-communication-skills/',
                    'rating': 4.5
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Communication Skills',
                    'channel': 'Skill Success',
                    'duration': 'Series (2+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Effective Communication',
                    'channel': 'Psychology & Self Improvement',
                    'duration': 'Series (1+ hours)',
                    'level': 'Beginner'
                }
            ]
        },
        'leadership': {
            'courses': [
                {
                    'title': 'Leadership Foundations',
                    'platform': 'Coursera',
                    'duration': '3-4 months',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/leadership-foundations',
                    'rating': 4.6
                },
                {
                    'title': 'Complete Leadership Masterclass',
                    'platform': 'Udemy',
                    'duration': '10+ hours',
                    'level': 'Beginner to Advanced',
                    'url': 'https://www.udemy.com/course/leadership-masterclass/',
                    'rating': 4.6
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Leadership Skills',
                    'channel': 'Brian Tracy',
                    'duration': 'Series (2+ hours)',
                    'level': 'Beginner to Intermediate'
                },
                {
                    'title': 'Effective Leadership',
                    'channel': 'Simon Sinek',
                    'duration': 'Series (2+ hours)',
                    'level': 'Intermediate'
                }
            ]
        },
        'project management': {
            'courses': [
                {
                    'title': 'Project Management Fundamentals',
                    'platform': 'Coursera',
                    'duration': '3 weeks',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/project-management-foundations',
                    'rating': 4.5
                },
                {
                    'title': 'CompTIA Project+ (PK0-005)',
                    'platform': 'Udemy',
                    'duration': '12+ hours',
                    'level': 'Intermediate',
                    'url': 'https://www.udemy.com/course/comptia-project-plus/',
                    'rating': 4.6
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Project Management Basics',
                    'channel': 'Edu4Sure',
                    'duration': 'Series (3+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Project Management Tutorial',
                    'channel': 'edpresso',
                    'duration': 'Series (2+ hours)',
                    'level': 'Beginner to Intermediate'
                }
            ]
        },
        'excel': {
            'courses': [
                {
                    'title': 'Microsoft Excel - Data Analysis & Business Modeling',
                    'platform': 'Udemy',
                    'duration': '17+ hours',
                    'level': 'Beginner to Advanced',
                    'url': 'https://www.udemy.com/course/microsoft-excel-data-analysis-business-modeling/',
                    'rating': 4.5
                },
                {
                    'title': 'Excel Skills for Business',
                    'platform': 'Coursera',
                    'duration': '4 weeks',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/excel-analysis',
                    'rating': 4.5
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Excel Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (2+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Excel Full Course',
                    'channel': 'Edureka',
                    'duration': '3+ hours',
                    'level': 'Beginner to Intermediate'
                }
            ]
        },
        'git': {
            'courses': [
                {
                    'title': 'Git & GitHub Crash Course',
                    'platform': 'Udemy',
                    'duration': '1.5+ hours',
                    'level': 'Beginner',
                    'url': 'https://www.udemy.com/course/git-and-github-crash-course/',
                    'rating': 4.6
                },
                {
                    'title': 'The Git & Github Bootcamp',
                    'platform': 'Udemy',
                    'duration': '15+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/the-git-github-bootcamp/',
                    'rating': 4.6
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Git Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (2+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Git and GitHub Tutorial',
                    'channel': 'Corey Schafer',
                    'duration': 'Series (1+ hours)',
                    'level': 'Beginner'
                }
            ]
        },
        'problem solving': {
            'courses': [
                {
                    'title': 'Problem Solving Skills for Business',
                    'platform': 'Coursera',
                    'duration': '2-3 weeks',
                    'level': 'Beginner',
                    'url': 'https://www.coursera.org/learn/problem-solving-skills',
                    'rating': 4.7
                },
                {
                    'title': 'Complete Problem-Solving Training',
                    'platform': 'Udemy',
                    'duration': '6+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/problem-solving-training/',
                    'rating': 4.4
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Problem Solving Techniques',
                    'channel': 'Skill Success',
                    'duration': 'Series (1+ hour)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Critical Thinking & Problem Solving',
                    'channel': 'Udacity',
                    'duration': 'Series (1+ hour)',
                    'level': 'Beginner'
                }
            ]
        },
        'rest api': {
            'courses': [
                {
                    'title': 'REST API Fundamentals',
                    'platform': 'Coursera',
                    'duration': '3-4 weeks',
                    'level': 'Intermediate',
                    'url': 'https://www.coursera.org/learn/rest-api-basics',
                    'rating': 4.5
                },
                {
                    'title': 'Design RESTful APIs with Flask',
                    'platform': 'Udemy',
                    'duration': '9+ hours',
                    'level': 'Intermediate',
                    'url': 'https://www.udemy.com/course/rest-api-flask-and-python/',
                    'rating': 4.6
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'REST API Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (1+ hour)',
                    'level': 'Beginner to Intermediate'
                },
                {
                    'title': 'Building REST APIs',
                    'channel': 'freeCodeCamp',
                    'duration': '3+ hours',
                    'level': 'Intermediate'
                }
            ]
        },
        'django': {
            'courses': [
                {
                    'title': 'Django for Beginners',
                    'platform': 'Udemy',
                    'duration': '29+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/django-for-beginners/',
                    'rating': 4.6
                },
                {
                    'title': 'Advanced Django',
                    'platform': 'Udemy',
                    'duration': '18+ hours',
                    'level': 'Intermediate to Advanced',
                    'url': 'https://www.udemy.com/course/advanced-django-web-development/',
                    'rating': 4.5
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Django Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (3+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Django Full Course',
                    'channel': 'Code with Stein',
                    'duration': '10+ hours',
                    'level': 'Beginner to Intermediate'
                }
            ]
        },
        'flask': {
            'courses': [
                {
                    'title': 'Flask by Example',
                    'platform': 'Udemy',
                    'duration': '10+ hours',
                    'level': 'Beginner to Intermediate',
                    'url': 'https://www.udemy.com/course/flask-by-example/',
                    'rating': 4.5
                },
                {
                    'title': 'REST APIs with Flask',
                    'platform': 'Udemy',
                    'duration': '9+ hours',
                    'level': 'Intermediate',
                    'url': 'https://www.udemy.com/course/rest-api-flask-and-python/',
                    'rating': 4.6
                }
            ],
            'youtube_tutorials': [
                {
                    'title': 'Flask Tutorial',
                    'channel': 'Traversy Media',
                    'duration': 'Series (2+ hours)',
                    'level': 'Beginner'
                },
                {
                    'title': 'Flask Full Course',
                    'channel': 'freeCodeCamp',
                    'duration': '3+ hours',
                    'level': 'Beginner to Intermediate'
                }
            ]
        }
    }
    
    @staticmethod
    def get_recommendations(missing_skills: List[str], num_resources: int = 3) -> Dict[str, Dict]:
        """
        Get learning resource recommendations for missing skills
        
        Args:
            missing_skills: List of skills the user lacks
            num_resources: Number of resources to recommend per skill
            
        Returns:
            Dictionary with recommendations organized by skill
        """
        recommendations = {}
        
        for skill in missing_skills[:10]:  # Limit to top 10 missing skills
            skill_lower = skill.lower()
            
            # Look for exact or partial match
            matched_skill = None
            for resource_skill in LearningResourcesRecommender.LEARNING_RESOURCES.keys():
                if resource_skill in skill_lower or skill_lower in resource_skill:
                    matched_skill = resource_skill
                    break
            
            if matched_skill:
                resource_data = LearningResourcesRecommender.LEARNING_RESOURCES[matched_skill]
                recommendations[skill] = {
                    'courses': resource_data['courses'][:num_resources],
                    'youtube_tutorials': resource_data['youtube_tutorials'][:num_resources],
                    'matched_skill': matched_skill
                }
            else:
                # Provide generic recommendations if no specific resource found
                recommendations[skill] = {
                    'courses': LearningResourcesRecommender._get_generic_recommendations(
                        skill, 'courses', num_resources
                    ),
                    'youtube_tutorials': LearningResourcesRecommender._get_generic_recommendations(
                        skill, 'youtube', num_resources
                    ),
                    'matched_skill': 'generic'
                }
        
        return recommendations
    
    @staticmethod
    def _get_generic_recommendations(skill: str, resource_type: str, num: int) -> List[Dict]:
        """
        Generate generic recommendations for skills without specific resources
        
        Args:
            skill: The skill to recommend for
            resource_type: 'courses' or 'youtube'
            num: Number of recommendations
            
        Returns:
            List of generic recommendation dictionaries
        """
        generic_courses = [
            {
                'title': f'{skill.title()} - Beginner Course',
                'platform': 'Coursera',
                'duration': '4-6 weeks',
                'level': 'Beginner',
                'url': f'https://www.coursera.org/search?query={skill}',
                'rating': 4.5
            },
            {
                'title': f'Master {skill.title()} - Complete Guide',
                'platform': 'Udemy',
                'duration': '10-20 hours',
                'level': 'Beginner to Intermediate',
                'url': f'https://www.udemy.com/courses/search/?q={skill}',
                'rating': 4.5
            },
            {
                'title': f'{skill.title()} Advanced Training',
                'platform': 'Udemy',
                'duration': '15-30 hours',
                'level': 'Intermediate to Advanced',
                'url': f'https://www.udemy.com/courses/search/?q={skill}',
                'rating': 4.4
            }
        ]
        
        generic_youtube = [
            {
                'title': f'{skill.title()} Tutorial',
                'channel': 'Traversy Media',
                'duration': '2-4 hours',
                'level': 'Beginner'
            },
            {
                'title': f'{skill.title()} Full Course',
                'channel': 'freeCodeCamp',
                'duration': '3-5 hours',
                'level': 'Beginner to Intermediate'
            },
            {
                'title': f'{skill.title()} Advanced Tutorial',
                'channel': 'Edureka',
                'duration': '2-3 hours',
                'level': 'Intermediate'
            }
        ]
        
        if resource_type == 'courses':
            return generic_courses[:num]
        else:
            return generic_youtube[:num]
    
    @staticmethod
    def create_personalized_learning_path(missing_skills: List[str], 
                                         role: str) -> Dict[str, any]:
        """
        Create a personalized learning path for the user
        
        Args:
            missing_skills: List of missing skills
            role: Target job role
            
        Returns:
            Personalized learning path dictionary
        """
        recommendations = LearningResourcesRecommender.get_recommendations(missing_skills)
        
        # Categorize skills by priority
        learning_path = {
            'role': role,
            'total_skills_to_learn': len(recommendations),
            'estimated_total_hours': 0,
            'resources': recommendations,
            'learning_strategy': []
        }
        
        # Calculate estimated hours
        for skill, rec in recommendations.items():
            if rec['courses']:
                # Extract hours from duration string (simplified)
                for course in rec['courses']:
                    if 'hours' in course['duration'].lower():
                        try:
                            hours = int(course['duration'].lower().split('+')[0].split()[0])
                            learning_path['estimated_total_hours'] += hours // len(rec['courses'])
                        except:
                            learning_path['estimated_total_hours'] += 10
        
        # Create learning strategy
        learning_path['learning_strategy'] = [
            f"1. Start with foundational skills: {', '.join([s for s in missing_skills[:3]])}",
            "2. Complete online courses for theoretical knowledge",
            "3. Watch YouTube tutorials for practical demonstrations",
            f"4. Practice with projects relevant to {role} roles",
            "5. Build a portfolio showcasing applied skills"
        ]
        
        return learning_path
    
    @staticmethod
    def get_skill_difficulty_level(skill: str) -> str:
        """
        Determine the difficulty level of learning a skill
        
        Args:
            skill: The skill name
            
        Returns:
            Difficulty level: 'Beginner', 'Intermediate', or 'Advanced'
        """
        beginner_skills = {
            'communication', 'problem solving', 'teamwork', 'excel',
            'python', 'javascript', 'html', 'css', 'git'
        }
        
        intermediate_skills = {
            'java', 'django', 'flask', 'rest api', 'sql',
            'data analysis', 'tableau', 'azure', 'jenkins'
        }
        
        advanced_skills = {
            'kubernetes', 'machine learning', 'tensorflow',
            'deep learning', 'advanced python', 'aws solutions architect'
        }
        
        skill_lower = skill.lower()
        
        if skill_lower in beginner_skills:
            return 'Beginner'
        elif skill_lower in intermediate_skills:
            return 'Intermediate'
        elif skill_lower in advanced_skills:
            return 'Advanced'
        else:
            return 'Intermediate'  # Default to intermediate


if __name__ == '__main__':
    # Test the recommender
    test_missing_skills = ['python', 'docker', 'communication', 'machine learning']
    recommendations = LearningResourcesRecommender.get_recommendations(test_missing_skills)
    
    print("Learning Resource Recommendations:")
    print("=" * 50)
    for skill, rec in recommendations.items():
        print(f"\n{skill.upper()}:")
        print(f"  Courses:")
        for course in rec['courses']:
            print(f"    - {course['title']} ({course['platform']})")
        print(f"  YouTube Tutorials:")
        for tutorial in rec['youtube_tutorials']:
            print(f"    - {tutorial['title']} ({tutorial['channel']})")

def analyze_skill_gap(skills, target_role):
    """
    Analyze the student's skills against a target software role.
    """

    role_skills = {
        "software developer": [
            "C",
            "Python",
            "Data Structures",
            "Algorithms",
            "SQL",
            "Git",
            "APIs"
        ],
        "data analyst": [
            "Python",
            "SQL",
            "Excel",
            "Statistics",
            "Data Visualization"
        ],
        "ai engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "SQL",
            "Git"
        ]
    }

    required = role_skills.get(
        target_role.lower(),
        role_skills["software developer"]
    )

    user_skills = {skill.lower() for skill in skills}

    missing = [
        skill for skill in required
        if skill.lower() not in user_skills
    ]

    matched = [
        skill for skill in required
        if skill.lower() in user_skills
    ]

    return {
        "target_role": target_role,
        "matched_skills": matched,
        "missing_skills": missing,
        "recommendation": (
            f"Focus first on: {', '.join(missing[:3])}"
            if missing
            else "You have covered the main skills for this role."
        )
    }


def generate_career_plan(target_role, missing_skills, days=30):
    """
    Create a simple action plan based on the student's
    missing skills.
    """

    if not missing_skills:
        return {
            "target_role": target_role,
            "duration_days": days,
            "plan": [
                "Build one portfolio project",
                "Practice coding problems",
                "Prepare for technical interviews",
                "Apply for internships"
            ]
        }

    plan = []

    for skill in missing_skills:
        plan.append(
            f"Learn {skill} and complete a small practical project."
        )

    plan.extend([
        "Practice interview questions",
        "Build or improve a GitHub portfolio project",
        "Apply for relevant internships"
    ])

    return {
        "target_role": target_role,
        "duration_days": days,
        "plan": plan
    }

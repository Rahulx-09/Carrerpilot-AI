from strands import Agent, tool
from tools import analyze_skill_gap, generate_career_plan


@tool
def skill_gap_analyzer(skills: list[str], target_role: str) -> dict:
    """
    Analyze a student's skills against the skills required
    for their target career.
    """
    return analyze_skill_gap(skills, target_role)


@tool
def career_plan_generator(
    target_role: str,
    missing_skills: list[str],
    days: int = 30
) -> dict:
    """
    Generate a practical career-learning plan.
    """
    return generate_career_plan(
        target_role,
        missing_skills,
        days
    )


careerpilot = Agent(
    tools=[
        skill_gap_analyzer,
        career_plan_generator
    ],
    system_prompt="""
You are CareerPilot AI, an autonomous career assistant
for college students and fresh graduates.

You help users:
1. Identify skill gaps.
2. Create personalized career plans.
3. Prepare for interviews.
4. Evaluate interview answers.
5. Recommend concrete next actions.

When a user asks about a skill gap, use the
skill_gap_analyzer tool.

When a user needs a learning plan, use the
career_plan_generator tool.

Be practical, specific, and encouraging.
"""
)


if __name__ == "__main__":
    response = careerpilot(
        """
        I want to become a software developer.
        I currently know C, Python and SQL.

        First analyze my skill gap.
        Then create a 30-day learning plan based
        on the missing skills.
        """
    )

    print(response)

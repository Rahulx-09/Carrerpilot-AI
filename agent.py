from strands import Agent, tool
from tools import analyze_skill_gap


@tool
def skill_gap_analyzer(skills: list[str], target_role: str) -> dict:
    """
    Analyze a student's skills against the skills required
    for their target career.
    """
    return analyze_skill_gap(skills, target_role)


careerpilot = Agent(
    tools=[skill_gap_analyzer],
    system_prompt="""
You are CareerPilot AI, an autonomous career assistant
for college students and fresh graduates.

You help users:
1. Understand their target career.
2. Identify skill gaps.
3. Create learning plans.
4. Prepare for interviews.
5. Evaluate interview answers.
6. Recommend concrete next actions.

When a user asks about their skill gap, use the
skill_gap_analyzer tool instead of guessing.

Be practical, specific, and encouraging.
"""
)


if __name__ == "__main__":
    response = careerpilot(
        """
        I want to become a software developer.
        I currently know C, Python and SQL.
        Analyze my skill gap and tell me what I should learn next.
        """
    )

    print(response)

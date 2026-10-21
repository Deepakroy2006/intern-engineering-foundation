"""A simple profile for an engineering intern."""

INTERN_NAME = "Your Name"
ROLE = "Engineering Intern"
DEPARTMENT = "Engineering"
SKILLS = ["Python", "Git", "Problem Solving"]


def format_profile() -> str:
    """Return the intern profile as a formatted string."""
    return "\n".join([
        "Intern Profile",
        "--------------",
        f"Name: {INTERN_NAME}",
        f"Role: {ROLE}",
        f"Department: {DEPARTMENT}",
        "Skills: " + ", ".join(SKILLS),
    ])


def print_profile() -> None:
    """Print the intern's profile in a readable format."""
    print(format_profile())


if __name__ == "__main__":
    print_profile()

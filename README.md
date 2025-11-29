# UE23CS341A : Software Engineering Laboratory

This repository contains code, documentation, and detailed problem statements for the laboratory exercises conducted during the fifth semester as part of the **Software Engineering (SE)** course.

## Repository Overview

The repository is structured into weekly folders, each dedicated to the laboratory exercises for a specific week, along with a mini-project folder for the course project.

### Folders

- **Lab1**: UML Diagrams and Software Design - Introduction to software modeling concepts with UML diagrams for a Coffee Kiosk system.
- **Lab2**: Jira Project Management - Hands-on experience with project management tools and agile methodologies using Jira.
- **Lab3**: Software Architecture - Component diagrams and architectural analysis for software systems.
- **Lab4**: Pair Programming (VibeCoding) - Collaborative coding exercise implementing a Ping-Pong game in Python with Pygame.
- **Lab5**: Static Code Analysis - Code quality analysis using tools like Pylint, Flake8, and Bandit for Python inventory management system.
- **Lab6**: Fuzz Testing - Property-based testing using Hypothesis framework to test robustness of string processing functions.
- **Lab7**: Code & Branch Coverage - Test coverage analysis using pytest-cov to ensure comprehensive testing of order processing system.
- **Miniproject**: Contains the Software Requirements Specification (SRS) template and project documentation.

## About the Course

The course, _UE23CS341A : Software Engineering_, focuses on hands-on learning of fundamental software engineering principles, methodologies, and best practices. Topics include software design patterns, testing strategies, code quality, collaborative development, and agile project management.

## Installation Instructions for macOS

To work on the exercises in this repository, you will need Python 3.x and various development tools. Here's how to set up your environment:

### Prerequisites

```bash
# Install Python 3 (if not already installed)
brew install python3

# Install pip packages for various labs
pip3 install pygame  # For Lab4 Ping-Pong game
pip3 install pylint flake8 bandit  # For Lab5 Static Code Analysis
pip3 install hypothesis pytest  # For Lab6 Fuzz Testing
pip3 install pytest pytest-cov  # For Lab7 Coverage Testing
```

### Running Lab Exercises

Each lab folder contains its own README with specific instructions. Generally:

```bash
# For Lab4 (Ping-Pong Game)
cd Lab4/PES1UG23CS488/ping-pong
python3 main.py

# For Lab5 (Static Code Analysis)
cd Lab5/static-code-analysis
pylint inventory_system.py
flake8 inventory_system.py
bandit -r inventory_system.py

# For Lab6 (Fuzz Testing)
cd Lab6/PES1UG23CS433
pytest test_processor.py

# For Lab7 (Coverage Testing)
cd Lab7
pytest --cov=order_processor --cov-report=html test_processor_CS433.py
```

## Contributions

We welcome contributions to improve this repository! Here's how you can contribute:

1. **Bug Reports**: If you find any issues in the code or documentation, feel free to open an issue in the repository.
2. **Enhancements**: Submit pull requests to add new features, improve existing code, or update documentation.
3. **Suggestions**: Share your ideas by creating a discussion thread.

### Guidelines for Contributors

- Ensure your code follows Python best practices and PEP 8 style guidelines.
- Provide detailed commit messages and explanations for your changes.
- Test your code thoroughly before submitting a pull request.
- Include appropriate documentation and comments in your code.

Thank you for your contributions!

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

Special thanks to the faculty and teaching assistants of UE23CS341A for their guidance and support throughout the course.

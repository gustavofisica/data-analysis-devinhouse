# Contributing to Data Analysis - DEVinHouse

Thank you for your interest in contributing to this project! Whether you're a fellow DEVinHouse student, instructor, or data enthusiast, your contributions are welcome.

## How to Contribute

### Bug Reports
- Check if the issue already exists in the [Issues](../../issues)
- Use the bug report template
- Include clear steps to reproduce
- Provide system information (Python version, OS, etc.)

### Feature Requests
- Use the feature request template
- Describe the use case and benefits
- Consider if it aligns with course objectives

### Documentation
- Fix typos or unclear explanations
- Add missing information in READMEs
- Improve code comments
- Translate content (if applicable)

### Code Contributions

#### Getting Started
1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/data-analysis-devinhouse.git
   cd data-analysis-devinhouse
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate   # Windows
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

#### Making Changes
1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed

3. **Test your changes**
   - Run affected scripts/notebooks
   - Verify data file paths work
   - Check for import errors

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add feature description"
   ```

#### Commit Message Guidelines
- Use conventional commits: `type(scope): description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Keep first line under 50 characters
- Examples:
  - `feat(M1S5): add data visualization notebook`
  - `fix(scripts): correct CSV file path in sales analysis`
  - `docs(README): add installation instructions`

#### Pull Request Process
1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request**
   - Use the PR template
   - Link to related issues
   - Describe what changed and why
   - Include screenshots for visual changes

3. **Address feedback**
   - Respond to code review comments
   - Make requested changes
   - Update documentation if needed

## Code Standards

### Python
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Maximum line length: 88 characters

### Jupyter Notebooks
- Clear markdown explanations between code cells
- Include cell outputs for visualizations
- Use relative paths for data files
- Add table of contents for long notebooks

### SQL
- Use uppercase for keywords (SELECT, FROM, WHERE)
- Indent subqueries properly
- Add comments for complex queries
- Test queries before committing

### Documentation
- Use clear, concise language
- Include code examples where helpful
- Update relevant README files
- Check spelling and grammar

## Course Context

This project follows the DEVinHouse 2025 curriculum:
- Respect assignment guidelines
- Don't share complete solutions before due dates
- Focus on learning objectives
- Encourage collaborative learning

## Questions?

- Create an [Issue](../../issues) for general questions
- Contact course instructors for academic guidance
- Join course discussion forums

## Recognition

Contributors will be acknowledged in:
- README contributors section
- Git commit history
- Course project presentations (if applicable)

---

Thank you for helping make this project better! 🚀
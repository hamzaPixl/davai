### Project Rules

---

### 1. Development Standards

#### Code Style and Formatting Guidelines
- **Definition**: All code must adhere to the Airbnb JavaScript Style Guide with ESLint for linting.
- **Rationale**: Consistent code style improves readability and maintainability.
- **Implementation**:
  - Use ESLint plugins to enforce code style during development.
  - Examples: 
    ```javascript
    // Good
    const variableName = 'value';

    // Bad
    var variable_name = 'value';
    ```

#### Naming Conventions
- **Definition**: Follow camelCase for variables and functions, and PascalCase for classes and components.
- **Rationale**: Clear and consistent naming enhances code understanding and navigation.
- **Implementation**:
  - Use descriptive names that reflect the purpose of the variable or function.
  - Examples:
    ```javascript
    // Good
    const userName = 'John Doe';

    // Bad
    const user_name = 'John Doe';
    ```

#### Code Organization and Project Structure Standards
- **Definition**: Organize code logically by feature or module, following a consistent folder structure.
- **Rationale**: Structured codebase improves maintainability and scalability.
- **Implementation**:
  - Separate frontend and backend code into distinct directories.
  - Examples:
    ```
    /frontend
      /components
      /pages
    /backend
      /controllers
      /models
    ```

#### Documentation Requirements and Standards
- **Definition**: Every function, module, and API endpoint must have clear documentation using JSDoc comments.
- **Rationale**: Comprehensive documentation facilitates code understanding and collaboration.
- **Implementation**:
  - Use JSDoc syntax to document parameters, return values, and function purpose.
  - Examples:
    ```javascript
    /**
     * Add two numbers.
     * @param {number} a - The first number.
     * @param {number} b - The second number.
     * @returns {number} The sum of a and b.
     */
    function addNumbers(a, b) {
      return a + b;
    }
    ```

---

### 2. Git Workflow & Version Control

#### Branch Naming Conventions and Workflow
- **Definition**: Use feature branches prefixed with the Jira ticket number and a brief description (e.g., `PROJ-123-feature-name`).
- **Rationale**: Clear branch names help track changes and associate them with specific tasks.
- **Implementation**:
  - Enforce branch naming conventions through pre-commit hooks or Git templates.
  - Examples:
    ```
    git checkout -b PROJ-123-feature-name

    git push origin PROJ-123-feature-name
    ```

#### Commit Message Standards and Templates
- **Definition**: Follow the conventional commit message format (e.g., `feat: implement feature XYZ`).
- **Rationale**: Standardized commit messages aid in understanding changes and generating release notes.
- **Implementation**:
  - Provide commit message templates for consistent documentation.
  - Examples:
    ```
    feat: implement feature XYZ

    fix: resolve issue with component ABC
    ```

#### Pull Request Process and Review Guidelines
- **Definition**: Require code reviews for all pull requests before merging.
- **Rationale**: Peer reviews ensure code quality, catch errors, and share knowledge.
- **Implementation**:
  - Set up branch protection rules to enforce code reviews.
  - Examples:
    - Reviewer checklist:
      - Code follows style guide
      - Unit tests added/updated
      - Functional requirements met

#### Release and Deployment Procedures
- **Definition**: Follow semantic versioning for releases (major.minor.patch) and automated deployments.
- **Rationale**: Clear versioning aids in tracking changes and deployments.
- **Implementation**:
  - Use CI/CD pipelines for automated testing, building, and deployment.
  - Examples:
    - Release versioning:
      - `v1.0.0`
    - Deployment strategy:
      - Staging -> QA -> Production

---

*(Continued in the next message)*
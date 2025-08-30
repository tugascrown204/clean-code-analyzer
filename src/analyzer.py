import sys
import ast

class CleanCodeAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.issues = []

    def analyze(self):
        with open(self.filename, 'r') as file:
            node = ast.parse(file.read(), filename=self.filename)
            self.visit(node)
        return self.issues

    def visit(self, node):
        for n in ast.walk(node):
            self.check_for_issues(n)

    def check_for_issues(self, node):
        if isinstance(node, ast.FunctionDef):
            self.check_function_name(node)
            self.check_function_complexity(node)
        elif isinstance(node, ast.Assign):
            self.check_variable_naming(node)
        # Add more checks as needed

    def check_function_name(self, node):
        if not node.name.islower():
            self.issues.append(f"Function name '{node.name}' should be lowercase")

    def check_function_complexity(self, node):
        if len(node.body) > 10:  # Example complexity check
            self.issues.append(f"Function '{node.name}' has too many lines")

    def check_variable_naming(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name) and not target.id.islower():
                self.issues.append(f"Variable name '{target.id}' should be lowercase")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <python_file>")
        sys.exit(1)
    filename = sys.argv[1]
    analyzer = CleanCodeAnalyzer(filename)
    issues = analyzer.analyze()
    if issues:
        print('Issues found:')
        for issue in issues:
            print(f'- {issue}')
    else:
        print('No issues found.')

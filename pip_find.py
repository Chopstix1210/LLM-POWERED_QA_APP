import subprocess
import os

def find_package_documentation(package_name):
    try:
        # Use pip show to get the installation information for the package
        result = subprocess.run(['pip3', 'show', package_name], capture_output=True, text=True, check=True)
        output_lines = result.stdout.splitlines()

        # Find the line starting with 'Location:'
        location_line = next(line for line in output_lines if line.startswith('Location:'))
        package_location = location_line.split(': ', 1)[1].strip()

        # Construct the path to the documentation
        doc_path = os.path.join(package_location, package_name)

        return doc_path
    except subprocess.CalledProcessError:
        print(f"Error: Package {package_name} not found")
        return None

def load_package_documentation(package_name):
    doc_path = find_package_documentation(package_name)
    if doc_path:
        try:
            with open(doc_path, 'r') as f:
                package_documentation = f.read()
            return package_documentation
        except FileNotFoundError:
            print(f"Error: Documentation not found at {doc_path}")
    return None

# Example: Find and load documentation for the langchain package
langchain_documentation = load_package_documentation('langchain')

if langchain_documentation:
    print("Langchain documentation:")
    print(langchain_documentation)

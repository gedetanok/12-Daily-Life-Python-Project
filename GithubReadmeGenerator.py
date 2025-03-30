
def generate_markdown_file():
    # Prompting user for inputs
    repository_name = input("\n Enter the name of your GitHub repository: ")
    project_description = input("Enter a short description of your project: ")
    installation_instructions = input("Enter installation instructions for your project: ")
    usage_instructions = input("Enter usage instructions for your project: ")
    contributors = input("Enter the contributors to your project (separated by commas): ")
    license = select_license()

    # Generating badges
    stars_badge = "[![GitHub stars](https://img.shields.io/github/stars/{})](https://github.com/{}/stargazers)".format(repository_name, repository_name)
    forks_badge = "[![GitHub forks](https://img.shields.io/github/forks/{})](https://github.com/{}/network/members)".format(repository_name, repository_name)
    issues_badge = "[![GitHub issues](https://img.shields.io/github/issues/{})](https://github.com/{}/issues)".format(repository_name, repository_name)
    license_badge = "[![GitHub license](https://img.shields.io/github/license/{})](https://github.com/{}/blob/master/LICENSE)".format(repository_name, repository_name)

    # Generating Markdown content
    markdown_content = f"""
    # {repository_name}
    {project_description}
    ## Table of Contents
    - [Installation](#installation)
    - [Usage](#usage)
    - [Contributors](#contributors)
    - [License](#license)
    - [Badges](#badges)
    - [GitHub Repository](#github-repository)
    ## Installation
    ```
    {installation_instructions}
    ```
    ## Usage
    ```
    {usage_instructions}
    ```
    ## Contributors
    {contributors}
    ## License
    This project is licensed under the {license} License - see the [LICENSE](LICENSE) file for details.
    ## Badges
    {stars_badge} {forks_badge} {issues_badge} {license_badge}
    ## GitHub Repository
    [Link to GitHub repository](https://github.com/{repository_name})
    """
    # Writing content to Markdown file
    markdown_file_name = f"{repository_name}_README.md"
    with open(markdown_file_name, "w") as markdown_file:
        markdown_file.write(markdown_content)
    print(f"Markdown file '{markdown_file_name}' generated successfully!")

def select_license():
    licenses = {
        "MIT": "MIT License",
        "Apache": "Apache License 2.0",
        "GPL": "GNU General Public License v3.0",
        # Add more licenses as needed
    }
    print("Select a license for your project:")
    for key, value in licenses.items():
        print(f"{key}: {value}")
    while True:
        selected_license = input("Enter the number corresponding to your selected license: ")
        if selected_license in licenses:
            return licenses[selected_license]
        else:
            print("Invalid input. Please enter a valid license number.")

if __name__ == "__main__":
    generate_markdown_file()
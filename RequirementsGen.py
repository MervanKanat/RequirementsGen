
import subprocess
import pkg_resources

def write_packages_to_file(filename, packages):
    """
    Writes a list of packages to a specified file.

    Parameters:
    filename (str): The name of the file to write to.
    packages (list): A list of package strings to write.
    """
    with open(filename, 'w') as file:
        for package in packages:
            file.write(f"{package}\n")

# Run 'pip freeze' command and capture the output
result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
installed_packages_from_pip = result.stdout.splitlines()

# Filter lines to include only those with '==' or extract package name from lines with '@'
filtered_packages = [line if '==' in line else line.split('@')[0] for line in installed_packages_from_pip]

# Write the filtered package list to 'requirements.txt'
write_packages_to_file('requirements.txt', filtered_packages)

# Check installed packages and list them in the format {package_name==version}
installed_packages = pkg_resources.working_set
package_info = [f"{package.project_name}=={package.version}" for package in installed_packages]

# Check for packages not in 'requirements.txt' and prepare to add them
unique_packages = [package for package in package_info if package not in filtered_packages]

# Write these unique packages to 'requirementsUpdate.txt'
write_packages_to_file('requirementsUpdate.txt', unique_packages)

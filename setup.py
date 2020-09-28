from setuptools import setup, find_packages

with open('README.md') as file:
    README = file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup(
    name='b_jira_filter',
    version='0.0.1',
    license='Apache License 2.0',
    packages=find_packages(exclude=[
        # Exclude virtual environment.
        'venv',
        # Exclude test source files.
        'b_jira_filter_test'
    ]),
    entry_points={
        'console_scripts': [
            'jira.sprints.storypoints=b_jira_filter.commands.sprint_story_points:sprint_story_points'
        ],
    },
    description='Script library to interact with JIRA API.',
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        'jira>=2.0.0,<3.0.0',
    ],
    author='Laimonas Sutkus',
    author_email='laimonas.sutkus@biomapas.com',
    keywords='JIRA',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
)
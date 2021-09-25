import json
from github import Github

token = 'ENTER TOKEN HERE'
g = Github(token)


def Commit(data):
    content = json.dumps(data, indent=2)

    repo = g.get_repo("silvan12/silvan.tech")
    contents = repo.get_contents("Projects/current_projects.json")
    repo.update_file(contents.path, "Update current_project", content, contents.sha)
    print("Commit to GitHub success.")


def Delete(data):
    del data[-1]
    print("Deleted last entry")
    Commit(data)


def Update(data):
    name = input("Enter project name:\n>")
    link = input("Enter GitHub link:\n>")

    a_dict = {'name': name, 'github': link}
    data.append(a_dict)
    print("Added one entry")
    Commit(data)

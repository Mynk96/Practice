from github import Github

g = Github("Mynk96", "Watthefun@13")

repo_dir = 'Practice'
repo = Repo(repo_dir)
file_list = ['test.txt']
commit_message = 'added test files'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()

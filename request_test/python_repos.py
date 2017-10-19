import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# 将API存储在一个变量中
response_dict = r.json()
print(r.json())
print(response_dict.keys())
print("Total repositories", response_dict['total_count'])

# 搜索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        # 'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=-45, show_legend=False)
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# #研究有关仓库的信息
# print("\nSelected information about each repository:\n")
# for repo_dict in repo_dicts:
#     print('\nSelected information about first repository:\n')
#     print('Name: ', repo_dict['name'])
#     print('Owner: ', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])

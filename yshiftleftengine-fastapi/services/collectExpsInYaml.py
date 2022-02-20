import yaml

ExpYamlPath = "C:\\Users\\yqy11\\Desktop\\exp.yml"


def CollectExpsInYaml():
    with open(ExpYamlPath, 'r', encoding='utf-8') as file:
        experiences = yaml.safe_load(file)
    return experiences

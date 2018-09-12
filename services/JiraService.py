from jira import JIRA

server = 'https://services.nisc.coop/services'
jira = JIRA(server=server, basic_auth=("gmausshardt", "Leahbestgirl10hearts"))

class JiraService:

    def get_jira():
        return jira

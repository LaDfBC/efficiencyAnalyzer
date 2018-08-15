from flask import Flask
from flask_restful import Resource, Api
from jira import JIRA
from flask_jsonpify import jsonify
import json

server = 'https://jira.nisc.coop/jira'
jira = JIRA(server=server, basic_auth=("gmausshardt", "Leahbestgirl10hearts"))

app = Flask(__name__)
api = Api(app)

class IssuesByIds(Resource):
    def get(self, jira_numbers):
        issues = {}
        for number in jira_numbers.split(','):
            issues[number] = jira.issue(number).key

        finale = {}
        finale['issues'] = issues
        return jsonify(finale)

class IssuesByOwners(Resource):
    def get(self, owners):
        issues = {}
        for owner in owners.split(','):
            issues[owner] = []
            current_issues = jira.search_issues('assignee = ' + owner + ' and resolution = "Unresolved"')
            for issue in current_issues:
                issues[owner].append(issue.key)
        finale = {}
        finale['issues'] = issues
        return jsonify(finale)

api.add_resource(IssuesByIds, '/issues/numbers/<jira_numbers>')
api.add_resource(IssuesByOwners, '/issues/owners/<owners>')


if __name__ == '__main__':
    app.run(port='5003')
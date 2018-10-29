from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from issueUtil import prettify
from services import JiraService

class IssuesByIds(Resource):
    def get(self, jira_numbers):
        issues = {}
        for number in jira_numbers.split(','):
            issues[number] = JiraService.jira.issue(number).key

        finale = {}
        finale['issues'] = issues
        return jsonify(finale)

class IssuesByOwners(Resource):
    def get(self, owners):
        issues = {}
        for owner in owners.split(','):
            issues[owner] = []
            current_issues = JiraService.jira.search_issues('assignee = ' + owner + ' and resolution = "Unresolved"')
            for issue in current_issues:
                # issues[owner].append(issue)
                issues[owner].append(prettify(issue))
        finale = {}
        finale['issues'] = issues
        return jsonify(finale)

class IssuesByTeams(Resource):
    def get(self, teams):
        issues = {}
        for team in teams.split(','):
            issues[team] = []
            current_issues = JiraService.jira.search_issues('customfield_11509 = ' + team + ' and resolution = "Unresolved"')
            for issue in current_issues:
                issues[team].append(prettify(issue))
        finale = {}
        finale['issues'] = issues
        return jsonify(finale)



if __name__ == '__main__':
    app.run(port='5003')
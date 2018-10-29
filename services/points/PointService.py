from flask_restful import Resource
from flask_jsonpify import jsonify

from services.JiraService import JiraService


class PointsByIssueNumbers(Resource):
    def get(self, jiraNumbers):
        issues = {}
        points = {}
        for number in jiraNumbers.split(','):
            issues[number] = JiraService.get_jira().issue(number).key

        for issue in issues:
            points[issue.key] = str(issue.fields.customfield_10002)

        finale = {}
        finale['points'] = points
        return jsonify(finale)

class PointsByTeamBySprint(Resource):
    def get(self, teams, sprints):
        sprints = {}
        points = {}
        for sprint in sprints:
            fetched_sprint = JiraService.get_jira().sprint(sprint)

        return jsonify(points)

class PointsBySprintInGeneral(Resource):
    def get(self, sprints):
        return jsonify({})
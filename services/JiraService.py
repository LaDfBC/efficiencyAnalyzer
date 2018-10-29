from flask import Flask, request
from flask_restful import Api
from jira import JIRA
import IssueService
from points import PointService

server = 'https://services.nisc.coop/services'
jira = JIRA(server=server, basic_auth=("gmausshardt", "Leahbestgirl10hearts"))

app = Flask(__name__)
api = Api(app)



def get_jira():
    return jira

@app.route('/issues/numbers/<jira_numbers>', methods=['GET'])
def get_issues(jira_numbers):
    owners = request.args.get('owners')
    return IssueService.IssuesByIds.get(jira_numbers)

@app.route('/points/numbers/<jira_numbers>')
def get_points(jira_numbers):
    owners = request.args.get('owners')
    return __process_request(jira_numbers, owners)

def __process_request(jira_numbers, owners):
    issues = IssueService.IssuesByIds.get(jira_numbers)
    return jsonify(xxxxfilterxxxx(issues, owners))

# Issue-based Requests
api.add_resource(IssueService.IssuesByIds, '/issues/numbers/<jira_numbers>')
api.add_resource(IssueService.IssuesByOwners, '/issues/owners/<owners>')
api.add_resource(IssueService.IssuesByTeams, '/issues/teams/<teams>')

# Point-based Requests
api.add_resource(PointService.PointsByIssueNumbers, '/points/issues/<issues>')
api.add_resource(PointService.PointsBySprintInGeneral, '/points/sprints/<sprints>')
api.add_resource(PointService.PointsByTeamBySprint '/points/')

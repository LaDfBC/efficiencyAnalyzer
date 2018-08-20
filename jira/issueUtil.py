# Utility Methods for dealing with JIRA Issues from the JIRA API

#Type is JIRA.resources.Issue
def prettify(issue):
    final_issue = {}
    final_issue["number"] = str(issue.key) # Number, i.e., MDMS-3542
    final_issue["assignee"] = str(issue.fields.assignee)
    final_issue["components"] = str(issue.fields.components)
    final_issue["created"] = str(issue.fields.created)
    final_issue["creator"] = str(issue.fields.creator)

    try:
        final_issue["sprints"] = str(issue.fields.customfield_10005) # Which sprints has this JIRA been a part of?
    except AttributeError:
        final_issue["sprints"] = []

    try:
        final_issue["team"] = str(issue.fields.customfield_11905)
    except AttributeError:
        final_issue["team"] = "No Team"

    try:
        final_issue['story_points'] = str(issue.fields.customfield_10002) # Or, "Estimation"
    except AttributeError:
        pass # None.  This has no point count

    if issue.fields.description: # Else, don't even add it. Blank is blank
        final_issue["description"] = issue.fields.description.encode("ascii", 'ignore')

    final_issue["fixVersions"] = str(issue.fields.fixVersions)
    try:
        final_issue["parent"] = str(issue.fields.parent) # Epic or Story this JIRA belongs to
    except AttributeError:
        pass
    final_issue["priority"] = str(issue.fields.priority)
    final_issue["project"] = str(issue.fields.project)
    final_issue["reporter"] = str(issue.fields.reporter)
    final_issue["summary"] = str(issue.fields.summary)
    final_issue["updated"] = str(issue.fields.updated)

    return final_issue

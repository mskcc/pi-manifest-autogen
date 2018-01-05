import base64
import json
import subprocess
import urllib2

import logging
from logging import handlers
import sys
import regenerateconfig

def initLogger():
    global logger
    logger = logging.getLogger('regenerate')
    logger.setLevel(logging.DEBUG)
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format)
    logger.addHandler(ch)
    fh = handlers.RotatingFileHandler("logs/regenerate-manifest.log", maxBytes=(1048576 * 5), backupCount=7)
    fh.setFormatter(format)
    logger.addHandler(fh)


def regenerate(projectId):
    logger.info("Regenerating manifest files for project: " + projectId)
    generateFilesScript = regenerateconfig.runSingleProjectPath

    logger.info("Running script: " + generateFilesScript)

    subprocess.check_output(["{0} {1}".format(generateFilesScript, str(projectId))], shell=True)
    logger.info("Script: " + generateFilesScript + " finished")


def invokeQuery(query):
    logger.info("Invoking query: " + query)

    req = urllib2.Request(query)
    authheader = "Basic " + base64.b64encode(regenerateconfig.username + ":" + regenerateconfig.password)
    req.add_header("Authorization", authheader)
    req.add_header("Content-Type", "application/json")
    response = urllib2.urlopen(req)

    return json.loads(response.read())


def regenerateProjects():
    query = regenerateconfig.jiraUrl + 'rest/api/2/search?jql=project=' + regenerateconfig.roslinProject + '+AND+status=%22' + regenerateconfig.toGenerateStatus + '%22'
    projectsToRegenerate = invokeQuery(query)

    projectIds = []

    for issue in projectsToRegenerate['issues']:
        projectId = issue['fields']['summary']
        projectIds.append(projectId)

    logger.info("Found {0} projects to regenerate: {1}".format(len(projectIds), projectIds))

    for projectId in projectIds:
        regenerate(projectId)

if __name__ == "__main__":
    initLogger()
    regenerateProjects()

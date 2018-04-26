import ConfigParser
import StringIO
import base64
import json
import logging
import subprocess
import sys
import urllib2
from logging import handlers

import generateconfig

dummySection = 'root'
ini_str = '[' + dummySection + ']\n' + open(generateconfig.createManifestProperties, 'r').read()
ini_fp = StringIO.StringIO(ini_str)
manifestconfig = ConfigParser.RawConfigParser()
manifestconfig.readfp(ini_fp)


def initLogger():
    global logger
    logger = logging.getLogger('Generate ROSLIN inputs')
    logger.setLevel(logging.DEBUG)
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format)
    logger.addHandler(ch)
    fh = handlers.TimedRotatingFileHandler(generateconfig.logFile, when='midnight')
    fh.setFormatter(format)
    logger.addHandler(fh)


def regenerate(projectId):
    logger.info("Regenerating manifest files for project: " + projectId)
    generateFilesScript = generateconfig.runSingleProjectPath

    logger.info("Running script: " + generateFilesScript)

    subprocess.check_output(["{0} {1}".format(generateFilesScript, str(projectId))], shell=True)
    logger.info("Script: " + generateFilesScript + " finished")


def invokeQuery(query):
    logger.info("Invoking query: " + query)

    req = urllib2.Request(query)
    authheader = "Basic " + base64.b64encode(getProperty('jira.username') + ":" + getProperty('jira.password'))
    req.add_header("Authorization", authheader)
    req.add_header("Content-Type", "application/json")
    response = urllib2.urlopen(req)

    return json.loads(response.read())


def regenerateProjects():
    query = getProperty('jira.url') + '/' + getProperty('jira.rest.path') + '/search?jql=project=' + getProperty('jira.roslin.project.name') + \
            '+AND+(status=%22' + getProperty('jira.roslin.fastqs.available.status') + '%22+OR+status=%22' + \
            getProperty('jira.roslin.input.regeneration.status') + '%22)&maxResults=' + str(
        generateconfig.maxNumberOfRequestsReturned)
    projectsToGenerate = invokeQuery(query)

    projectIds = []

    totalNumberOfProjects = projectsToGenerate["total"]

    logger.info("Total number of projects to generate files: {0}".format(totalNumberOfProjects))

    for issue in projectsToGenerate['issues']:
        projectId = issue['fields']['summary']
        projectIds.append(str(projectId))

    logger.info("Found {0} projects to generate: {1}".format(len(projectIds), projectIds))

    for projectId in projectIds:
        regenerate(projectId)


def getProperty(propertyName):
    property = manifestconfig.get(dummySection, propertyName)
    if("transition" in propertyName or "status" in propertyName):
        formattedProperty = "+".join(property.split())
        if (propertyName is not formattedProperty):
            logger.info("Retrieving property: {0}. Original value: {1}, formatted value: {2}".format(propertyName, property,
                                                                                                     formattedProperty))
        return formattedProperty
    return property


if __name__ == "__main__":
    initLogger()
    regenerateProjects()

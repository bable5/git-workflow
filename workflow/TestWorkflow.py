from git import *
import Workflow as wf

"""
Stubs for testing.
"""

def createBranchName(issueName, desc):
    return wf.createBranchName(issueName, desc)

def startIssue(issueName, root, desc=None):
    print issueName, root, desc
    branchName = createBranchName(issueName, desc)
    print("Checkout: " + branchName + " from " + root)

def deleteIssue(issueName, desc=None, defaultBranch='master'):
    branchName = createBranchName(issueName, desc)
    print ("Checking out " + str(defaultBranch))
    print ("Deleting " + str(branchName))

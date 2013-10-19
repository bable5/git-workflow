from git import *

def prefix():
    # TODO: Extract to common class if other workflow providers installed
    return "issue/"

def __findRepo():
    return Repo(".")

def createBranchName(issueName, desc):
    branchName = prefix() + str(issueName)
    if (desc != None):
        branchName += "/" + str(desc)

    return branchName


def startIssue(issueName, root, desc=None):
    """ Start a new issue branch """
    print issueName, root, desc

    repo = __findRepo()
    branchName = createBranchName(issueName, desc)

    print("Checkout: " + branchName)

    repo.git.checkout(root, b=branchName)

def deleteIssue(issueName, desc=None, defaultBranch='master'):
    """ Delete an issue branch
    @param issueName
    @param desc 
    @param defaultBranch -- branch the git repo will be on when the issue branch is deleted. Defaults to master
    """

    repo = __findRepo()
    branchName = createBranchName(issueName, desc)
    print ("Checking out " + str(defaultBranch))
    repo.git.checkout(defaultBranch)

    print ("Deleting " + str(branchName))
    repo.git.branch('-d', branchName)

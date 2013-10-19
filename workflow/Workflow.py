#   Copyright 2013 Sean L. Mooney
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from git import *
import os.path

def prefix():
    # TODO: Extract to common class if other workflow providers installed
    return "issue/"

def findRepo():
    return Repo(os.getcwd())

def createBranchName(issueName, desc):
    branchName = prefix() + str(issueName)
    if (desc != None):
        branchName += "/" + str(desc)

    return branchName


def startIssue(issueName, root, desc=None):
    """ Start a new issue branch """
    print issueName, root, desc

    repo = findRepo()
    branchName = createBranchName(issueName, desc)

    print("Checkout: " + branchName)

    repo.git.checkout(root, b=branchName)

def deleteIssue(issueName, desc=None, defaultBranch='master'):
    """ Delete an issue branch
    @param issueName
    @param desc 
    @param defaultBranch -- branch the git repo will be on when the issue branch is deleted. Defaults to master
    """

    repo = findRepo()
    branchName = createBranchName(issueName, desc)
    print ("Checking out " + str(defaultBranch))
    repo.git.checkout(defaultBranch)

    print ("Deleting " + str(branchName))
    repo.git.branch('-d', branchName)

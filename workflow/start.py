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

import Workflow as wf
#import TestWorkflow as wf
import argparse

def startIssue(issueName, root, desc=None):
    wf.startIssue(issueName, 'master', desc)

def parseArgs():
    """ Args
    --issue-name=<issue-name>
    [--desc=<description>
    [--start-from=<treeish>]
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--issue",
                        help="Issue Name/Number",
                        required=True
                        )
    parser.add_argument("-s", "--start_from",
                       default='master',
                       help="Treeish point to start the issue from, defaults to 'master'")
    parser.add_argument("--desc", dest="desc",
                       default=None,
                       help="Description for the issue.")

    args = parser.parse_args()

    issue = args.issue
    root  = args.start_from
    desc  = args.desc
    return issue, root, desc

def main():
    issue, root, desc = parseArgs()
    print issue, root, desc
    startIssue(issue, root, desc)

if __name__ == "__main__":
    main()

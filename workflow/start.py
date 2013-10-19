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

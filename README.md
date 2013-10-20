git-workflow 
============

Automate interaction with an issue tracker/planning 

Current supports Jira, but is designed to be general enough to support an issue
tracker which integrates with git commits.

Description 
====

<code>git-workflow</code> is similar to the 
<a href"http://nvie.com/posts/a-successful-git-branching-model/">git flow</a>
concept, but is centered around making it easy to use <code>git</code> with an
issue tracker such as Jira.  <code>git-workflow</code> automates creating issue
(topic) branches and appending the appropriate markers to the commit messages
to get <code>git</code> repos and issues trackers linked.


Commands 
======

*     $> git workflow start -i &lt;issue-identifier</it>&gt;
*     $> git workflow commit
*     $> git workflow finish

Requirements
====

* <a href="https://github.com/gitpython-developers/GitPython">GitPython</a>

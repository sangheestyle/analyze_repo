#Analyze Repo

Representing status of development by analyzing repository. You can see some example at the bottom of this page.

##What to do
* Showing 'Who modified which files?'
* Showing Relationship among authors by a file.
* Representing graph visualization for above items.

##Requirements
You might want to install [Pattern](https://github.com/clips/pattern).
``` bash
$ pip install -r requirements.txt
```
##Examples
You can get a graph representing relationship among committers and files modified by themselves. To do, you need to clone a git repository and make sure the path `/path/to/git`. After doing following command, you can find a folder named `project_name` and click index.html in the folder.

``` bash
$ python examples/graph_log_with_diffstats.py project_name /path/to/git
```

##Gallery
You can see some pre-built graphs.
* [Android framework git - weighted](https://googledrive.com/host/0B-YJnfgGCje6MDItb3R6cDFlbEE/index.html)
* [Android framework git](https://googledrive.com/host/0B-YJnfgGCje6SGZ5Mklrc0dLWW8/index.html)

import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analyze_repo.log_stat import LogStat
from analyze_repo.log_stat_graph import LogStatGraph


if len(sys.argv) != 3:
    print "usage: python graph_log_with_diffstats.py [project_name] [git_path]"
    print "e.g.: python graph_log_with_diffstats.py framework /path/to/git"
    print "You can open the folder named [project_name] and click index.html!"
    exit()
elif not os.path.isdir(sys.argv[2]):
    print "error: check your git repo path"

repo_name, repo_path = sys.argv[1:3]

# config pattern.graph module
# see http://www.clips.ua.ac.be/pages/pattern-graph

# config canvas size
# see http://www.clips.ua.ac.be/pages/pattern-graph#canvas
canvas_width = 2000
canvas_height = 1000

# config graph prune depth
# see http://www.clips.ua.ac.be/pages/pattern-graph#graph
depth = 0

# get log stats from the given git repo
log_stat = LogStat(repo_name, repo_path)
log_stat.do_log()

# generate a folder including html
g = LogStatGraph(repo_name)
g.load(log_stat)
g.prune(depth)
g.export(width=canvas_width, height=canvas_height)
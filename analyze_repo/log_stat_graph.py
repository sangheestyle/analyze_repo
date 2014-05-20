from pattern.graph import Graph


class LogStatGraph:

    def __init__(self, name=None):
        self.name = None
        self.graph = Graph()

    def load(self, log_stat):
        if self.name is None:
            self.name = log_stat.repo_name
        for commit in log_stat.commits:
            author_email = commit.ae
            self.graph.add_node(author_email)
            for diffstat in commit.diffstats:
                file_path = diffstat["file_path"]
                self.graph.add_node(file_path)
                # for reference
                # int(diffstat["deletions"]) + int(diffstat["insertions"])
                self.graph.add_edge(author_email, file_path)

    def prune(self, depth=0):
        self.graph.prune(depth)

    def export(self, path=None, **kwargs):
        if path is None:
            path = self.name
        self.graph.export(path, directed=True, **kwargs)


if __name__ == "__main__":
    from analyze_repo.log_stat import LogStat

    repo_name="framework"
    repo_path="/home/sanghee/Dev/platform_frameworks_base"
    depth = 0
    log_stat = LogStat(repo_name, repo_path)
    log_stat.do_log()

    g = LogStatGraph(repo_name)
    g.load(log_stat)
    g.prune(depth)
    g.export(width=2000, height=1500)
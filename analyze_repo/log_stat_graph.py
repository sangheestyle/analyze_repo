from pattern.graph import Graph

#COLOR PRESET
BLACK_15 = (0,0,0,0.15)
BLACK_25 = (0,0,0,0.25)
BLACK_50 = (0,0,0,0.50)

class LogStatGraph:

    def __init__(self, name=None):
        self.name = None
        self.graph = Graph()

    def load(self, log_stat):
        if self.name is None:
            self.name = log_stat.repo_name
        for commit in log_stat.commits:
            author_email = commit.ae
            self.graph.add_node(author_email, fill=BLACK_50)
            for diffstat in commit.diffstats:
                file_path = diffstat["file_path"]
                self.graph.add_node(file_path, stroke=BLACK_25, text=BLACK_15)
                self.graph.add_edge(author_email, file_path, stroke=BLACK_25)

    def prune(self, depth=0):
        self.graph.prune(depth)

    def export(self, path=None, **kwargs):
        if path is None:
            path = self.name
        self.graph.export(path, directed=True, weighted=True, **kwargs)
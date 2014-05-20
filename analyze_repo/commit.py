class Commit:

    def __init__(self, h, ae):
        self.h = h
        self.ae = ae
        self.diffstats = []

    def add_diffstat(self, insertions, deletions, file_path):
        diffstat = {"insertions": insertions,
                    "deletions": deletions,
                    "file_path": file_path}
        self.diffstats.append(diffstat)
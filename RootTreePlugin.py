import ete3

class RootTreePlugin:
    def input(self, inputfile):
       self.T = ete3.Tree(inputfile)

    def run(self):
       root_point = self.T.get_midpoint_outgroup()
       self.T.set_outgroup(root_point)

    def output(self, outputfile):
       self.T.write(outfile=outputfile)

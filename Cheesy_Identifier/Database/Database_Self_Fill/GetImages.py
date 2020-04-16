
"""

Array of queries shall be like:  ["provolone", "cheddar"]
For more than one element in query: "provolone cheddar" for example.
So it should be like:  ["provolone", "cheddar", "provolone cheddar"].

"""
import os
import time

class extractor():
    def __init__(self, _path_, _queries_, n_images, _additional_features_, _clean_="no"):
        self.xampp_path = _path_
        self.query = _queries_
        self.number = n_images
        self.add_fts = _additional_features_
        self.clean = _clean_

    def array_implode(self, array):
        if len(array) == 0:
            return ""
        return "_DL_".join(["_".join(x.split()) for x in array])

    def fragment_array(self):
        return [("?link="+self.array_implode([self.query[x]])
                +"_QF_"
                +"_QF_"+self.clean
                +"_QF_"+str(self.number)
                +"_QF_"+"\\".join(os.path.abspath(os.getcwd()).split("\\")[:-1])) for x in range(0, len(self.query))]

    def implode_arrays(self):
        return ("?link="+self.array_implode(self.query)
                +"_QF_"
                +"_QF_"+self.clean
                +"_QF_"+str(self.number)
                +"_QF_"+"\\".join(os.path.abspath(os.getcwd()).split("\\")[:-1]))

    def permutation(self):
        if self.add_fts != []:
            self.query = [ x+" "+y for x in self.query for y in self.add_fts]

    def cmd_command(self, optional=""):
        cmd = "start /max http://localhost/Extractor_algorithm_Cheesy_Identifier/getImages.php"
        return cmd+self.implode_arrays() if optional=="" else cmd+optional

    def start_apache(self):
        os.system("START \"\" "+self.xampp_path+"/apache_start")
        time.sleep(4)

    def stop_apache(self, timer=2):
        time.sleep(timer)
        os.system("START \"\" "+self.xampp_path+"/apache_stop")

    def thread_start(self):
        self.permutation()
        for x in self.fragment_array():
            os.system(self.cmd_command(x))
            self.clean = "no"

    def start(self):
        self.permutation()
        os.system(self.cmd_command())



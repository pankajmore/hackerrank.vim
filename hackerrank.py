import requests
import time
import sys
import os.path

class HackerRank:
    def __init__(self,url,code="",ext=".py"):
        self.code = code
        self.ext = ext
        self.set_language()
        self.problem_url = url
        self.s = requests.session()
        self.payload = {'code' : self.code, 'language' : self.language}
        self.set_post_url()

    def set_post_url(self):
        rootUrl = "https://www.hackerrank.com/"
        l = self.problem_url.split("/")
        if l[3] == "challenges":
            contestUrl = "/contests/master/challenges/" + l[4]
        else:
            # it's a contest
            contestUrl = "/".join(l[3:])
        self.post_url = rootUrl + "/rest/" + contestUrl + "/compile_tests/"

    def set_language(self):
        if self.ext == ".py":
            self.language = "python"
        if self.ext == ".c":
            self.language = "c"
        # TODO : find out the language value for other exts

    def set_code(self,code):
        self.code = code

    def generate_payload(self):
        self.payload = {'code' : self.code, 'language' : self.language}

    def compile_and_test(self):
        self.generate_payload()
        self.r = self.s.post(self.post_url, params=self.payload)
        if self.r.status_code == 404:
            return "NOT_FOUND"
        j = self.r.json()
        self.submission_id = j['model']['id']
        self.get_url = self.post_url + "/" + str(self.submission_id)
        self.rr = self.s.get(self.get_url, cookies = self.s.cookies)
        return self.rr

    def fetch(self):
        if self.r.status_code == 404:
            return
        self.rr = self.s.get(self.get_url, cookies = self.s.cookies)
        self.res = self.rr.json()
        if self.res['model']['status'] == 0:
           time.sleep(1)
           self.fetch()
        else:
            return

    def compiler_message(self):
        return self.res['model']['compilemessage']

    def testcase_message(self):
        return self.res['model']['testcase_message']

    def expected_output(self):
        return self.res['model']['expected_output']

    def stdin(self):
        return self.res['model']['stdin']

    def stdout(self):
        return self.res['model']['stdout']

    def dump(self):
        cm = self.compiler_message()
        tm = self.testcase_message()
        eo = self.expected_output()
        stdin = self.stdin()
        stdout = self.stdout()
        s = ""
        for i in range(len(tm)):
            s += (cm + "\n")
            s += ("Testcase# " + str(i) + "\n")
            s += ("Sample Input:\n\n")
            s += (stdin[i])
            s += ("\n")
            s += ("Your Output:\n\n")
            s += (stdout[i])
            s += ("\n")
            s += ("Expected Output:\n\n")
            s += (eo[i])
            s += ("\n\n")
            s += ("Compiler Message:\n")
            s += (tm[i])
            s += ("\n")
            print(s)
            return s

    def run(self):
        if self.compile_and_test() == "NOT_FOUND":
            return "404 : NOT_FOUND"
        self.fetch()
        return self.dump()

if __name__=="__main__":
    url = sys.argv[1]
    codefile = sys.argv[2]
    ext = os.path.splitext(codefile)[1]
    code = open(codefile).read()
    h = HackerRank(url,code,ext)
    h.run()

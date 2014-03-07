import requests
import time

class HackerRank:
    def __init__(self,url):
        self.code = ""
        self.language = "python"
        self.problem_url = url
        self.s = requests.session()
        self.payload = {'code' : self.code, 'language' : self.language}
        self.post_url = url

    def set_language(self, lang):
        self.language = lang

    def set_code(self,code):
        self.code = code

    def generate_payload(self):
        self.payload = {'code' : self.code, 'language' : self.language}

    def compile_and_test(self):
        self.generate_payload()
        self.r = self.s.post(self.post_url, params=self.payload)
        if self.r.text == None:
            print "BUG"
        j = self.r.json()
        self.submission_id = j['model']['id']
        self.get_url = self.post_url + "/" + str(self.submission_id)
        self.rr = self.s.get(self.get_url, cookies = self.s.cookies)
        return self.rr

    def fetch(self):
        self.rr = self.s.get(self.get_url, cookies = self.s.cookies)
        self.res = self.rr.json()

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
            s += ("Testcase# " + str(i) + "\n")
            s += ("Sample Input")
            s += (stdin[i])
            s += ("\n")
            s += ("Your Output:\n")
            s += (stdout[i])
            s += ("\n")
            s += ("Expected Output:\n")
            s += (eo[i])
            s += ("\n")
            s += ("Compiler Message:\n")
            s += (tm[i])
            s += ("\n")
            print(s)
            return s

    def run(self):
        self.compile_and_test()
        time.sleep(10)
        self.fetch()
        return self.dump()

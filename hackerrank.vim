function! HackerRank()
python << endPython

import sys,vim
sys.path.append(vim.eval("expand('<sfile>:p:h')"))
from hackerrank import *

h = HackerRank("https://www.hackerrank.com/rest/contests/overnite2013/challenges/atul-and-christmas-tree/compile_tests/")

def create_new_buffer(file_name, file_type, contents):
    vim.command('rightbelow vsplit {0}'.format(file_name))
    vim.command('normal! ggdG')
    vim.command('setlocal filetype={0}'.format(file_type))
    vim.command('setlocal buftype=nowrite')
    vim.command('call append(0, {0})'.format(contents))

out = h.run()

def make_results_buffer(out):
    buf = vim.current.buffer
    code = "".join(buf)
    h.set_code(code)
    contents = [out]
    create_new_buffer("Results", "txt", contents)

make_results_buffer(out)

endPython
endfunction

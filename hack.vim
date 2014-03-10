function! HackerRank(url)
    " Get the bytecode.
    let bytecode = system("python2 hackerrank.py " . a:url . " " . bufname("%") . " 2>&1")

    " Open a new split and set it up.
    rightbelow vsplit __HackerRank_Results__
    normal! ggdG
    setlocal filetype=potionbytecode
    setlocal buftype=nofile

    " Insert the bytecode.
    call append(0, split(bytecode, '\v\n'))
endfunction

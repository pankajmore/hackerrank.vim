function! HackerRank(url)
    let results = system("python hackerrank.py " . a:url . " " . bufname("%") . " 2>&1")
    " Open a new split and set it up.
    rightbelow vsplit __HackerRank_Results__
    normal! ggdG
    setlocal filetype=results
    setlocal buftype=nofile
    call append(0, split(results, '\v\n'))
endfunction

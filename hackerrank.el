(defun hackerRank-compile-and-test (url)
  (interactive "sEnter the url : ")
  (async-shell-command (concat "python /home/pankajm/prog/hackerrank.vim/hackerrank.py " url " " (buffer-file-name))))

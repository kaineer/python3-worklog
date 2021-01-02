Scenarios list
--------------

 * Tasks
   * List tasks
   * Add task
     [should add week number and task id]
   * Edit task
   * Remove task
   * Label task as complete
   * Label task as cancelled
   * Label task as current
 * Notes
   * Add note
     [should add timestamp for note]
   * Edit note
   * Remove note
   * Note fields
     * ? branch
     * ? commit sha
     * ? note label: todo, note, done
     * comment

Commands
--------

$ wl task add ["Task title"]
$ wl task ls
$ wl task commit [task.id] sha
$ wl task branch [task.id] branch.name
$ wl task edit [task.id]
$ wl task [current] task.id
$ wl task done [task.id]
$ wl task cancel [task.id]
$ wl task rm [task.id]

$ wl note add [task.id] ["Note content"] ;; здесь было бы неплохо брать содержимое из последнего коммита
;; для этого можно будет прочитать `.git/COMMIT_EDITMSG`
;;
$ wl note rm [note.id]
$ wl note edit [note.id]

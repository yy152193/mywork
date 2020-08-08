# copy vimrc to ~/.vimrc
    1. YouCompleteMe 
        a. MANUAL install bcuz of submodule 
        b. For cmake/gnu/ninja, goto YCM GIT to know how to generate COMPILATION DATABASE
        b. For other compiler, cp/link YouCompleteMe/third_party/ycmd/.ycm_extra_conf.py \
           to WORKDIRECTORY and add "find . -name include" to FLAGS
    2. run :BundleInstall in vim

# zsh
    1. git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
    2. cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
    3. chsh -s $(which zsh)
    4. fix ~/.zshrc ZSH_THEME="candy"
    5. fix ~/.oh-my-zsh/themes/candy.zsh-theme
        PROMPT=$'%{$fg_bold[green]%}%n@%m %{$reset_color%}%{$fg[white]%}[%~]%{$reset_color%} $(git_prompt_info) %{$fg[red]%}$%{$reset_color%} '

#tmux
    1. apt install tmux

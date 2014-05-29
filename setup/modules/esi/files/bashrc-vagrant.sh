# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

if [[ $- == *i* ]]
then
    sudo iptables -I INPUT 5 -i eth0 -p tcp --dport 8000 -m state --state NEW,ESTABLISHED -j ACCEPT
    sudo su esi
fi

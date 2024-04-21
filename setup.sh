#!/usr/bin/env bash

# bash-completion
#source <(kubectl completion bash)
source ~/.kube/kubectl_autocompletion
# change PS1 to show current context of pwd without absolute path
result=${PWD##*/}          # to assign to a variable
#result=${result:-/}        # to correct for the case where PWD=/
#printf '%s\n' "${PWD##*/}"

export PS1='🔥 ${PWD##*/}: '

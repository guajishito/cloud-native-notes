#!/bin/bash

echo '==========$*=========='
for para in "$*"
# $*中的所有参数看成是一个整体，所以这个or循环只会循环一次
do
    echo $para
done

echo '==========$@=========='
for para in "$@"
# $@中的每个参数都看成是独立的，所以"$@"中有几个参数，就会循环几次
do
    echo $para
done
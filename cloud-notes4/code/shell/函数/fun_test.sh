#!/bin/bash

function add(){
        s=$[$1 + $2]
        echo "和："$s
}

read -p "请输入第一个整数：" a
read -p "请输入第二个整数：" b

add $a $b
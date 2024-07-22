#!/bin/bash

read -p "Top interview 150 문제이름 작성 바랍니다 :" title

if [ -z "$title" ]; then
  echo "문제이름을 작성해주세요~~!!!!!"
  exit 100
fi

format_date=$(date +%y%m%d)
folder_name="[${format_date}] ${title}"
folder_path="./Top Interview 150/${folder_name}"  

if [ -d "${folder_path}" ]; then
    echo "이미 존재하는 폴더입니다."
else 
    mkdir "${folder_path}"
    echo "~~~폴더 생성 완료~~~"
fi






#!/bin/bash
touch file1
mkdir dirA
mkdir ./dirA/dirC
touch -a -d '1 Nov 2018 12:34' ./dirA/dirC/file4
touch -a -d '1 Nov 2018 12:34' ./dirA/dirC/file5
mkdir ./dirA/dirC/dirD
touch -a -d '1 Nov 2018 12:34' ./dirA/dirC/dirD/file8
touch ./dirA/dirC/dirD/file6
touch -a -d '1 Nov 2018 12:34' ./dirA/dirC/dirD/file7
mkdir ./dirA/dirE
touch -a -d '1 Nov 2018 12:34' ./dirA/dirE/file9
touch -a -d '1 Nov 2018 12:34' ./dirA/file2
touch -a -d '1 Nov 2018 12:34' ./dirA/file3
mkdir ./dirB
touch ./dirB/file10
mkdir ./dirB/dirF
touch -a -d '1 Nov 2018 12:34' ./dirB/dirF/file11
touch -a -d '1 Nov 2018 12:34' ./dirB/dirF/file12
mkdir ./dirB/dirF/dirG
touch -a -d '1 Nov 2018 12:34' ./dirB/dirF/dirG/file13

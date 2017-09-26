#!/bin/bash
for i in seq'3 10';
do
	python3.4 main.py
	mv report.log report_$i.log
	mv report_$i.log logs/
done
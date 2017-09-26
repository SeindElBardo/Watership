#_##!/bin/bash
#_##eX_1 Conejos y lobos cuidan a sus descendientes DONE
#_#for i in `seq 1 10`;
#_#do
#_#	python3.4 EX_1.py > logs/EX_1/results_$i.log
#_#	echo finalizado experimento 1_$i
#_#done 
#_#
#_##EX_2 conejos y lobos se mueven si no son felices DONE
#_#for i in `seq 1 10`;
#_#do
#_#	python3.4 EX_2.py > logs/EX_2/results_$i.log
#_#	echo finalizado experimento 2_$i
#_#done

#EX_3 Evolución de la población respecto al limite de plantas.
for i in `seq 7 10`;
do
	time python3.4 EX_3.py > logs/EX_3/results_$i/results.log
	mv tierra1.log logs/EX_3/results_$i/
	mv tierra2.log logs/EX_3/results_$i/
	mv tierra3.log logs/EX_3/results_$i/
	mv tierra4.log logs/EX_3/results_$i/
	echo finalizado experimento 3_$i
done

#EX_4 Evolución del acervo genetico en todas las poblaciones y Grafico de felicidad DONE
#_#for i in `seq 1 10`;
#_#do
#_#	python3.4 EX_4.py > logs/EX_4/results_$i/results.log
#_#	mv plantas.log logs/EX_4/results_$i/
#_#	mv conejos.log logs/EX_4/results_$i/
#_#	mv zorros.log logs/EX_4/results_$i/
#_#	echo finalizado experimento 4_$i
#_#done
#_#
#_##EX_5 Evolución del acervo con individuos mal preparados DONE
#_#for i in `seq 1 10`;
#_#do
#_#	python3.4 EX_5.py > logs/EX_5/results_$i/results.log
#_#	mv plantas.log logs/EX_5/results_$i/
#_#	mv conejos.log logs/EX_5/results_$i/
#_#	mv zorros.log logs/EX_5/results_$i/
#_#	echo finalizado experimento 5_$i
#_#done
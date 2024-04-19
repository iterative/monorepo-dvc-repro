N=100

for i in $( seq 0 $N); do
    mkdir $i
    cp script.py $i/script.py
    cp dvc.yaml $i/dvc.yaml
    echo " " >> script.py
    echo "print('$RANDOM-$RANDOM')" >> $i/script.py
    echo "seed: $RANDOM" > $i/params.yaml
done


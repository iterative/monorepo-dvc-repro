N=$1

for i in $( seq 1 $N); do
    mkdir -p project-$i
    cp script_template.py project-$i/script.py
    cp dvc_template.yaml project-$i/dvc.yaml
    echo "print('$RANDOM-$RANDOM')" >> project-$i/script.py
    echo "seed: $RANDOM" > project-$i/params.yaml
done


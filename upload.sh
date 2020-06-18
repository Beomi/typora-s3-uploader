BASEDIR=$(dirname $0)
echo $@ > log.log
$BASEDIR/venv/bin/python $BASEDIR/upload.py "$@"

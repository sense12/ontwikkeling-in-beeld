projectname=app
path=$(PYTHONPATH)

all:
	$(warning 'there is no default make target')

start:
	gunicorn -w 2 --daemon run:app --bind 127.0.0.1:8000 --pid /tmp/gunicorn.pid


stop:
	kill -QUIT `cat /tmp/gunicorn.pid` && echo "stopped" || echo "failed"
clean: stop
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

docs:
	export PYTHONPATH=`pwd` && \
        cd docs && make clean html && \
        export PYTHONPATH=${path}

pep8:
	pep8 --ignore E501 --show-source -r ${projectname} && echo "All good!"

unittest:
	clean-pyc
	coverage erase
	SETTINGS_PATH='.' coverage run --include "${projectname}*" --omit "*test*" -m unittest2 discover
	coverage report
	coverage html -d docs/coverage/

test:
	pep8 unittest

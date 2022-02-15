This is a website test written in python and the webtesting framework selenium.

The goal for this test was to work in docker and docker swarm, next to the website container itself

Its also possible to let it run on your windows or mac device (I also have configuration variables for this use in the configfile.yaml)

When the test is started, logs will be  created depending on your configured logging level in the configfile.yaml

If you want to run the script locally outside of an container make shure to have docker, python, chrome, chromedriver and the python modules: selenium and pyyaml installed
(the dependencies will otherwise be automatically installed within the docker container)

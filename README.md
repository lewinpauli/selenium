This is a website test written in python and the webtesting framework selenium

The goal for this test was to work in docker and docker swarm, next to the website container itself

When an error occours the website test will end immediately (then take a look at the logfiles)

Its also possible to let it run on your windows or mac device (I also have configuration variables for this in the configfile.yaml)

When the test is started, logs will be created depending on your configured logging level in the configfile.yaml

If you want to run the script locally outside of an container make shure to have docker, python, chrome, chromedriver and the python modules: selenium and pyyaml installed
Also take a look at the configfile.yaml an the part for your operating system
(The dependencies will otherwise be automatically installed within the docker container)

My goal was it to write the script as universal as possible so you can edit it for your website

I also recommend to take a look at seleniumbase and the browser-extension katalon. With this you can record your own website behaviour and import it in seleniumbase, create visual website tests and much more, but for my usecase the website was not compatible (https://github.com/seleniumbase/SeleniumBase)

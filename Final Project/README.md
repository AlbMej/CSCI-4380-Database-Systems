# Database Systems Final Project Spring 2019

## Contributors
* Tyler Beckmann '19
* Leslie Chase '19
* Alberto Mejia '20
* Nathan Strelser '19

## Setup

You need to click on the links in datasets.txt, then click export and export as csv

Go into psql terminal and type:
<pre>
	psql -U postgres -h localhost postgres
</pre>
Run the following commands:
<pre>
	Create database project;
	Create user crime with password 'crime';
	Grant all privileges on database project to crime;
</pre>
Then run:
<pre>
	python3 load_data.py
</pre>
  
Apart from installing the `blessing` dependency described in `requirements.txt`, no additional setup is needed.
Run `pip3 install -r requirements.txt` to install. 

After that, you can now run the application through the following command

`python3 interface.py`

After running the command, you will see a command line interface of which you can navigate through to see the results of our project. 

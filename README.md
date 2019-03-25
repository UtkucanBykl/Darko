## Darko



### Why name is Darko ?

Because Donnie Darko is my favorite movie character.

#### What is Darko ?

<p>Darko is a lightweight key-value store. Also use graph tech so dont repeat common data.</p>

### Why use Graph ?

Because, we usually use to common value for each keys.
Like 
````
john:doe
jane:doe
doe:george
````
So think about it, Why we get memmory address every each 'doe'.


### Usage 


First,run project
````bash
git clone https://github.com/UtkucanBykl/Darko.git
cd Darko/Darko
python run.py
`````
If you want close the wal(Write Ahead Log) or change wal directory
````python
from config import Config
config = Config.get_config()
config.wal = False
config.wal_path = '../'
`````



For create key-value
````
http://127.0.0.1:12345/create?sentence=key:value
````
Also you can create multiple
````python
http:127.0.0.1:12345/create?sentence=key:value&sentence=value:key
````

For delete key-value
````
http://127.0.0.1:12345/delete?sentence=key:value
````

For retrieve node
````
http://127.0.0.1:12345/nodes
````

For get value of key
````
http://127.0.0.1:12345/<key_name>
````



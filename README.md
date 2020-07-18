# Portfolio_v2

This is the second version of my personal portfolio website. It includes a blog.
## Tools and Technologies
 * HTML5, CSS3
 * Bootstrap
 * Django
 * Disqus (for comments)
 
### How to run
Clone or download the project. Then open the folder with Terminal/cmd.
Then run 
```bash
pip install -r requirements.txt
```
This will install all required files and libraries.

##### Add env file  
Create a new file named **env.py** and copy from **env-sample.py**. Change the values as necessary.

Now run these commands
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

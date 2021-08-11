## Personal YT API

### Functionalities

* Asynchronously fetch data (videos) using YouTube API after every 5 minutes and store the data in the database. The search query used to fetch data is `tech`).
* GET API (`/api/videos/`) to retrieve paginated response (videos) from the local database.
* SEARCH API (`/api/videos/search/?search=<search_query>`) to retrieve paginated response (videos) based on the search query on video title and description. The Search API also supports fuzzy matching/partial matching on video title and description.
* Support for multiple API keys.
* Dedicated dashboard for accessing and searching the videos (using the APIs created, called using AJAX). Accessible at `http://localhost:8000`.

  ![image](https://user-images.githubusercontent.com/39924567/128798648-ffa96aca-1911-4cc0-be2f-4ab017cbfde4.png)
* Paginated search results on the dashboard.


### Setting-up the project

  * Download and install Python 3.8
  * Download and install Git.
  * Clone the repository to your local machine `$ git clone https://github.com/garg3133/personal-yt-api.git`
  * Change directory `$ cd personal-yt-api`
  * Install virtualenv `$ pip install virtualenv`
  * Create a virtual environment `$ virtualenv env -p python3.8`  
  * Activate the env: `$ source env/bin/activate` (for linux) `> ./env/Scripts/activate` (for Windows PowerShell)
  * Install the requirements: `$ pip install -r requirements.txt`
  * Create a new file in the root directory of the repository with name `.env` and add the following content in it:
    ```
    YOUTUBE_DATA_API_KEYS = 'yt-api-key1,yt-api-key2,...'
    ```  
  * Make migrations `$ python manage.py makemigrations`
  * Migrate the changes to the database `$ python manage.py migrate`
  * Create admin `$ python manage.py createsuperuser`
  * Run the server `$ python manage.py runserver`
  * Install and start Redis on your PC.
  * Run celery worker `$ celery -A personal_yt_api worker --pool=solo -l INFO`
  * Run celery beat (task scheduler) `$ celery -A personal_yt_api beat -l INFO`

### Setting-up the project in docker

  * Clone the repository to your local machine `$ git clone https://github.com/garg3133/personal-yt-api.git`
  * Change directory `$ cd personal-yt-api`
  * Create a new file in the root directory of the repository with name `.env` and add the following content in it:
    ```
    YOUTUBE_DATA_API_KEYS = 'yt-api-key1,yt-api-key2,...'
    ```
  * Run migrations `docker-compose run web python manage.py migrate`
  * Build the docker image `docker-compose build`
  * Run the docker image `docker-compose up`
  * The server will start at default port (8000), head over to your web browser to test at `http://localhost:8000`.

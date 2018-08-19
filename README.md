# Dalton Scraping

This python script extract the vehicle data of the [Dalton/Toyota](https://daltontoyota.com.mx/) webpage
and saves the results into a database (postgres as default). 

## Configure

Consider configuring the app according to your use-case. 
The configuration of this app is contained in a `.env` file in the 
`config` package. 

**Debian based OS** 

1. Create the enviorment variables.
    * Create the file: `cp config/.env.example config/.env`
    * Edit the variables: `vim config/.env`
2. Create and activate a virtual environment.
    * Create: `virtualenv --python=python3 venv`
    * Activate: `source venv/bin/activate`
3. Install the requirements.
    * Install: `pip install -r requirements.txt`

## Run 

Run the app following these steps: 
1. Activate the virtualenv.
    * Activate: `source venv/bin/activate`
2. Run the `main.py` file.
    * Run: `python main.py`

## License

All rights are reserved to [chatbotmx](chatbotmx.com).

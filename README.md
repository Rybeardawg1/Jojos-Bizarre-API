# Jojos-Bizarre-API

Gonna make an NLP model that'll respond to API calls. Maybe make it into a Twitter bot too or something.. idk

## To Do:

### Get all Jojo script data<br>

[x] get scripts<br>
[] get better formatted scripts for NLP<br>
[] get manga data<br>

<blockquote>
Show: https://transcripts.foreverdreaming.org/viewforum.phpf=1721 <br>
https://en.wikiquote.org/wiki/JoJo%27s_Bizarre_Adventure <br>
Manga: picture-to-text scanner maybe? <br>
Manga: https://mangadex.org/title/136/jojo-s-bizarre-adventure-part-1-phantom-blood <br>
</blockquote>

### The API itself

[x] Make REST API that will call model when prompted and return quote when unprompted <br>
[] Flask is fucking slow so Rust...? <br>

### Learn about NLPs

[x] Understand NLP basics<br>
[x] Train jojo-gpt2<br>
[] Train a better one<br>

<blockquote>
Understand tokenization, stemming, and lemmatization <br>
Apply/practice concepts<br>
</blockquote>

### Hosting

<blockquote>
Domain: https://instantdomains.com/search?q=jojosbizarreapi <br>
https://www.heroku.com/ <br>
https://www.pythonanywhere.com/ <br>
https://www.digitalocean.com/ <br>
https://www.shuttle.rs/<br>
AWS? <br>
</blockquote>

### Running Development Server

Flask: <br>
python flask_api.py

Axum: <br>
python -m venv C:\Users\Rybeardawg1\AppData\Local\Programs\Python\Python39\Lib\venv <br>
set LIBTORCH_USE_PYTORCH=1 <br>
As of now, tch version 0.14.0 crate supports up to PyTorch 2.1.0. If you need to downgrade, use pip install torch==2.1.0<br>
cargo build <br>
cargo run <br>

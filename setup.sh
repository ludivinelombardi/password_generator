mkdir -p ~/.streamlit/
echo "
[general]n
email = "ludivine.lombardi@epitech.eu"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml
Langkah-langkah setup project flask
A. Virtual Environment

1. Buat folder project
2. Buat virtual env (2)
   - python -m venv .venv
   - poetry config virtualenvs.in-project true
3. Masuk ke dalam virutal env
   - [venv folder]\Script\activate
4. Install depedency/package
5. Check packacge yang di install
   - pip list

B. Package Manager Poetry

1. pip install poetry
2. Tambahkan poetry
   - poetry init -> jika sudah ada projectnya
   - poetry new [nama project] -> jika baru akan membuat project\* (1)
3. install depedency di poetry
   - poetry add flask
4. Run development
   - poetry run flask --app .\app\ run

C. Debug mode

1. install poetry .env
   - poetry add poetry-dotenv-plugin
2. create file .env
   - FLASK_DEBUG = TRUE
   - FLAS_ENV = development

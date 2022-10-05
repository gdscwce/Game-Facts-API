<h1 align=center> Game Facts API </h1>
<h1 align=center>Helps users fetch facts about any games to integrate into their own games, quizzes or applications.</h1>
<p align="center">
  <img src="https://img.shields.io/github/license/gdscwce/Game-Facts-API?style=for-the-badge&logo=appveyor">
  <img src="https://img.shields.io/github/stars/gdscwce/Game-Facts-API?style=for-the-badge&logo=appveyor">
  <img src="https://img.shields.io/github/forks/gdscwce/Game-Facts-API?style=for-the-badge&logo=appveyor">
  <img src="https://img.shields.io/github/issues/gdscwce/Game-Facts-API?style=for-the-badge&logo=appveyor">
  </p>

<br>

## Tech Stack 💻
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

---

<br/>

## Setting up Virtual Environments



<br>

**Venv** is a tool that creates an isolated environment separate from other projects. Creating a virtual environment allows us to work on a Python project without affecting other projects that also use Python and their dependencies.

<br>

Install **pip** first
```bash
sudo apt-get install python3-pip
```

Then install **venv**
```bash
sudo apt install python3-venv
```

Now create a virtual environment 
```bash
python3 -m venv {name_of_virtual_environment}
```
  
Active your virtual environment:    
```bash
source {name_of_virtual_environment}/bin/activate
```

Install all dependencies from ```requirements.txt```
```
pip3 install -r requirements.txt
```

To deactivate:
```
deactivate
```

Run the project using ```uvicorn``` by executing the following command
```
uvicorn main:app --reload
```

<br>

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.




## Endpoints

| Method   |      Path      |  Description |
|----------|:-------------:|------:|
| **GET** | `/fact/game={games}?limit={limit}` | Fetch facts about one or multiple games. |
| **GET** | `/fact/random?limit={limit}` | Fetch facts(s) about a random game. |

#### Games must be seperated by "&"
----

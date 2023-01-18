# Social Coach - backend

### inicialização do ambiente 

>Step-by-step setup tutorial of the Marketplace's backend.
>
>The tutorial assumes that the user's OS is UNIX based, **if not make the appropriate changes and select the correct OS in the documentation**. 
>
>_If running on Windows remember to enable Hyper-V and virtual environments._ 

#### Pre Requiments
* [Docker](https://docs.docker.com/engine/install/debian/)
> create docker group, _**you'll probably have to reboot after this**_.
```shell script
sudo groupadd docker
sudo usermod -aG docker $USER
```
* [Docker Compose](https://docs.docker.com/compose/install/)

#### Git clone
>[Clone the project](https://github.com/thinkideaapp/44express-backend) and go to the chosen directory, for example:
```shell script
git clone https://github.com/thinkideaapp/sensi-backend-init.git
cd ~/sensi-backend-init
```

#### GitHub's registry login

> See how to generate a GitHub token: * [Personal access token with access to GitHub packages](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

```shell script
echo <your-personal-access-token> | docker login docker.pkg.github.com --username <your-username> --password-stdin
```

#### Pycharm Integration
>It's possible to run your container and debug with it using PyCharm.

* Build, Execution, Deployment
>To enable docker in PyCharm go to: File>Settings>Build,Execution,Deployment>Docker
> ![Enable Docker](app/static/documentation/enable_docker.png)
>Click in the **+** icon and use the default settings

* Project Interpreter
>We need to create a remote python interpreter, basically the python interpreter running inside our container.
>
>Go to File>Settings>Project: 44express-backend>Python Interpreter
>
>Add a configuration clicking in the ![setting icon](app/static/documentation/setting_icon.png) icon and clicking on "Add" and configure it like so: ![Docker Compose Config](app/static/documentation/docker_compose_config.png)

* Run/Debug Configurations
>The final step in the setup is to configure the Run/Debug configuration, **create one using the Remote Interpreter**. ![Run/Debug Config](app/static/documentation/run_debug_config.png)

#### Deploy
>First deploy
```shell script
docker-compose up --build
```
>Regular Deploy
```shell script
docker-compose up
 ```
>Once the project is up and running just debug the application by clicking in the debug icon ![debug icon](app/static/documentation/pycharm_debug_icon.png)
>
>>You ready to go!

* Redeploy restoring all databases
```shell script
bash init.sh
```

#### Migrations and DB
>To make a migration on the database use:
```shell script
docker-compose exec api flask db migrate -m"<your message>"
```
>if there's a conflict with the migration heads, run:
```shell script
bash db-merge.sh
``` 
>If you wish to update the db dupms, use:
```shell script
bash db-dump
```

### autenticação no swagger

> cole o link no seu navergador após a inicialização do docker-compose up --build:
``` shell script
http://127.0.0.1:4130/docs#/ 
```

> click no botão Authorize

![Captura de tela de 2022-08-03 10-31-30](https://user-images.githubusercontent.com/50378596/182626006-7c4064d6-5446-44c3-ae1a-7597ddf9eb08.png)
<br>

>coloque a key informada a baixo no "api_key (apiKey)":

b2ZlcnRhcGxheXVzZXI6b2ZlcnRhcGxheXBhc3N3b3Jk


![Captura de tela de 2022-08-03 10-31-45](https://user-images.githubusercontent.com/50378596/182636158-bf5ea867-5b04-4f35-a2c4-3b7e1e7d869d.png)
<br>

>click em authorize

![Captura de tela de 2022-08-03 11-41-32](https://user-images.githubusercontent.com/50378596/182647536-efc0fd73-3300-4b67-ae16-18f2c88c40f7.png)
<br>

>Entre na rota Token

![Captura de tela de 2022-08-03 11-40-43](https://user-images.githubusercontent.com/50378596/182647841-db1a977d-41a0-4a40-86fe-a008161f52c2.png)
<br>

>click em Try it out

![Captura de tela de 2022-08-03 11-42-01](https://user-images.githubusercontent.com/50378596/182648173-a65d7154-4695-4741-b632-e0dcfcf46d2a.png)
<br>

>click em execute

![Captura de tela de 2022-08-03 11-42-16](https://user-images.githubusercontent.com/50378596/182648375-147dd514-e345-4caa-949e-ea0c38b80e32.png)
<br>

>copie o jwt sem as "aspas" gerado pelo rota token e cole no jwt  (http, Bearer). Pronto já pode visualizar as rotas

![Captura de tela de 2022-08-03 11-46-00](https://user-images.githubusercontent.com/50378596/182648489-11eca162-3147-438a-95de-69dbcbe47ee5.png)
<br>


### Relatorio de tests

docker-compose exec api python -m pytest "tests" -p no:warnings --cov="app"


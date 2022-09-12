# Sexist-speech Recognition

Ce repository a été créé dans le cadre d’une formation en Data Science dispensée par l’organisme de formation [Le Wagon](https://www.lewagon.com/) par [Camille](https://github.com/CamillePe), [Chen](https://github.com/sunc33), [Anatole](https://github.com/Anatsoul) et [Liam](https://github.com/Liamabra) .

## Les objectifs de ce projet étaient :

* Créer une base consolidée (à l’aide de bases de données labellisées par des chercheurs) pour entraîner le modèle de Deep Learning à la reconnaissance de messages sexistes. Pour éviter les doublons une fois les bases assemblées, nous avons effectué une étape de nettoyage et suppression des “duplicates”.


* Créer une base d’analyse en vue de la démonstration des capacités du modèle “en conditions réelles”. Nous avons utilisé les API de Twitter et Reddit pour récupérer des posts, commentaires… Un fois le corpus créé, nous avons testé le modèle de Deep learning dessus.

* Créer un modèle de deep learning capable de détecter un message sexiste sur les réseaux sociaux en utilisant le principe du transfert learning. Nous avons figé les poids d’un modèle de base roBERTa formé sur environ 58 millions de tweets et affiné pour l'analyse des sentiments. Puis, nous avons ajouté une couche de Dense que nous avons entraîné spécifiquement à la reconnaissance de messages sexistes en ligne à l’aide de la base consolidée.


* Présenter les capacités et les limites de ce modèle à l’aide d’une démonstration ludique que nous avons créée sur Streamlit en vue du Démo day en live chez [Le Wagon](https://github.com/lewagon). Ce dernier n’est pas partagé sur ce repository.

<em>Disclaimer</em> : Ce projet est le résultat d’un exercice à visée pédagogique. Il a été réalisé en 10 jours et nécessite donc des améliorations.

## Sources :

* Pour la création de la base consolidée :
`*[“The 'Call me sexist but' Dataset (CMSB)”](https://search.gesis.org/research_data/SDN-10.7802-2251?doi=10.7802/2251), Samory Mattia, GESIS - Leibniz-Institut für Sozialwissenschaften.`
`*[“]AI ML NIT Patna @ TRAC - 2: Deep Learning Approach for Multi-lingual Aggression Identification”](https://docs.google.com/forms/d/e/1FAIpQLSesLjGKLQlE3dmQNZUEl5QJVno7NngeLTP9XvIMCvpZu7sXNg/viewform), Kirti Kumari & Jyoti Prakash Singh, National Institute of Technology Patna.`
`*[“North American Chapter of the Association for Computaitional Linguistics(NAACL)”](https://github.com/zeeraktalat/hatespeech), [Zeerak Talat](https://github.com/zeeraktalat).`

* Pour la création des datasets d’analyse : Reddit Social Media & Twitter.

* Pour le modèle de base [roBERTa](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment).


### Startup the project :

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for sexist_speech_recognition in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/sexist_speech_recognition`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "sexist_speech_recognition"
git remote add origin git@github.com:{group}/sexist_speech_recognition.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
sexist_speech_recognition-run
```

### Install :

Go to `https://github.com/{group}/sexist_speech_recognition` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/sexist_speech_recognition.git
cd sexist_speech_recognition
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
sexist_speech_recognition-run
```

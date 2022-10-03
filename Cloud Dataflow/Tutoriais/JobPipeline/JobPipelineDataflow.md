# Job Pipeline Dataflow - Batch
Executando JobPipeline-v0.py no ambiente Cloud via Dataflow.

<br>

## PASSO 1 - Criar Bucket
Dados da bucket:
* Região: us-central1
* Tipo de Bucket: standard
```bash
gsutil mb -p data-labs-358422 -c standard -l us-central1 -b on gs://isidoro_flowdata
```
> * *Testando com upload do arquivo JobPipeline-v0.py direto do GitHub*
> * *Testando com upload do dataset futebol.csv direto na Bucket*
<br>

## PASSO 2 - Ativar e Configurar Ambiente
* Instale o SDK do Cloud Dataflow com a versão Python 3.7
> No Cloud Shell digite o comando:
```bash
docker run -it -e DEVSHELL_PROJECT_ID=$DEVSHELL_PROJECT_ID python:3.7 /bin/bash
```
<br>

* Instale a versão mais rescente do Apache Beam
> No Cloud Shell digite o comando:
```bash
pip install 'apache-beam[gcp]'
```
<br>

## PASSO 3 - Execute a Pipeline
* Defina uma Variável de Ambiente Bucket para a Bucket que você criou.
> No Cloud Shell digite o comando:
```bash
BUCKET=gs://NOME_DA_SUA_BUCKET
```
<br>

* Execute o JobPipeline-v0.py
> No Cloud Shell digite o comando:
```bash
python -m apache_beam.JobPipeline-v0 --project $DEVSHELL_PROJECT_ID \
  --runner DataflowRunner \
  --staging_location $BUCKET/staging \
  --temp_location $BUCKET/temp \
  --output $BUCKET/results/output \
  ```

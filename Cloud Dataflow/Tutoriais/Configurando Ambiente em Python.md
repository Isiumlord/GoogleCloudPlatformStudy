# Configurando Ambiente Cloud Dataflow em Python
Nesse tutorial iremos configurar um ambiente de desenvolvimento do Dataflow em Python.
<br>

## ESCOPO
* Instalar o SDK do Cloud Dataflow para Python;
* Executar um pipeline de exemplo usando o Console do Google Cloud Platform.
<br>

## ITENS NECESSÁRIOS
* Uma Bucket;
* SDK do Dataflow instalado com a versão Python 3.7;
* Apache Beam instalado no SDK do Dataflow;
* Código da Pipeline.
<br>

## FERRAMENTAS
* Google Cloud Platform;
* Cloud Shell;
* Cloud Storage;
* Cloud Dataflow.
<br>

## PASSO 1 - Ative o Cloud Shell no Console do Google Cloud Platform.
<br>

## PASSO 2 - Crie uma Bucket.
* Crie a Bucket por linha de comando com as condições: **Standard, Multi-Region us**.
> No Cloud Shell digite o comando:
```bash
gsutil mb -p ID_PROJETO -c TIPO_DE_SAVE -l REGIÃO_ZONA -b on gs://NOME_DA_BUCKET
```
*Não esqueça de editar os campos necessários*.

<br>

## PASSO 3 - Configure o Ambiente
* Instale o SDK do Cloud Dataflow com a versão Python 3.7
> No Cloud Shell digite o comando:
```bash
docker run -it -e DEVSHELL_PROJECT_ID=$DEVSHELL_PROJECT_ID python:3.7 /bin/bash
```
<br>

* Instale a versão mais rescente do Apache Beam.
> No Cloud Shell digite o comando:
```bash
pip install 'apache-beam[gcp]'
```
<br>

## PASSO 4 - Execute o wordcount.py
* Execute o `wordcount.py` com Apache Beam.
> No Cloud Shell digite o comando:
```bash
python -m apache_beam.examples.wordcount --output OUTPUT_FILE
```

*NOTA: Até aqui você instalou `google-cloud-dataflow`, mas está executando `wordcount` com `Apache_beam`. A razão para isso é que o Cloud Dataflow é uma distribuição do Apache Beam*.

<br>

* Liste os arquivos que estão em seu ambiente de nuvem local para obter o nome do `OUTPUT_FILE`.
> No Cloud Shell digite o comando:
```bash
ls
```
<br>

* Copie o nome do OUTPUT_FILE e o abra.
> No Cloud Shell digite o comando:
```bash
cat NOME_DO_OUTPUT_FILE
```
<br>

## PASSO 5 - Execute a Pipeline.
* Defina uma Variável de Ambiente Bucket para a Bucket que você criou.
> No Cloud Shell digite o comando:
```bash
BUCKET=gs://NOME_DA_SUA_BUCKET
```
<br>

* Execute o `wordcount.py` examples remotamente.
> No Cloud Shell digite o comando:
```bash
python -m apache_beam.examples.wordcount --project $DEVSHELL_PROJECT_ID \
  --runner DataflowRunner \
  --staging_location $BUCKET/staging \
  --temp_location $BUCKET/temp \
  --output $BUCKET/results/output \
  --region us-west1
  ```
  <br>
  
## PASSO 6 - Verifique a Execução do Trabalho e o seu Encerramento.
* No Menu Principal do Google Cloud Platform acesse Cloud Dataflow > Navegação;
* Visualize o Trabalho em andamento.
* Depois que todas as Caixas estiverem marcadas com o status de `Succeeded` você saberá que o trabalho terminou.
* Para ver os resultados vá no Menu Principal do Google Cloud Platform acesse Cloud Storage > Navegação;
* Clique no nome da sua Bucket;
* Nela haverá diversos diretórios com os resultados.

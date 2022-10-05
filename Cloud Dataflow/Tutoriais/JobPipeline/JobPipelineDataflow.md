# Job Pipeline Dataflow - Batch
Executando JobPipeline-v0.py no ambiente Cloud via Dataflow.

* Gerar Tamplate usando o código desenvolvido;
* Usar Template no Dataflow;
* Rodar a Pipeline.

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

## PASSO 2 - Criar Conta de Serviço Google
* IAM > Contas de Serviço > Criar Conta de Serviço > Dar Permissão `Dataflow Worker`

## PASSO 3 - Ativar e Configurar Ambiente
* Instale a versão mais rescente do Apache Beam
> No Cloud Shell digite o comando:
```bash
pip install 'apache-beam[gcp]'
```

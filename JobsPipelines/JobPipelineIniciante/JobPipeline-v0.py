{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM3Sjrxb4ZiV7q6odNKHdu0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Isiumlord/GoogleCloudPlatformStudy/blob/main/JobsPipelines/JobPipelineIniciante/JobPipeline-v0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "TAREFAS\n",
        "\n",
        "* Ignorar colunas não utilizáveis (deletar colunas) ✔\n",
        "* Ajustar campos de data (mudar disposição) ✔\n",
        "* Concatenações (juntar campos diversos: pode ser por junção simples de string, cálculo entre colunas ou cruzamento de dados) ✔\n",
        "* Domínio (padrão do cliente) - fazer \"De x Para\" com o padrão de campos da Dasa - Exemplo: Feminino para F) ✔\n",
        "\n",
        "DATASET TRABALHADO\n",
        "* Premier League Match Data (https://www.kaggle.com/datasets/evangower/premier-league-match-data)"
      ],
      "metadata": {
        "id": "2iE0RJsWYsGj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Instalando Apache Beam"
      ],
      "metadata": {
        "id": "7b1KSUhjjcmb"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "meGtpE7vjWqF"
      },
      "outputs": [],
      "source": [
        "!pip install apache-beam"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Importando Bibliotecas"
      ],
      "metadata": {
        "id": "lmKsQjFojhoE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import apache_beam as beam\n",
        "from apache_beam.io import ReadFromText\n",
        "import pandas as pd"
      ],
      "metadata": {
        "id": "NEN-oD01jhWy"
      },
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Declarando Variavel Global"
      ],
      "metadata": {
        "id": "zP4h6Alv2yBH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pipeline = beam.Pipeline()"
      ],
      "metadata": {
        "id": "q1MFazbQXtwp"
      },
      "execution_count": 40,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Criando Funções de Transformações em Pandas"
      ],
      "metadata": {
        "id": "39WXnHzDu3DM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "* Lendo o Arquivo .csv\n",
        "* Transformando-o em Dataframe\n",
        "* Transformando Coluna `Date` em `datetime`\n",
        "* Formatando a data para `dia/mês/ano`"
      ],
      "metadata": {
        "id": "OKxyK1HZ5-dQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def formatandoData(df):\n",
        "\n",
        "    # Lendo Arquivo\n",
        "    df = pd.read_csv(\"/content/futebol.csv\", sep=\",\")\n",
        "    \n",
        "    # Formatando data para `dia/mês/ano`\n",
        "    df['Date'] = pd.to_datetime(df.Date)\n",
        "    df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')\n",
        "\n",
        "    # Formatando data para `mês/dia/ano`\n",
        "    #df['Date'] = pd.to_datetime(df.Date)\n",
        "    #df['Date'] = df['Date'].dt.strftime('%m/%d/%Y')\n",
        "\n",
        "    return df"
      ],
      "metadata": {
        "id": "6l7NtWM_Wusc"
      },
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Excluindo Colunas: FTHG, FTAG, HTHG, HTAG, HTR, HST, AST, HF, AF, HC, AC, HY, AY, HR, AR"
      ],
      "metadata": {
        "id": "DQipuHlr3jBt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def excluirColunas(df):\n",
        "    df.drop([\"FTHG\",\n",
        "             \"FTAG\",\n",
        "             \"HTHG\",\n",
        "             \"HTAG\",\n",
        "             \"HTR\", \"HST\", \"AST\", \"HF\", \"AF\", \"HC\", \"AC\", \"HY\", \"AY\", \"HR\", \"AR\"], axis=1, inplace=True)\n",
        "\n",
        "    return df"
      ],
      "metadata": {
        "id": "m2fV62T2WukK"
      },
      "execution_count": 42,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Editando Dados da Coluna `FTR`"
      ],
      "metadata": {
        "id": "xDiMOr_i3nn-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def editandoDados(df):\n",
        "    df.loc[df.FTR == \"H\", [\"FTR\"]] = \"H-Editado\"\n",
        "    df.loc[df.FTR == \"A\", [\"FTR\"]] = \"A-Editado\"\n",
        "    df.loc[df.FTR == \"D\", [\"FTR\"]] = \"D-Editado\"\n",
        "\n",
        "    return df"
      ],
      "metadata": {
        "id": "lOSiM-IuxyHU"
      },
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Concatenando as colunas `HomeTeam` e `AwayTeam` em uma só coluna chamada `Combate`"
      ],
      "metadata": {
        "id": "3ApeG3z33psY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def concatenando(df):\n",
        "    df['Combate'] = df['HomeTeam'].map(str) + ' VS ' + df['AwayTeam'].map(str)\n",
        "    return df"
      ],
      "metadata": {
        "id": "5QR100ZkWuX7"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Transformando DataFrame em Dicionário (necessário para rodar no Job Pipeline)"
      ],
      "metadata": {
        "id": "BZQHUXhs4vGZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def dicionario(df):\n",
        "    df_dicionario = df.to_dict('records')\n",
        "    return df_dicionario"
      ],
      "metadata": {
        "id": "HByE10iAW6li"
      },
      "execution_count": 45,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Job Pipeline em Apache Beam"
      ],
      "metadata": {
        "id": "K3ajDbwRYmmj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "job = (\n",
        "    pipeline\n",
        "    |'Lendo Arquvio' >> beam.io.ReadFromText(\"/content/futebol.csv\", skip_header_lines=0)\n",
        "    |'Formatando Data' >> beam.Map(formatandoData)\n",
        "    |'Excluindo Colunas' >> beam.Map(excluirColunas)\n",
        "    |'Editando Dados' >> beam.Map(editandoDados)\n",
        "    |'Concatenando Colunas' >> beam.Map(concatenando)\n",
        "    |'Transformando Dataframe em Dicionario' >> beam.Map(dicionario)\n",
        "    |'Salvando Resultados em txt' >> beam.io.WriteToText(\"/content/resultados.txt\")\n",
        "    |\"Mostrar resultados\" >> beam.Map(print)\n",
        ")\n",
        "\n",
        "pipeline.run()"
      ],
      "metadata": {
        "id": "r8wwP3B9Wuz-"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
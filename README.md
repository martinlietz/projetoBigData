# Projeto Big Data

<img src="https://i.imgur.com/dBNsFcL.png" width="30%">


# Projeto final do Modulo de Big Data

# Data de Entrega: 
25/08/2021

email: matheus.domingos@live.com
slack: Matheus Oliveira

# Proposta:

Fazer análise dos resultados de partidas de futebol existentes no arquivo results.csv
O dataset foi retirado do desafio existente no kaggel.

https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017



| Campo Arquivo  | Campo Hive           | Tipo    | Descrição                                                              |
|----------------|----------------------|---------|------------------------------------------------------------------------|
| date           | Data                 | date    | quando jogo ocorreu                                                    |
| home_teamName  | equipe_mandante      | string  | equipe da casa                                                         |
| away_teamName  | equipe_visitante     | string  | equipe visitante                                                       |
| home_scoreHome | gol_equipe_mandante  | int     | pontuação equipe da casa                                               |
| away_scoreAway | gol_equipe_visitante | int     | pontuação equipe visitante                                             |
| tournamentName | torneio              | string  | torneio                                                                |
| cityCity       | cidade               | string  | onde o jogo aconteceu                                                  |
| countryCountry | pais                 | string  | onde a partida ocorreu                                                 |
| neutralTRUE    | fora_pais            | boolean | se o jogo ocorreu fora do país da equipe da casa, FALSE caso contrário |


# Passos:


1- Importar o arquivo result.csv para o HDFS

2 - Criar uma tabela no Hive com o nome de resultado, onde seja possível realizar consultas
no arquivo result.csv.

O nome das colunas devem respeitar o tipo e a nomenclatura informada acima.
Executar uma query simples no HUE retornando as 5 primeiras linhas da tabela criada.

3 - Realizar análise utilizando Spark:

AJUDA: copiar o hive-site.xml para o conf do Spark.
```
sudo cp /etc/hive/conf/hive-site.xml /etc/spark/conf/
```
AJUDA: Para ler a tabela Hive e criar o dataframe, utilize o script abaixo:
```
from pyspark.sql import HiveContext
h = HiveContext(sc)
df = h.sql("select * from default.resultado")
```
Após a criação do dataframe, responda as questões abaixo.
* a - quantos registro existem no dataframe
* b - quantas equipes únicas mandantes existem no dataframe
* c - quantas vezes as equipes mandantes saíram vitoriosas
* d - quantas vezes as equipes visitantes saíram vitoriosas
* e - quantas partidas resultaram em empate
* f - a partir de um dataframe, crie uma tabela no Hive com o nome de partida_pais com o
* total de partida em cadas país
* g - utilizando o hive e a tabela partida_pais, em qual país teve mais partidas.

O que enviar:
* 1 - Print do ls com o arquivo no HDFS (hdfs.jpeg)
* 2 - Um arquivo chamado tabela.txt com o DDL de criação da tabela no HIVE.
* 3 - Print da query executada no HUE com os 5 primeiros registros da tabela (hue.jpeg)
* 4 - Um arquivo chamado resposta.txt com as respostas das 7 perguntas
* 5 - Um arquivo analise.py com os comandos executados para a análise no Spark.

**hive-site.xml**
```xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<configuration>

  <!-- Hive Configuration can either be stored in this file or in the hadoop configuration files  -->
  <!-- that are implied by Hadoop setup variables.                                                -->
  <!-- Aside from Hadoop setup variables - this file is provided as a convenience so that Hive    -->
  <!-- users do not have to edit hadoop configuration files (that may be managed as a centralized -->
  <!-- resource).                                                                                 -->

  <!-- Hive Execution Parameters -->
  
  <property>
    <name>hive.execution.engine</name>
    <value>spark</value>
    <description> Chooses execution engine. </description>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://127.0.0.1/metastore?createDatabaseIfNotExist=true</value>
    <description>JDBC connect string for a JDBC metastore</description>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>com.mysql.jdbc.Driver</value>
    <description>Driver class name for a JDBC metastore</description>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>hive</value>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>cloudera</value>
  </property>

  <property>
    <name>hive.hwi.war.file</name>
    <value>/usr/lib/hive/lib/hive-hwi-0.8.1-cdh4.0.0.jar</value>
    <description>This is the WAR file with the jsp content for Hive Web Interface</description>
  </property>

  <property>
    <name>datanucleus.fixedDatastore</name>
    <value>true</value>
  </property>

  <property>
    <name>datanucleus.autoCreateSchema</name>
    <value>false</value>
  </property>

  <property>
    <name>hive.metastore.uris</name>
    <value>thrift://127.0.0.1:9083</value>
    <description>IP address (or fully-qualified domain name) and port of the metastore host</description>
  </property>
</configuration>


```

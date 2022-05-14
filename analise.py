from pyspark.sql import HiveContext, SQLContext
contexto = HiveContext(sc) 
banco = contexto.table("projeto.resultados")
df = contexto.sql("SELECT * FROM projeto.resultados")
# a - quantos registro existem no dataframe
df.count() # 43182
# b - quantas equipes únicas mandantes existem no dataframe
df.select('home_team').distinct().count() # 307
# c - quantas vezes as equipes mandantes saíram vitoriosas
df.filter(df.home_score>df.away_score).count() # 21004
# d - quantas vezes as equipes visitantes saíram vitoriosas 
df.filter(df.home_score<df.away_score).count() # 12223
# e - quantas partidas resultaram em empate 
df.filter(df.home_score==df.away_score).count() #9955
# df - a partir de um dataframe, crie uma tabela no Hive com o nome de partida_pais com o total de partida em cadas país
dfCount = df.groupBy("country").count()
dfCount.show()
dfCount.saveAsTable("projeto.partida_pais")
# g - utilizando o hive e a tabela partida_pais, em qual país teve mais partidas
sqlContext.sql("USE projeto")
sqlContext.sql("SELECT * FROM projeto.partida_pais ORDER BY count DESC").head(1)
# United States com 1236 jogos.
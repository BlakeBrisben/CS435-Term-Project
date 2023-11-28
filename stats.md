make[1]: Entering directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
shell_scripts/clean_data.sh
Deleted /TP/output/cleaned_data
start of the data cleaning process
Input File: /TP/input/	Output File: /TP/output/cleaned_data
root
 |-- _c0: string (nullable = true)
 |-- app_id: string (nullable = true)
 |-- app_name: string (nullable = true)
 |-- review_id: string (nullable = true)
 |-- language: string (nullable = true)
 |-- review: string (nullable = true)
 |-- timestamp_created: string (nullable = true)
 |-- timestamp_updated: string (nullable = true)
 |-- recommended: string (nullable = true)
 |-- votes_helpful: string (nullable = true)
 |-- votes_funny: string (nullable = true)
 |-- weighted_vote_score: string (nullable = true)
 |-- comment_count: string (nullable = true)
 |-- steam_purchase: string (nullable = true)
 |-- received_for_free: string (nullable = true)
 |-- written_during_early_access: string (nullable = true)
 |-- author.steamid: string (nullable = true)
 |-- author.num_games_owned: string (nullable = true)
 |-- author.num_reviews: string (nullable = true)
 |-- author.playtime_forever: string (nullable = true)
 |-- author.playtime_last_two_weeks: string (nullable = true)
 |-- author.playtime_at_review: string (nullable = true)
 |-- author.last_played: string (nullable = true)

Total number of observations before cleaning: 40848659
Total number of observations after cleaning: 7240395
+--------------------+--------------------+-----------+
|            app_name|              review|recommended|
+--------------------+--------------------+-----------+
|The Witcher 3: Wi...|One of the best R...|       True|
|The Witcher 3: Wi...|good story, good ...|       True|
|The Witcher 3: Wi...|            dis gud,|       True|
|The Witcher 3: Wi...|favorite game of ...|       True|
|The Witcher 3: Wi...|Why wouldn't you ...|       True|
|The Witcher 3: Wi...|Isn't Geralt hot ...|       True|
|The Witcher 3: Wi...|Very Fun, Would p...|       True|
|The Witcher 3: Wi...|The only thing bi...|       True|
|The Witcher 3: Wi...|better than cyber...|       True|
|The Witcher 3: Wi...|We all know you'l...|       True|
+--------------------+--------------------+-----------+
only showing top 10 rows

end of the data cleaning process
make[1]: Leaving directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
make[1]: Entering directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
shell_scripts/resample_data.sh
Deleted /TP/output/resampled_data
start of the resampling process
Input File: /TP/output/cleaned_data	Output File: /TP/output/resampled_data
Total number of observations before resampling: 7240395
+--------------------+--------------------+-----------+
|            app_name|              review|recommended|
+--------------------+--------------------+-----------+
|The Witcher 3: Wi...|One of the best R...|       True|
|The Witcher 3: Wi...|good story, good ...|       True|
|The Witcher 3: Wi...|            dis gud,|       True|
|The Witcher 3: Wi...|favorite game of ...|       True|
+--------------------+--------------------+-----------+
only showing top 4 rows

root
 |-- app_name: string (nullable = true)
 |-- review: string (nullable = true)
 |-- recommended: string (nullable = true)

Total number of recommended games before resampling: 6500516
Total number of not recommended games before resampling: 662337
ratio: 9
Total number of observations after resampling: 1383719
Total number of recommended games after resampling: 721382
Total number of not recommended games after resampling: 662337
resampled ratio: 1
root
 |-- app_name: string (nullable = true)
 |-- review: string (nullable = true)
 |-- label: integer (nullable = false)

+--------------------+--------------------+-----+
|            app_name|              review|label|
+--------------------+--------------------+-----+
|The Witcher 3: Wi...|                yes?|    1|
|The Witcher 3: Wi...|                good|    1|
|The Witcher 3: Wi...|Really nice story...|    1|
|The Witcher 3: Wi...|The Witcher 3 is ...|    1|
+--------------------+--------------------+-----+
only showing top 4 rows

end of the resampling process

Deleted /TP/output/logistic_regression_results
start of logistic regression classification
Input File: /TP/output/resampled_data	Output File: /TP/output/logistic_regression_results
+------------------+--------------------+-----+
|          app_name|              review|label|
+------------------+--------------------+-----+
|Grand Theft Auto V|its trash it keep...|    0|
|Grand Theft Auto V|single player is ...|    0|
|Grand Theft Auto V|Not fun if you do...|    0|
|Grand Theft Auto V|insanely overpric...|    0|
|Grand Theft Auto V|this is shit but ...|    0|
|Grand Theft Auto V|story mode is ver...|    0|
|Grand Theft Auto V|Loading screen th...|    0|
|Grand Theft Auto V|gta's story is pr...|    0|
|Grand Theft Auto V|Modders. ugh, hig...|    0|
|Grand Theft Auto V|just got banned f...|    0|
+------------------+--------------------+-----+
only showing top 10 rows

+------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|          app_name|              review|label|               words|            filtered|        raw_features|            features|
+------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|Grand Theft Auto V|its trash it keep...|    0|[its, trash, it, ...|[trash, keeps, cr...|(10000,[1807,2173...|(10000,[1807,2173...|
|Grand Theft Auto V|single player is ...|    0|[single, player, ...|[single, player, ...|(10000,[351,1807,...|(10000,[351,1807,...|
|Grand Theft Auto V|Not fun if you do...|    0|[not, fun, if, yo...|[fun, spend, real...|(10000,[353,4319,...|(10000,[353,4319,...|
|Grand Theft Auto V|insanely overpric...|    0|[insanely, overpr...|[insanely, overpr...|(10000,[3443,4012...|(10000,[3443,4012...|
|Grand Theft Auto V|this is shit but ...|    0|[this, is, shit, ...|[shit, imma, keep...|(10000,[1517,4781...|(10000,[1517,4781...|
|Grand Theft Auto V|story mode is ver...|    0|[story, mode, is,...|[story, mode, goo...|(10000,[211,353,4...|(10000,[211,353,4...|
|Grand Theft Auto V|Loading screen th...|    0|[loading, screen,...|[loading, screen,...|(10000,[1753,6315...|(10000,[1753,6315...|
|Grand Theft Auto V|gta's story is pr...|    0|[gta, s, story, i...|[gta, story, pret...|(10000,[855,931,1...|(10000,[855,931,1...|
|Grand Theft Auto V|Modders. ugh, hig...|    0|[modders, ugh, hi...|[modders, ugh, hi...|(10000,[80,178,28...|(10000,[80,178,28...|
|Grand Theft Auto V|just got banned f...|    0|[just, got, banne...|[got, banned, fuc...|(10000,[2944,6010...|(10000,[2944,6010...|
+------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
only showing top 10 rows

+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|            app_name|              review|label|               words|            filtered|        raw_features|            features|
+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|  Grand Theft Auto V|SHITY ONLINE PLAY...|    0|[shity, online, p...|[shity, online, p...|(10000,[490,1753,...|(10000,[490,1753,...|
|Tom Clancy's Rain...|"I just bought th...|    0|[i, just, bought,...|[bought, game, sh...|(10000,[141,447,1...|(10000,[141,447,1...|
|        Just Cause 3|I like this game ...|    1|[i, like, this, g...|[like, game, lot,...|(10000,[44,524,75...|(10000,[44,524,75...|
| Black Desert Online|Why pay 10 bucks ...|    0|[why, pay, 10, bu...|[pay, 10, bucks, ...|(10000,[1139,2398...|(10000,[1139,2398...|
|ARK: Survival Evo...|The game is buggy...|    0|[the, game, is, b...|[game, buggy, dra...|(10000,[1064,1376...|(10000,[1064,1376...|
|Sid Meier's Civil...|this game rules, ...|    1|[this, game, rule...|[game, rules, ll,...|(10000,[453,3443,...|(10000,[453,3443,...|
|PLAYERUNKNOWN'S B...|           sHIT GAME|    0|        [shit, game]|        [shit, game]|(10000,[8460,8975...|(10000,[8460,8975...|
|                Rust|             amazing|    1|           [amazing]|           [amazing]|  (10000,[44],[1.0])|(10000,[44],[3.46...|
|            Terraria|stupid ass shit s...|    1|[stupid, ass, shi...|[stupid, ass, shi...|(10000,[80,4000,7...|(10000,[80,4000,7...|
|                Rust|I cant run this shit|    0|[i, cant, run, th...|   [cant, run, shit]|(10000,[266,6026,...|(10000,[266,6026,...|
+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
only showing top 10 rows

+-----+--------------------+----------+
|label|         probability|prediction|
+-----+--------------------+----------+
|    0|[0.41525340158469...|       1.0|
|    1|[0.16790395083304...|       1.0|
|    1|[0.41528324676521...|       1.0|
|    1|[0.32663108727745...|       1.0|
|    1|[0.23096648478433...|       1.0|
|    1|[0.33848008237506...|       1.0|
|    1|[0.20065306161542...|       1.0|
|    1|[0.19950291704518...|       1.0|
|    1|[0.28318095189972...|       1.0|
|    1|[0.31381950914728...|       1.0|
+-----+--------------------+----------+
only showing top 10 rows

Cross validation accuracy: 0.9091001865455437

              precision    recall  f1-score   support

           0       0.88      0.72      0.79    132309
           1       0.78      0.91      0.84    143939

    accuracy                           0.82    276248
   macro avg       0.83      0.81      0.81    276248
weighted avg       0.83      0.82      0.82    276248

Best reg: 0.1
Best Max Iterations: 10
Best elasticNet: 0.0
Best family: auto
end of logistic regression classification

/TP/output/random_forest_results is empty
start of Random Forest classification
Input File: /TP/output/resampled_data	Output File: /TP/output/random_forest_results
+------------------+--------------------+-----+
|          app_name|              review|label|
+------------------+--------------------+-----+
|Grand Theft Auto V|its trash it keep...|    0|
|Grand Theft Auto V|single player is ...|    0|
|Grand Theft Auto V|Not fun if you do...|    0|
|Grand Theft Auto V|insanely overpric...|    0|
|Grand Theft Auto V|this is shit but ...|    0|
|Grand Theft Auto V|story mode is ver...|    0|
|Grand Theft Auto V|Loading screen th...|    0|
|Grand Theft Auto V|gta's story is pr...|    0|
|Grand Theft Auto V|Modders. ugh, hig...|    0|
|Grand Theft Auto V|just got banned f...|    0|
+------------------+--------------------+-----+
only showing top 10 rows

+------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|          app_name|              review|label|               words|            filtered|        raw_features|            features|
+------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|Grand Theft Auto V|its trash it keep...|    0|[its, trash, it, ...|[trash, keeps, cr...|(10000,[1807,2173...|(10000,[1807,2173...|
|Grand Theft Auto V|single player is ...|    0|[single, player, ...|[single, player, ...|(10000,[351,1807,...|(10000,[351,1807,...|
|Grand Theft Auto V|Not fun if you do...|    0|[not, fun, if, yo...|[fun, spend, real...|(10000,[353,4319,...|(10000,[353,4319,...|
|Grand Theft Auto V|insanely overpric...|    0|[insanely, overpr...|[insanely, overpr...|(10000,[3443,4012...|(10000,[3443,4012...|
|Grand Theft Auto V|this is shit but ...|    0|[this, is, shit, ...|[shit, imma, keep...|(10000,[1517,4781...|(10000,[1517,4781...|
|Grand Theft Auto V|story mode is ver...|    0|[story, mode, is,...|[story, mode, goo...|(10000,[211,353,4...|(10000,[211,353,4...|
|Grand Theft Auto V|Loading screen th...|    0|[loading, screen,...|[loading, screen,...|(10000,[1753,6315...|(10000,[1753,6315...|
|Grand Theft Auto V|gta's story is pr...|    0|[gta, s, story, i...|[gta, story, pret...|(10000,[855,931,1...|(10000,[855,931,1...|
|Grand Theft Auto V|Modders. ugh, hig...|    0|[modders, ugh, hi...|[modders, ugh, hi...|(10000,[80,178,28...|(10000,[80,178,28...|
|Grand Theft Auto V|just got banned f...|    0|[just, got, banne...|[got, banned, fuc...|(10000,[2944,6010...|(10000,[2944,6010...|
+------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
only showing top 10 rows

+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|            app_name|              review|label|               words|            filtered|        raw_features|            features|
+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|    Cities: Skylines|Expensive dlc to ...|    0|[expensive, dlc, ...|[expensive, dlc, ...|(10000,[1480,1637...|(10000,[1480,1637...|
|     DARK SOULS™ III|                 yee|    1|               [yee]|               [yee]|(10000,[7430],[1.0])|(10000,[7430],[8....|
|           HITMAN™ 2|looks good, but w...|    0|[looks, good, but...|[looks, good, man...|(10000,[836,3713,...|(10000,[836,3713,...|
|Monster Hunter: W...|"Game is a lot of...|    1|[game, is, a, lot...|[game, lot, fun, ...|(10000,[157,585,1...|(10000,[157,585,1...|
|        Phasmophobia|This game is supe...|    0|[this, game, is, ...|[game, super, bor...|(10000,[3851,4319...|(10000,[3851,4319...|
|      Hunt: Showdown|Just play Tarkov ...|    0|[just, play, tark...|[play, tarkov, ho...|(10000,[2173,4117...|(10000,[2173,4117...|
|          The Forest|With only a handf...|    0|[with, only, a, h...|[handful, differe...|(10000,[815,1052,...|(10000,[815,1052,...|
|Sekiro™: Shadows ...|It's like playing...|    0|[it, s, like, pla...|[like, playing, r...|(10000,[1,46,208,...|(10000,[1,46,208,...|
|Tom Clancy's Ghos...|Crashes within 30...|    0|[crashes, within,...|[crashes, within,...|(10000,[86,1614,1...|(10000,[86,1614,1...|
|            PAYDAY 2|Guns, cash, and c...|    1|[guns, cash, and,...|[guns, cash, coke...|(10000,[1251,3330...|(10000,[1251,3330...|
+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
only showing top 10 rows

+-----+--------------------+----------+
|label|         probability|prediction|
+-----+--------------------+----------+
|    1|[0.50521240186940...|       0.0|
|    0|[0.51240736785463...|       0.0|
|    1|[0.48752595956215...|       1.0|
|    1|[0.47582989430584...|       1.0|
|    0|[0.51061406548137...|       0.0|
|    1|[0.46215152889088...|       1.0|
|    1|[0.46215152889088...|       1.0|
|    1|[0.46215152889088...|       1.0|
|    1|[0.42880794570595...|       1.0|
|    1|[0.43024665858765...|       1.0|
+-----+--------------------+----------+
only showing top 10 rows

Cross validation accuracy: 0.8113383360896395

              precision    recall  f1-score   support

           0       0.87      0.33      0.48    132534
           1       0.61      0.96      0.74    144271

    accuracy                           0.66    276805
   macro avg       0.74      0.64      0.61    276805
weighted avg       0.74      0.66      0.62    276805

Best maxBins: 20
end of Random Forest classification


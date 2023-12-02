make[1]: Entering directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
shell_scripts/clean_data.sh
***********************************************************************************
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
***********************************************************************************
make[1]: Leaving directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
make[1]: Entering directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
shell_scripts/resample_data.sh
***********************************************************************************
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
Total number of observations after resampling: 1383763
Total number of recommended games after resampling: 721426
Total number of not recommended games after resampling: 662337
resampled ratio: 1
root
 |-- app_name: string (nullable = true)
 |-- review: string (nullable = true)
 |-- label: integer (nullable = false)

+--------------------+--------------------+-----+
|            app_name|              review|label|
+--------------------+--------------------+-----+
|The Witcher 3: Wi...|I don't think any...|    1|
|The Witcher 3: Wi...|Immersive and add...|    1|
|The Witcher 3: Wi...|           i like it|    1|
|The Witcher 3: Wi...|Fantastic game. V...|    1|
+--------------------+--------------------+-----+
only showing top 4 rows

end of the resampling process
***********************************************************************************
make[1]: Leaving directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
make[1]: Entering directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
shell_scripts/run_logistic_regressionr.sh
***********************************************************************************
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
|Grand Theft Auto V|its trash it keep...|    0|[its, trash, it, ...|[trash, keeps, cr...|(262144,[50671,68...|(262144,[50671,68...|
|Grand Theft Auto V|single player is ...|    0|[single, player, ...|[single, player, ...|(262144,[16607,33...|(262144,[16607,33...|
|Grand Theft Auto V|Not fun if you do...|    0|[not, fun, if, yo...|[fun, spend, real...|(262144,[23087,12...|(262144,[23087,12...|
|Grand Theft Auto V|insanely overpric...|    0|[insanely, overpr...|[insanely, overpr...|(262144,[2437,875...|(262144,[2437,875...|
|Grand Theft Auto V|this is shit but ...|    0|[this, is, shit, ...|[shit, imma, keep...|(262144,[32890,64...|(262144,[32890,64...|
|Grand Theft Auto V|story mode is ver...|    0|[story, mode, is,...|[story, mode, goo...|(262144,[2410,491...|(262144,[2410,491...|
|Grand Theft Auto V|Loading screen th...|    0|[loading, screen,...|[loading, screen,...|(262144,[81065,13...|(262144,[81065,13...|
|Grand Theft Auto V|gta's story is pr...|    0|[gta, s, story, i...|[gta, story, pret...|(262144,[23071,34...|(262144,[23071,34...|
|Grand Theft Auto V|Modders. ugh, hig...|    0|[modders, ugh, hi...|[modders, ugh, hi...|(262144,[22003,24...|(262144,[22003,24...|
|Grand Theft Auto V|just got banned f...|    0|[just, got, banne...|[got, banned, fuc...|(262144,[41748,15...|(262144,[41748,15...|
+------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
only showing top 10 rows

+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|            app_name|              review|label|               words|            filtered|        raw_features|            features|
+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|        No Man's Sky|"Sean Murray stol...|    0|[sean, murray, st...|[sean, murray, st...|(262144,[29558,31...|(262144,[29558,31...|
|           Half-Life|           fun stuff|    1|        [fun, stuff]|        [fun, stuff]|(262144,[23087,81...|(262144,[23087,81...|
|The Elder Scrolls...| Its SOOOO PRETTY!!!|    1|[its, soooo, pretty]|     [soooo, pretty]|(262144,[23071,13...|(262144,[23071,13...|
|              Arma 3|       good and good|    1|   [good, and, good]|        [good, good]|(262144,[113432],...|(262144,[113432],...|
|        DOOM Eternal|WHY IS THIS GAME ...|    1|[why, is, this, g...|[game, fucking, g...|(262144,[41748,11...|(262144,[41748,11...|
|             MORDHAU|for some reason i...|    0|[for, some, reaso...|[reason, go, back...|(262144,[31015,48...|(262144,[31015,48...|
|            Terraria|why are you check...|    0|[why, are, you, c...|[checking, bad, r...|(262144,[43224,78...|(262144,[43224,78...|
|   They Are Billions|       So Addictive!|    1|     [so, addictive]|         [addictive]|(262144,[136634],...|(262144,[136634],...|
|       Borderlands 3|This game feels l...|    0|[this, game, feel...|[game, feels, lik...|(262144,[12524,10...|(262144,[12524,10...|
|PLAYERUNKNOWN'S B...|this game is tota...|    0|[this, game, is, ...|  [game, totally, h]|(262144,[138895,2...|(262144,[138895,2...|
+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
only showing top 10 rows

+-----+--------------------+----------+
|label|         probability|prediction|
+-----+--------------------+----------+
|    1|[7.75897496546857...|       1.0|
|    1|[0.01346127963007...|       1.0|
|    1|[0.05025830958916...|       1.0|
|    1|[0.00314089294558...|       1.0|
|    1|[0.00599421345765...|       1.0|
|    1|[0.65455097614606...|       0.0|
|    1|[8.22623126846149...|       1.0|
|    1|[0.02681861805330...|       1.0|
|    1|[0.59139223590866...|       0.0|
|    1|[0.40810232172341...|       1.0|
+-----+--------------------+----------+
only showing top 10 rows

Best reg: 0.001
Best Max Iterations: 70
Best elasticNet: 0.0
Best family: auto
Logistic Regression raw prediction accuracy: 0.9510780769866516

              precision    recall  f1-score   support

           0       0.90      0.86      0.88    132745
           1       0.88      0.91      0.89    144070

    accuracy                           0.89    276815
   macro avg       0.89      0.89      0.89    276815
weighted avg       0.89      0.89      0.89    276815

prediction count: 276824
end of logistic regression classification
***********************************************************************************
make[1]: Leaving directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
make[1]: Entering directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
shell_scripts/run_random_forest.sh
***********************************************************************************
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
|         Garry's Mod|Garry's Mod is th...|    1|[garry, s, mod, i...|[garry, mod, best...|(10000,[763,2543,...|(10000,[763,2543,...|
|Tom Clancy's Rain...|     it's ok i guess|    1|[it, s, ok, i, gu...|         [ok, guess]|(10000,[2645,8660...|(10000,[2645,8660...|
|            Among Us|The game is fun f...|    1|[the, game, is, f...|[game, fun, bit, ...|(10000,[1805,1989...|(10000,[1805,1989...|
|  Grand Theft Auto V|           good game|    1|        [good, game]|        [good, game]|(10000,[6168,8975...|(10000,[6168,8975...|
|           HITMAN™ 2|Feels like a game...|    0|[feels, like, a, ...|[feels, like, gam...|(10000,[495,3330,...|(10000,[495,3330,...|
|     Castle Crashers|First boss is har...|    1|[first, boss, is,...|[first, boss, har...|(10000,[1653,6403...|(10000,[1653,6403...|
|         Garry's Mod|           nice game|    1|        [nice, game]|        [nice, game]|(10000,[3370,8975...|(10000,[3370,8975...|
|Call of Duty: Inf...|game is dead and ...|    0|[game, is, dead, ...|[game, dead, brok...|(10000,[80,4395,8...|(10000,[80,4395,8...|
|The Elder Scrolls...|iron daggers for ...|    1|[iron, daggers, f...|[iron, daggers, d...|(10000,[2205,3489...|(10000,[2205,3489...|
|       Rocket League|LOVE THIS GAME AL...|    1|[love, this, game...|  [love, game, play]|(10000,[2173,6240...|(10000,[2173,6240...|
+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
only showing top 10 rows

+-----+--------------------+----------+
|label|         probability|prediction|
+-----+--------------------+----------+
|    1|[0.44721324947744...|       1.0|
|    0|[0.47135579433751...|       1.0|
|    0|[0.46524573031606...|       1.0|
|    1|[0.47862493147879...|       1.0|
|    1|[0.47528521398567...|       1.0|
|    1|[0.45623179792966...|       1.0|
|    1|[0.49504341764382...|       1.0|
|    1|[0.49675185661188...|       1.0|
|    1|[0.44183240448693...|       1.0|
|    0|[0.46524573031606...|       1.0|
+-----+--------------------+----------+
only showing top 10 rows

Random Forest raw prediction accuracy: 0.8164833194927834

              precision    recall  f1-score   support

           0       0.88      0.33      0.48    132156
           1       0.61      0.96      0.75    144421

    accuracy                           0.66    276577
   macro avg       0.75      0.64      0.61    276577
weighted avg       0.74      0.66      0.62    276577

Local output_data is empty
***********************************************************************************
make[1]: Leaving directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
make[1]: Entering directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'
shell_scripts/dummy.sh
***********************************************************************************
Deleted /TP/output/dummy_results
start of dummy classification
Input File: /TP/output/resampled_data	Output File: /TP/output/dummy_results
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
|Grand Theft Auto V|its trash it keep...|    0|[its, trash, it, ...|[trash, keeps, cr...|(262144,[50671,68...|(262144,[50671,68...|
|Grand Theft Auto V|single player is ...|    0|[single, player, ...|[single, player, ...|(262144,[16607,33...|(262144,[16607,33...|
|Grand Theft Auto V|Not fun if you do...|    0|[not, fun, if, yo...|[fun, spend, real...|(262144,[23087,12...|(262144,[23087,12...|
|Grand Theft Auto V|insanely overpric...|    0|[insanely, overpr...|[insanely, overpr...|(262144,[2437,875...|(262144,[2437,875...|
|Grand Theft Auto V|this is shit but ...|    0|[this, is, shit, ...|[shit, imma, keep...|(262144,[32890,64...|(262144,[32890,64...|
|Grand Theft Auto V|story mode is ver...|    0|[story, mode, is,...|[story, mode, goo...|(262144,[2410,491...|(262144,[2410,491...|
|Grand Theft Auto V|Loading screen th...|    0|[loading, screen,...|[loading, screen,...|(262144,[81065,13...|(262144,[81065,13...|
|Grand Theft Auto V|gta's story is pr...|    0|[gta, s, story, i...|[gta, story, pret...|(262144,[23071,34...|(262144,[23071,34...|
|Grand Theft Auto V|Modders. ugh, hig...|    0|[modders, ugh, hi...|[modders, ugh, hi...|(262144,[22003,24...|(262144,[22003,24...|
|Grand Theft Auto V|just got banned f...|    0|[just, got, banne...|[got, banned, fuc...|(262144,[41748,15...|(262144,[41748,15...|
+------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
only showing top 10 rows

+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|            app_name|              review|label|               words|            filtered|        raw_features|            features|
+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
|    Darkest Dungeon®|You can tell I li...|    0|[you, can, tell, ...|[tell, like, game...|(262144,[1094,368...|(262144,[1094,368...|
|  Grand Theft Auto V|I started the gam...|    0|[i, started, the,...|[started, game, t...|(262144,[1546,230...|(262144,[1546,230...|
|            PAYDAY 2|micro transaction...|    0|[micro, transacti...|[micro, transacti...|(262144,[18184,11...|(262144,[18184,11...|
| Black Desert Online|bs game full of p...|    0|[bs, game, full, ...|[bs, game, full, ...|(262144,[9129,675...|(262144,[9129,675...|
|           Fallout 4|    Skyrim with guns|    1|[skyrim, with, guns]|      [skyrim, guns]|(262144,[140451,2...|(262144,[140451,2...|
|The Elder Scrolls...|I dare you to rei...|    1|[i, dare, you, to...|[dare, reinstall,...|(262144,[58237,69...|(262144,[58237,69...|
|The Elder Scrolls...|                game|    1|              [game]|              [game]|(262144,[138895],...|(262144,[138895],...|
|         Garry's Mod|Me and my friends...|    1|[me, and, my, fri...|[friends, enjoy, ...|(262144,[2701,767...|(262144,[2701,767...|
|           Fallout 4|Cant install mods...|    0|[cant, install, m...|[cant, install, m...|(262144,[17252,69...|(262144,[17252,69...|
|    Dead by Daylight|           i love it|    0|       [i, love, it]|              [love]|(262144,[186480],...|(262144,[186480],...|
+--------------------+--------------------+-----+--------------------+--------------------+--------------------+--------------------+
only showing top 10 rows

+-----+----------+
|label|prediction|
+-----+----------+
|    0|       0.0|
|    0|       1.0|
|    0|       0.0|
|    0|       1.0|
|    1|       1.0|
|    1|       1.0|
|    1|       1.0|
|    1|       1.0|
|    0|       0.0|
|    0|       0.0|
+-----+----------+
only showing top 10 rows

Dummy classifier raw prediction accuracy: 0.49941139289059633

              precision    recall  f1-score   support

           0       0.48      0.50      0.49    132334
           1       0.52      0.50      0.51    144111

    accuracy                           0.50    276445
   macro avg       0.50      0.50      0.50    276445
weighted avg       0.50      0.50      0.50    276445

end of dummy classification
***********************************************************************************
make[1]: Leaving directory '/s/chopin/g/under/delta27/cs435/TermProject/Project/CS435-Term-Project'

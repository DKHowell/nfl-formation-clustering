---
title: "NFL Formation Analysis"
output:
  html_document:
    keep_md: true
---



Import libraries.


```r
library(jtools)
library(car)
```

```
Loading required package: carData
```

```r
library(glmnet)
```

```
Loading required package: Matrix
```

```
Loaded glmnet 4.1-2
```

Import and format csv file created with NFL_defense_clustering.ipynb


```r
dat = read.csv('r_2_file.csv', stringsAsFactors = TRUE)
dat$cluster_=as.factor(dat$cluster_)
dat$Personnel = as.factor(dat$Personnel)
print(head(dat))
```

```
  cluster_         play_type_ posteam_type game_seconds_remaining
1       -1  pass deep outside         home                   3595
2        0 pass short outside         home                   3589
3        0           run left         home                   3554
4        0         run middle         home                   3532
5        1  pass deep outside         home                   3506
6        3           run left         home                   3482
  defendersInTheBox down ydstogo score_differential Personnel         epa
1                 7    1      10                  0       524 -0.51316344
2                 7    2      10                  0       416  0.39024173
3                 6    3       2                  0       416  1.16820927
4                 6    1      10                  0       416 -0.15614171
5                 5    2       7                  0       416  1.48862751
6                 7    1      10                  0       416 -0.03934548
```

Run ANOVA on EPA by formation clusters to determine if there is a significant difference in offensive play success against different clusters.


```r
anov1= aov(epa~cluster_, data=dat)
summary(anov1)
```

```
              Df Sum Sq Mean Sq F value Pr(>F)  
cluster_      13     36   2.787   1.619 0.0723 .
Residuals   9830  16922   1.722                 
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

Perform a Tukey Pairwise analysis of EPA by cluster.


```r
TukeyHSD(anov1, 'cluster_', conf.level=0.99)
```

```
  Tukey multiple comparisons of means
    99% family-wise confidence level

Fit: aov(formula = epa ~ cluster_, data = dat)

$cluster_
              diff         lwr        upr     p adj
0--1   0.084257109 -0.10354026 0.27205448 0.9115404
1--1   0.187169892 -0.03500448 0.40934427 0.0756487
2--1   0.055171119 -0.16278592 0.27312815 0.9995379
3--1   0.127535960 -0.07244714 0.32751906 0.4537371
4--1   0.064725668 -0.15780159 0.28725292 0.9980094
5--1   0.019343153 -0.24254020 0.28122650 1.0000000
6--1  -0.026246632 -0.36269522 0.31020195 1.0000000
7--1   0.059044470 -0.21708551 0.33517445 0.9999294
8--1   0.101456794 -0.50901324 0.71192682 0.9999963
9--1  -0.004115992 -0.42043594 0.41220396 1.0000000
10--1  0.135341881 -0.17217150 0.44285526 0.9228338
11--1  0.411378513 -0.30055719 1.12331422 0.6243126
12--1  0.007532708 -0.67399513 0.68906055 1.0000000
1-0    0.102912782 -0.08947155 0.29529711 0.7400715
2-0   -0.029085991 -0.21658412 0.15841213 0.9999984
3-0    0.043278851 -0.12298455 0.20954225 0.9993758
4-0   -0.019531442 -0.21232318 0.17326030 1.0000000
5-0   -0.064913956 -0.30204929 0.17222138 0.9989363
6-0   -0.110503741 -0.42806937 0.20706189 0.9887476
7-0   -0.025212640 -0.27799326 0.22756798 1.0000000
8-0    0.017199684 -0.58307020 0.61746957 1.0000000
9-0   -0.088373102 -0.48958699 0.31284078 0.9999010
10-0   0.051084772 -0.23564639 0.33781593 0.9999916
11-0   0.327121404 -0.37608748 1.03033028 0.8867144
12-0  -0.076724401 -0.74913088 0.59568208 1.0000000
2-1   -0.131998773 -0.35392026 0.08992272 0.5759515
3-1   -0.059633931 -0.26393057 0.14466271 0.9979363
4-1   -0.122444224 -0.34885592 0.10396747 0.7250690
5-1   -0.167826738 -0.43301868 0.09736520 0.4673815
6-1   -0.213416523 -0.55244680 0.12561375 0.4768262
7-1   -0.128125422 -0.40739526 0.15114442 0.8967952
8-1   -0.085713098 -0.69760977 0.52618357 0.9999995
9-1   -0.191285884 -0.60969499 0.22712322 0.8992430
10-1  -0.051828010 -0.36216389 0.25850787 0.9999961
11-1   0.224208622 -0.48895078 0.93736802 0.9956794
12-1  -0.179637183 -0.86244322 0.50316885 0.9993007
3-2    0.072364841 -0.12733727 0.27206696 0.9838227
4-2    0.009554549 -0.21272022 0.23182932 1.0000000
5-2   -0.035827966 -0.29749681 0.22584088 0.9999997
6-2   -0.081417751 -0.41769940 0.25486389 0.9997156
7-2    0.003873351 -0.27205320 0.27979990 1.0000000
8-2    0.046285675 -0.56409236 0.65666371 1.0000000
9-2   -0.059287111 -0.47547216 0.35689794 0.9999994
10-2   0.080170763 -0.22715996 0.38750149 0.9993613
11-2   0.356207394 -0.35564944 1.06806422 0.8206871
12-2  -0.047638411 -0.72908386 0.63380703 1.0000000
4-3   -0.062810292 -0.26749064 0.14187005 0.9965930
5-3   -0.108192807 -0.35509067 0.13870505 0.9252157
6-3   -0.153782592 -0.47870307 0.17113788 0.8730779
7-3   -0.068491490 -0.33045223 0.19346925 0.9993456
8-3   -0.026079167 -0.63027228 0.57811395 1.0000000
9-3   -0.131651953 -0.53871211 0.27540820 0.9943192
10-3   0.007805921 -0.28705022 0.30266206 1.0000000
11-3   0.283842553 -0.42271821 0.99040332 0.9614628
12-3  -0.120003252 -0.79591439 0.55590789 0.9999919
5-4   -0.045382515 -0.31087016 0.22010513 0.9999949
6-4   -0.090972299 -0.43023393 0.24828933 0.9991440
7-4   -0.005681198 -0.28523185 0.27386946 1.0000000
8-4    0.036731126 -0.57529376 0.64875601 1.0000000
9-4   -0.068841660 -0.48743825 0.34975493 0.9999968
10-4   0.070616214 -0.23997239 0.38120482 0.9998585
11-4   0.346652845 -0.36661657 1.05992226 0.8497873
12-4  -0.057192959 -0.74011390 0.62572798 1.0000000
6-5   -0.045589785 -0.41187241 0.32069284 0.9999999
7-5    0.039701317 -0.27208880 0.35149144 0.9999999
8-5    0.082113640 -0.54529290 0.70952018 0.9999998
9-5   -0.023459146 -0.46423984 0.41732154 1.0000000
10-5   0.115998728 -0.22389801 0.45589547 0.9905829
11-5   0.392035360 -0.33447532 1.11854604 0.7281351
12-5  -0.011810445 -0.70854965 0.68492876 1.0000000
7-6    0.085291101 -0.29130927 0.46189148 0.9998646
8-6    0.127703425 -0.53430393 0.78971078 0.9999785
9-6    0.022130639 -0.46664577 0.51090705 1.0000000
10-6   0.161588513 -0.23859214 0.56176917 0.9598530
11-6   0.437625145 -0.31896756 1.19421785 0.6226597
12-6   0.033779340 -0.69427305 0.76183173 1.0000000
8-7    0.042412324 -0.59107315 0.67589780 1.0000000
9-7   -0.063160462 -0.51255171 0.38623079 0.9999995
10-7   0.076297412 -0.27469357 0.42728839 0.9999148
11-7   0.352334043 -0.37943275 1.08410084 0.8583364
12-7  -0.051511761 -0.75372996 0.65070643 1.0000000
9-8   -0.105572786 -0.81153198 0.60038641 0.9999990
10-8   0.033885088 -0.61389617 0.68166635 1.0000000
11-8   0.309921720 -0.60216848 1.22201192 0.9909547
12-8  -0.093924085 -0.98248263 0.79463446 1.0000000
10-9   0.139457874 -0.32987059 0.60878634 0.9975292
11-9   0.415494506 -0.37984013 1.21082914 0.7708946
12-9   0.011648701 -0.75658624 0.77988364 1.0000000
11-10  0.276036632 -0.46814033 1.02021360 0.9801647
12-10 -0.127809173 -0.84295049 0.58733215 0.9999913
12-11 -0.403845805 -1.36494678 0.55725517 0.9452521
```

Run ANOVA again with interaction terms.


```r
anov2 = lm(epa~cluster_+play_type_+cluster_:play_type_, data=dat)
summ(anov2)
```

```
MODEL INFO:
Observations: 9844
Dependent Variable: epa
Type: OLS linear regression 

MODEL FIT:
F(97,9746) = 2.29, p = 0.00
R² = 0.02
Adj. R² = 0.01 

Standard errors: OLS
------------------------------------------------------------
                                 Est.   S.E.   t val.      p
----------------------------- ------- ------ -------- ------
(Intercept)                      0.38   0.29     1.29   0.20
cluster_0                        0.07   0.35     0.19   0.85
cluster_1                        0.60   0.40     1.51   0.13
cluster_2                       -0.13   0.40    -0.33   0.74
cluster_3                       -0.02   0.37    -0.06   0.95
cluster_4                        0.73   0.45     1.64   0.10
cluster_5                       -0.55   0.65    -0.84   0.40
cluster_6                       -1.38   0.97    -1.43   0.15
cluster_7                       -0.58   0.57    -1.02   0.31
cluster_8                        2.30   1.34     1.72   0.09
cluster_9                        0.38   0.52     0.73   0.46
cluster_10                       0.12   0.51     0.24   0.81
cluster_11                       0.81   1.34     0.61   0.54
cluster_12                      -3.19   0.97    -3.29   0.00
play_type_pass deep             -0.48   0.32    -1.48   0.14
outside                                                     
play_type_pass short            -0.20   0.31    -0.65   0.51
middle                                                      
play_type_pass short            -0.52   0.30    -1.73   0.08
outside                                                     
play_type_run left              -0.45   0.32    -1.43   0.15
play_type_run middle            -0.36   0.32    -1.15   0.25
play_type_run right             -0.43   0.31    -1.36   0.17
cluster_0:play_type_pass         0.53   0.39     1.35   0.18
deep outside                                                
cluster_1:play_type_pass        -0.21   0.45    -0.47   0.64
deep outside                                                
cluster_2:play_type_pass         0.49   0.45     1.09   0.28
deep outside                                                
cluster_3:play_type_pass         0.34   0.41     0.83   0.41
deep outside                                                
cluster_4:play_type_pass        -0.05   0.49    -0.11   0.91
deep outside                                                
cluster_5:play_type_pass         0.81   0.70     1.17   0.24
deep outside                                                
cluster_6:play_type_pass         1.75   1.02     1.72   0.09
deep outside                                                
cluster_7:play_type_pass         0.68   0.62     1.09   0.27
deep outside                                                
cluster_8:play_type_pass        -1.60   1.44    -1.11   0.27
deep outside                                                
cluster_9:play_type_pass        -1.11   0.67    -1.67   0.10
deep outside                                                
cluster_10:play_type_pass        0.65   0.58     1.11   0.27
deep outside                                                
cluster_11:play_type_pass        1.58   1.43     1.11   0.27
deep outside                                                
cluster_12:play_type_pass        3.46   1.11     3.11   0.00
deep outside                                                
cluster_0:play_type_pass        -0.01   0.38    -0.03   0.98
short middle                                                
cluster_1:play_type_pass        -0.48   0.43    -1.10   0.27
short middle                                                
cluster_2:play_type_pass        -0.12   0.44    -0.28   0.78
short middle                                                
cluster_3:play_type_pass         0.11   0.40     0.28   0.78
short middle                                                
cluster_4:play_type_pass        -0.91   0.48    -1.90   0.06
short middle                                                
cluster_5:play_type_pass         0.35   0.69     0.51   0.61
short middle                                                
cluster_6:play_type_pass         1.38   1.00     1.38   0.17
short middle                                                
cluster_7:play_type_pass         0.11   0.62     0.19   0.85
short middle                                                
cluster_8:play_type_pass        -1.35   1.42    -0.95   0.34
short middle                                                
cluster_9:play_type_pass        -0.51   0.58    -0.87   0.39
short middle                                                
cluster_10:play_type_pass        0.14   0.55     0.25   0.80
short middle                                                
cluster_11:play_type_pass       -1.10   1.41    -0.78   0.43
short middle                                                
cluster_12:play_type_pass        3.13   1.11     2.82   0.00
short middle                                                
cluster_0:play_type_pass         0.03   0.36     0.10   0.92
short outside                                               
cluster_1:play_type_pass        -0.36   0.41    -0.88   0.38
short outside                                               
cluster_2:play_type_pass         0.30   0.41     0.74   0.46
short outside                                               
cluster_3:play_type_pass         0.24   0.38     0.63   0.53
short outside                                               
cluster_4:play_type_pass        -0.56   0.46    -1.23   0.22
short outside                                               
cluster_5:play_type_pass         0.73   0.66     1.10   0.27
short outside                                               
cluster_6:play_type_pass         1.48   0.98     1.52   0.13
short outside                                               
cluster_7:play_type_pass         0.83   0.59     1.42   0.16
short outside                                               
cluster_8:play_type_pass        -1.94   1.37    -1.42   0.16
short outside                                               
cluster_9:play_type_pass        -0.27   0.55    -0.49   0.62
short outside                                               
cluster_10:play_type_pass        0.10   0.52     0.18   0.85
short outside                                               
cluster_11:play_type_pass       -0.52   1.37    -0.38   0.71
short outside                                               
cluster_12:play_type_pass        3.32   1.02     3.26   0.00
short outside                                               
cluster_0:play_type_run         -0.05   0.38    -0.14   0.88
left                                                        
cluster_1:play_type_run         -0.50   0.43    -1.16   0.25
left                                                        
cluster_2:play_type_run          0.19   0.43     0.43   0.67
left                                                        
cluster_3:play_type_run          0.11   0.39     0.28   0.78
left                                                        
cluster_4:play_type_run         -0.79   0.47    -1.67   0.09
left                                                        
cluster_5:play_type_run          0.46   0.67     0.68   0.50
left                                                        
cluster_6:play_type_run          1.17   0.99     1.18   0.24
left                                                        
cluster_7:play_type_run          0.67   0.60     1.12   0.26
left                                                        
cluster_8:play_type_run         -2.69   1.40    -1.92   0.06
left                                                        
cluster_9:play_type_run         -0.37   0.61    -0.61   0.54
left                                                        
cluster_10:play_type_run        -0.32   0.57    -0.56   0.57
left                                                        
cluster_11:play_type_run        -0.84   1.87    -0.45   0.66
left                                                        
cluster_12:play_type_run         3.16   1.04     3.03   0.00
left                                                        
cluster_0:play_type_run         -0.07   0.38    -0.18   0.86
middle                                                      
cluster_1:play_type_run         -0.67   0.44    -1.52   0.13
middle                                                      
cluster_2:play_type_run          0.01   0.44     0.02   0.98
middle                                                      
cluster_3:play_type_run          0.05   0.40     0.12   0.90
middle                                                      
cluster_4:play_type_run         -0.86   0.47    -1.80   0.07
middle                                                      
cluster_5:play_type_run          0.67   0.68     0.98   0.33
middle                                                      
cluster_6:play_type_run          1.25   1.00     1.25   0.21
middle                                                      
cluster_7:play_type_run          0.43   0.61     0.71   0.48
middle                                                      
cluster_8:play_type_run         -2.83   1.41    -2.00   0.05
middle                                                      
cluster_9:play_type_run         -0.62   0.67    -0.92   0.36
middle                                                      
cluster_10:play_type_run        -0.52   0.57    -0.91   0.36
middle                                                      
cluster_11:play_type_run        -0.93   1.41    -0.66   0.51
middle                                                      
cluster_12:play_type_run         3.46   1.23     2.81   0.00
middle                                                      
cluster_0:play_type_run         -0.15   0.38    -0.39   0.70
right                                                       
cluster_1:play_type_run         -0.48   0.43    -1.11   0.27
right                                                       
cluster_2:play_type_run          0.15   0.43     0.35   0.73
right                                                       
cluster_3:play_type_run         -0.03   0.39    -0.07   0.94
right                                                       
cluster_4:play_type_run         -0.81   0.47    -1.73   0.08
right                                                       
cluster_5:play_type_run          0.36   0.68     0.53   0.59
right                                                       
cluster_6:play_type_run          1.25   0.99     1.25   0.21
right                                                       
cluster_7:play_type_run          0.73   0.60     1.21   0.22
right                                                       
cluster_8:play_type_run         -2.65   1.38    -1.93   0.05
right                                                       
cluster_9:play_type_run         -0.49   0.61    -0.81   0.42
right                                                       
cluster_10:play_type_run        -0.18   0.55    -0.32   0.75
right                                                       
cluster_11:play_type_run        -0.64   1.43    -0.45   0.65
right                                                       
cluster_12:play_type_run         3.40   1.06     3.22   0.00
right                                                       
------------------------------------------------------------
```

Examine assumptions of ANOVA to determine if there are any serious violations.


```r
par(mfrow=c(2,2))
plot(anov2$fitted.values, anov2$residuals, xlab = 'residuals', ylab='fitted values', main = 'Residuals vs. Fitted')
qqnorm(anov2$residuals)
qqline(anov2$residuals)
hist(anov2$residuals, main = '', xlab='residuals')
```

![](ClusterAnalysis_files/figure-html/unnamed-chunk-6-1.png)<!-- -->
2-way ANOVA with interaction terms included.



Apply Box-Cox transformation to EPA.


```r
dat$epa = dat$epa-min(dat$epa)+1
model2  = lm(epa~cluster_+play_type_+cluster_:play_type_, data=dat)
bc = boxCox(model2)
```

![](ClusterAnalysis_files/figure-html/unnamed-chunk-7-1.png)<!-- -->

```r
opt.lambda = bc$x[which.max(bc$y)]
# Round it to the nearest 0.5
cat("Optimal lambda:", opt.lambda, end="\n")
```

```
Optimal lambda: 1.676768 
```

```r
anov3 = lm(epa**opt.lambda~cluster_+play_type_+cluster_:play_type_, data=dat)
summ(anov3)
```

```
MODEL INFO:
Observations: 9844
Dependent Variable: epa^opt.lambda
Type: OLS linear regression 

MODEL FIT:
F(97,9746) = 2.85, p = 0.00
R² = 0.03
Adj. R² = 0.02 

Standard errors: OLS
--------------------------------------------------------------
                                  Est.    S.E.   t val.      p
----------------------------- -------- ------- -------- ------
(Intercept)                      74.54    2.66    28.01   0.00
cluster_0                         1.55    3.22     0.48   0.63
cluster_1                         5.60    3.64     1.54   0.12
cluster_2                        -1.33    3.68    -0.36   0.72
cluster_3                         0.19    3.35     0.06   0.96
cluster_4                         7.55    4.07     1.86   0.06
cluster_5                        -3.56    5.95    -0.60   0.55
cluster_6                       -13.57    8.83    -1.54   0.12
cluster_7                        -5.45    5.23    -1.04   0.30
cluster_8                        22.14   12.20     1.82   0.07
cluster_9                         3.25    4.78     0.68   0.50
cluster_10                        1.96    4.61     0.43   0.67
cluster_11                        6.88   12.20     0.56   0.57
cluster_12                      -27.45    8.83    -3.11   0.00
play_type_pass deep              -4.30    2.93    -1.47   0.14
outside                                                       
play_type_pass short             -2.17    2.86    -0.76   0.45
middle                                                        
play_type_pass short             -5.29    2.72    -1.94   0.05
outside                                                       
play_type_run left               -4.93    2.88    -1.71   0.09
play_type_run middle             -4.20    2.89    -1.45   0.15
play_type_run right              -4.61    2.86    -1.61   0.11
cluster_0:play_type_pass          3.72    3.55     1.05   0.30
deep outside                                                  
cluster_1:play_type_pass         -2.44    4.06    -0.60   0.55
deep outside                                                  
cluster_2:play_type_pass          4.87    4.11     1.18   0.24
deep outside                                                  
cluster_3:play_type_pass          2.53    3.71     0.68   0.50
deep outside                                                  
cluster_4:play_type_pass         -1.42    4.45    -0.32   0.75
deep outside                                                  
cluster_5:play_type_pass          5.37    6.37     0.84   0.40
deep outside                                                  
cluster_6:play_type_pass         17.14    9.30     1.84   0.07
deep outside                                                  
cluster_7:play_type_pass          6.22    5.69     1.09   0.27
deep outside                                                  
cluster_8:play_type_pass        -15.87   13.18    -1.20   0.23
deep outside                                                  
cluster_9:play_type_pass        -10.80    6.10    -1.77   0.08
deep outside                                                  
cluster_10:play_type_pass         5.33    5.33     1.00   0.32
deep outside                                                  
cluster_11:play_type_pass        16.32   13.06     1.25   0.21
deep outside                                                  
cluster_12:play_type_pass        29.29   10.15     2.89   0.00
deep outside                                                  
cluster_0:play_type_pass         -1.32    3.48    -0.38   0.70
short middle                                                  
cluster_1:play_type_pass         -4.29    3.93    -1.09   0.27
short middle                                                  
cluster_2:play_type_pass         -1.02    3.98    -0.26   0.80
short middle                                                  
cluster_3:play_type_pass          0.39    3.62     0.11   0.91
short middle                                                  
cluster_4:play_type_pass         -9.29    4.34    -2.14   0.03
short middle                                                  
cluster_5:play_type_pass          1.54    6.29     0.24   0.81
short middle                                                  
cluster_6:play_type_pass         13.34    9.13     1.46   0.14
short middle                                                  
cluster_7:play_type_pass          1.25    5.64     0.22   0.82
short middle                                                  
cluster_8:play_type_pass        -13.50   12.94    -1.04   0.30
short middle                                                  
cluster_9:play_type_pass         -4.41    5.34    -0.83   0.41
short middle                                                  
cluster_10:play_type_pass         0.47    5.01     0.09   0.93
short middle                                                  
cluster_11:play_type_pass       -10.21   12.87    -0.79   0.43
short middle                                                  
cluster_12:play_type_pass        26.70   10.13     2.64   0.01
short middle                                                  
cluster_0:play_type_pass         -0.61    3.30    -0.18   0.85
short outside                                                 
cluster_1:play_type_pass         -3.46    3.73    -0.93   0.35
short outside                                                 
cluster_2:play_type_pass          2.81    3.77     0.75   0.46
short outside                                                 
cluster_3:play_type_pass          1.73    3.44     0.50   0.61
short outside                                                 
cluster_4:play_type_pass         -6.18    4.16    -1.48   0.14
short outside                                                 
cluster_5:play_type_pass          5.18    6.04     0.86   0.39
short outside                                                 
cluster_6:play_type_pass         14.23    8.93     1.59   0.11
short outside                                                 
cluster_7:play_type_pass          7.64    5.36     1.43   0.15
short outside                                                 
cluster_8:play_type_pass        -19.20   12.48    -1.54   0.12
short outside                                                 
cluster_9:play_type_pass         -2.28    5.03    -0.45   0.65
short outside                                                 
cluster_10:play_type_pass        -0.08    4.74    -0.02   0.99
short outside                                                 
cluster_11:play_type_pass        -4.41   12.53    -0.35   0.72
short outside                                                 
cluster_12:play_type_pass        28.44    9.28     3.07   0.00
short outside                                                 
cluster_0:play_type_run          -1.53    3.46    -0.44   0.66
left                                                          
cluster_1:play_type_run          -4.69    3.93    -1.19   0.23
left                                                          
cluster_2:play_type_run           1.75    3.93     0.45   0.66
left                                                          
cluster_3:play_type_run           0.63    3.60     0.18   0.86
left                                                          
cluster_4:play_type_run          -8.14    4.33    -1.88   0.06
left                                                          
cluster_5:play_type_run           2.73    6.15     0.44   0.66
left                                                          
cluster_6:play_type_run          11.43    9.05     1.26   0.21
left                                                          
cluster_7:play_type_run           6.11    5.46     1.12   0.26
left                                                          
cluster_8:play_type_run         -26.00   12.81    -2.03   0.04
left                                                          
cluster_9:play_type_run          -3.32    5.55    -0.60   0.55
left                                                          
cluster_10:play_type_run         -3.96    5.16    -0.77   0.44
left                                                          
cluster_11:play_type_run         -7.40   17.08    -0.43   0.66
left                                                          
cluster_12:play_type_run         27.00    9.53     2.83   0.00
left                                                          
cluster_0:play_type_run          -1.60    3.49    -0.46   0.65
middle                                                        
cluster_1:play_type_run          -6.27    3.99    -1.57   0.12
middle                                                        
cluster_2:play_type_run           0.23    3.99     0.06   0.95
middle                                                        
cluster_3:play_type_run           0.26    3.65     0.07   0.94
middle                                                        
cluster_4:play_type_run          -8.70    4.33    -2.01   0.04
middle                                                        
cluster_5:play_type_run           4.75    6.20     0.77   0.44
middle                                                        
cluster_6:play_type_run          12.22    9.11     1.34   0.18
middle                                                        
cluster_7:play_type_run           4.09    5.58     0.73   0.46
middle                                                        
cluster_8:play_type_run         -26.96   12.87    -2.09   0.04
middle                                                        
cluster_9:play_type_run          -5.51    6.08    -0.91   0.37
middle                                                        
cluster_10:play_type_run         -5.60    5.22    -1.07   0.28
middle                                                        
cluster_11:play_type_run         -8.09   12.87    -0.63   0.53
middle                                                        
cluster_12:play_type_run         29.94   11.24     2.66   0.01
middle                                                        
cluster_0:play_type_run          -2.50    3.45    -0.73   0.47
right                                                         
cluster_1:play_type_run          -4.65    3.94    -1.18   0.24
right                                                         
cluster_2:play_type_run           1.28    3.93     0.33   0.75
right                                                         
cluster_3:play_type_run          -0.84    3.60    -0.23   0.82
right                                                         
cluster_4:play_type_run          -8.45    4.29    -1.97   0.05
right                                                         
cluster_5:play_type_run           1.64    6.17     0.27   0.79
right                                                         
cluster_6:play_type_run          12.00    9.05     1.33   0.19
right                                                         
cluster_7:play_type_run           6.73    5.48     1.23   0.22
right                                                         
cluster_8:play_type_run         -25.77   12.58    -2.05   0.04
right                                                         
cluster_9:play_type_run          -4.51    5.54    -0.81   0.42
right                                                         
cluster_10:play_type_run         -2.73    5.03    -0.54   0.59
right                                                         
cluster_11:play_type_run         -4.85   13.04    -0.37   0.71
right                                                         
cluster_12:play_type_run         29.15    9.65     3.02   0.00
right                                                         
--------------------------------------------------------------
```

```r
par(mfrow=c(2,2))
plot(anov3$fitted.values, anov3$residuals, xlab = 'residuals', ylab='fitted values', main = 'Residuals vs. Fitted')
qqnorm(anov3$residuals)
qqline(anov3$residuals)
hist(anov3$residuals, main = '', xlab='residuals')
```

![](ClusterAnalysis_files/figure-html/unnamed-chunk-8-1.png)<!-- -->

Run ridge regression model with all variables


```r
library(glmnet)
X =  model.matrix( ~ .-1, dat[,-10])
ridge.cv = cv.glmnet(X, dat[,10], alpha=1, nfolds = 30)
ridge.model <- glmnet(X, dat[,10], alpha=1, nlambda = 100)
coef(ridge.model, ridge.cv$lambda.min)
```

```
48 x 1 sparse Matrix of class "dgCMatrix"
                                        s1
(Intercept)                   1.292226e+01
cluster_-1                   -6.623211e-02
cluster_0                     .           
cluster_1                     9.055690e-02
cluster_2                     .           
cluster_3                     3.568258e-02
cluster_4                     .           
cluster_5                    -2.109475e-02
cluster_6                    -5.993729e-02
cluster_7                     .           
cluster_8                     .           
cluster_9                    -4.323430e-02
cluster_10                    3.325088e-02
cluster_11                    2.238151e-01
cluster_12                    .           
play_type_pass deep outside   1.375942e-01
play_type_pass short middle   .           
play_type_pass short outside -1.355191e-01
play_type_run left           -2.171859e-01
play_type_run middle         -1.958001e-01
play_type_run right          -2.397033e-01
posteam_typehome              .           
game_seconds_remaining        1.461961e-05
defendersInTheBox            -1.297120e-03
down                         -2.309121e-02
ydstogo                      -1.615554e-02
score_differential            5.280475e-04
Personnel227                  .           
Personnel245                 -2.675081e-01
Personnel308                  .           
Personnel317                 -2.394105e-01
Personnel326                  5.019641e-03
Personnel335                  3.082774e-02
Personnel416                  .           
Personnel425                  .           
Personnel434                 -2.729630e-02
Personnel443                 -3.463810e-01
Personnel515                  1.762641e-01
Personnel524                  .           
Personnel533                  .           
Personnel542                  2.415587e-01
Personnel614                  .           
Personnel623                  9.724342e-02
Personnel632                  1.059421e-01
Personnel641                  1.925971e-01
Personnel713                 -2.708879e+00
Personnel722                  .           
Personnel731                  .           
```
Forward-backward stepwise regression.


```r
n = nrow(dat)
base_mod = lm(epa~1, data=dat)
full_mod = lm(epa~.+cluster_:play_type_, data=dat)
stepwise_model = step(base_mod, scope=list(lower=base_mod, upper=full_mod), direction="both", k=2, trace=F)
summ(stepwise_model)
```

```
MODEL INFO:
Observations: 9844
Dependent Variable: epa
Type: OLS linear regression 

MODEL FIT:
F(9,9834) = 13.61, p = 0.00
R² = 0.01
Adj. R² = 0.01 

Standard errors: OLS
-----------------------------------------------------------
                                Est.   S.E.   t val.      p
---------------------------- ------- ------ -------- ------
(Intercept)                    13.30   0.11   118.33   0.00
play_type_pass deep            -0.18   0.10    -1.70   0.09
outside                                                    
play_type_pass short           -0.33   0.10    -3.23   0.00
middle                                                     
play_type_pass short           -0.48   0.10    -4.95   0.00
outside                                                    
play_type_run left             -0.57   0.10    -5.73   0.00
play_type_run middle           -0.55   0.10    -5.42   0.00
play_type_run right            -0.60   0.10    -5.96   0.00
ydstogo                        -0.02   0.00    -5.63   0.00
down                           -0.04   0.02    -2.10   0.04
game_seconds_remaining          0.00   0.00     1.55   0.12
-----------------------------------------------------------
```


```r
step(base_mod, scope=list(lower=base_mod, upper=full_mod), direction="both", k=2)
```

```
Start:  AIC=5356.19
epa ~ 1

                         Df Sum of Sq   RSS    AIC
+ play_type_              6   150.190 16808 5280.6
+ ydstogo                 1    32.635 16926 5339.2
<none>                                16958 5356.2
+ down                    1     2.373 16956 5356.8
+ game_seconds_remaining  1     2.199 16956 5356.9
+ defendersInTheBox       1     2.082 16956 5357.0
+ score_differential      1     0.051 16958 5358.2
+ posteam_type            1     0.003 16958 5358.2
+ cluster_               13    36.227 16922 5361.1
+ Personnel              21    61.499 16897 5362.4

Step:  AIC=5280.62
epa ~ play_type_

                         Df Sum of Sq   RSS    AIC
+ ydstogo                 1    46.555 16762 5255.3
+ game_seconds_remaining  1     4.390 16804 5280.0
<none>                                16808 5280.6
+ defendersInTheBox       1     3.339 16805 5280.7
+ score_differential      1     1.176 16807 5281.9
+ down                    1     0.125 16808 5282.5
+ posteam_type            1     0.007 16808 5282.6
+ Personnel              21    61.079 16747 5286.8
+ cluster_               13    33.177 16775 5287.2
- play_type_              6   150.190 16958 5356.2

Step:  AIC=5255.31
epa ~ play_type_ + ydstogo

                         Df Sum of Sq   RSS    AIC
+ down                    1     7.812 16754 5252.7
+ game_seconds_remaining  1     4.418 16757 5254.7
<none>                                16762 5255.3
+ score_differential      1     1.499 16760 5256.4
+ defendersInTheBox       1     0.090 16762 5257.3
+ posteam_type            1     0.045 16762 5257.3
+ cluster_               13    32.249 16729 5262.4
+ Personnel              21    53.901 16708 5265.6
- ydstogo                 1    46.555 16808 5280.6
- play_type_              6   164.110 16926 5339.2

Step:  AIC=5252.72
epa ~ play_type_ + ydstogo + down

                         Df Sum of Sq   RSS    AIC
+ game_seconds_remaining  1     4.100 16750 5252.3
<none>                                16754 5252.7
+ score_differential      1     1.763 16752 5253.7
+ defendersInTheBox       1     0.144 16754 5254.6
+ posteam_type            1     0.055 16754 5254.7
- down                    1     7.812 16762 5255.3
+ cluster_               13    33.513 16720 5259.0
+ Personnel              21    53.144 16701 5263.4
- ydstogo                 1    54.242 16808 5282.5
- play_type_              6   171.864 16926 5341.2

Step:  AIC=5252.31
epa ~ play_type_ + ydstogo + down + game_seconds_remaining

                         Df Sum of Sq   RSS    AIC
<none>                                16750 5252.3
- game_seconds_remaining  1     4.100 16754 5252.7
+ score_differential      1     1.460 16748 5253.5
+ defendersInTheBox       1     0.259 16750 5254.2
+ posteam_type            1     0.084 16750 5254.3
- down                    1     7.493 16757 5254.7
+ cluster_               13    34.032 16716 5258.3
+ Personnel              21    53.576 16696 5262.8
- ydstogo                 1    53.988 16804 5282.0
- play_type_              6   173.832 16924 5342.0
```

```

Call:
lm(formula = epa ~ play_type_ + ydstogo + down + game_seconds_remaining, 
    data = dat)

Coefficients:
                 (Intercept)   play_type_pass deep outside  
                   1.330e+01                    -1.777e-01  
 play_type_pass short middle  play_type_pass short outside  
                  -3.283e-01                    -4.776e-01  
          play_type_run left          play_type_run middle  
                  -5.732e-01                    -5.525e-01  
         play_type_run right                       ydstogo  
                  -5.966e-01                    -1.979e-02  
                        down        game_seconds_remaining  
                  -3.741e-02                     1.958e-05  
```

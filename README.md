## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125718
- **Columns**: 5

#### data read
first import padndas module to Identifying Data, and read the csv file
```
import pandas as pd
dirty = pd.read_csv('messy_population_data.csv')
```
#### check columns
next we check the dataframe's column name,number, data types,non-null count etc
```
dirty.info()
```
next we find the mean,sd etc
```
dirty.describe()
```
#### missing value
find missing value of each column
```
dirty.isna().sum()
```
```
income_groups    6306
age              6223
gender           5907
year             6202
population       6340
```
#### check duplicated rows
check how many rows are duplicate
```
dirty.duplicated().sum()
```
```
2950
```
#### chceck unique value

next we find the unique vlaue for each column
```
a = dirty['income_groups'].unique()
print(a)

b = dirty['year'].unique()
print(b)

c = dirty['gender'].unique()
print(c)

d = dirty['age'].unique()
print(d)

e = dirty['population'].unique()
print(e)
```
for income_groups we have:
```
['high_income' nan 'high_income_typo''low_income''low_income_typo' 'lower_middle_income' 'lower_middle_income_typo' 'upper_middle_income_typo' 'upper_middle_income']
```
for age we have:
```
[  0.  nan   1.  10. 100.  11.  12.  13.  14.  15.  16.  17.  18.  19. 2.  20.  21.  22.  23.  24.  25.  26.  27.  28.  29.   3.  30.  31. 32.  33.  34.  35.  36.  37.  38.  39.   4.  40.  41.  42.  43.  44. 45.  46.  47.  48.  49.   5.  50.  51.  52.  53.  54.  55.  56.  57. 58.  59.   6.  60.  61.  62.  63.  64.  65.  66.  67.  68.  69.   7. 70.  71.  72.  73.  74.  75.  76.  77.  78.  79.   8.  80.  81.  82. 83.  84.  85.  86.  87.  88.  89.   9.  90.  91.  92.  93.  94.  95. 96.  97.  98.  99.]
```

for gender we have:
```
[ 1.  3. nan  2.]
```
for year we have:
```
[1950. 1951. 1952. 1953. 1954. 1955. 1956. 1957. 1958. 1959. 1960. 1961. 1962. nan 1964. 1965. 1966. 1967. 1968. 1969. 1970. 1971. 1972. 1973. 1974. 1975. 1976. 1977. 1978. 1979. 1980. 1981. 1983. 1984. 1985. 1986. 1987. 1988. 1989. 1990. 1991. 1992. 1993. 1994. 1995. 1996. 1998. 1999. 2000. 2001. 2002. 2003. 2004. 2005. 2006. 2007. 2008. 2009. 2010. 2011. 2012. 2013. 2014. 2015. 2016. 2017. 2018. 2019. 2020. 2021. 2022. 2023. 2024. 2025. 2026. 2027. 2028. 2029. 2030. 2031. 2032. 2033. 2034. 2035. 2036. 2037. 2038. 2039. 2040. 2041. 2042. 2043. 2044. 2045. 2046. 2047. 2048. 2049. 2050. 2051. 2052. 2054. 2055. 2056. 2057. 2058. 2059. 2060. 2061. 2062. 2063. 2064. 2065. 2066. 2067. 2068. 2069. 2070. 2071. 2072. 2073. 2074. 2075. 2076. 2077. 2078. 2079. 2080. 2081. 2082. 2083. 2084. 2085. 2086. 2087. 2088. 2089. 2090. 2091. 2092. 2093. 2094. 2095. 2096. 2097. 2099. 2100. 1963. 1982. 1997. 2053. 2098. 2119. 2103. 2101. 2107. 2117. 2114. 2113. 2110. 2118. 2105. 2116. 2106. 2109. 2104. 2111. 2102. 2108. 2115.]
```
for population we have:
```
[7.7982860e+06 7.7397110e+06 7.7139050e+06 ... 3.4482690e+06 1.2118786e+09  7.7754050e+06]
```

### Column Details
| Column Name    | Data Type | Non-Null Count |  Mean  |
|----------------|-----------|----------------|--------|
| income_groups  | object    | 119412         | [Mean] |
| age            | float64   | 119495         | 50.007 |
| gender         | float64   | 119811         | [Mean] |
| year           | float64   | 119516         | 2025   |
| population     | float64   | 119378         |1.11e+08|

### Identified Issues

1. **[Missing Values]**
   - Description: There are some missing value in each column
   - Affected Column(s): income_groups,age,gender,year,population
   - Example: Nah value in each columns
   - Potential Impact: Missing data can reduce the statistical power of a study and can produce biased estimates

2. **[incorrect Categories value]**
   - Description: there are some typo in Categories column
   - Affected Column(s): income_groups
   - Example: "lower_middle_income_typo" etc.
   - Potential Impact: wrong grouping could skew your data away from the true value

3. **[woring year]**
   - Description: There are some year value are greater than current year value
   - Affected Column(s): year
   - Example: 2067,2068,2069...
   - Potential Impact: Unreal year value cause mistakes on the analysis

4. **[duplicate rows]**
   - Description: there are some rows are duplicated
   - Affected Column(s): income_groups,age,gender,year population
   - Example: rows are same
   - Potential Impact: Duplicate rows can inflate certain data statistics, leading to inaccurate results. 

5. **[woring data type]**
   - Description: there are some column in wrong datatype
   - Affected Column(s): gender,year,population
   - Example: gender should not be float64, but category
   year should not be float64, but integer.
   - Potential Impact: This can lead to incorrect data entries, resulting in inaccurate statistics.

6. **[outlier value]**
   - Description: there are some outlier in population column
   - Affected Column(s): population
   - Example: one of the row has 32930428000 population which is more than earth population
   - Potential Impact: Unreal population value cause mistakes on the analysis


### Issue 2: [Next Issue]
#### The technique used to address each issue and Justification
For **missing values**,since the quantity is small,  I chose to drop all rows containing missing values using .dropna()


For **incorrect category values**, I used .replace() to substitute the incorrect values with the correct ones.

For **unrealistic years**, I dropped all entries with years beyond 2024.
For **duplicate rows**, I removed them with .drop_duplicates()

For **incorrect data types**, I used .astype() to convert them to the correct types.

For **outliers**, I used .quantile() to identify and remove entries above the 99th percentile.


#### The impact of your cleaning on the dataset (e.g., number of rows affected/removed, changes in data distribution)
I deleted approximately 80,000 rows of data, with most deletions due to incorrect year values. I will explain what changed in Part 3.
#### Any assumptions you made
According to real world expectations, I assumed that the year values should go only up to 2024.

## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv
- **Rows**: 46695
- **Columns**: 5

#### missing value
find missing value of each column

```
income_groups    0
age              0
gender           0
year             0
population       0

```
#### check duplicated rows
check how many rows are duplicate

```
0
```
#### chceck unique value
income_groups
```
['high_income' 'low_income' 'lower_middle_income' 'upper_middle_income']
```
age:
```
[  0.   1.  10. 100.  11.  12.  13.  14.  15.  16.  17.  18.  19.   2.
  20.  21.  22.  23.  24.  25.  26.  27.  28.  29.   3.  30.  31.  32.
  33.  34.  35.  36.  37.  38.  39.   4.  40.  41.  42.  43.  44.  45.
  46.  47.  48.  49.   5.  50.  51.  52.  53.  54.  55.  56.  57.  58.
  59.   6.  60.  61.  62.  63.  64.  65.  66.  67.  68.  69.   7.  70.
  71.  72.  73.  74.  75.  76.  77.  78.  79.   8.  80.  81.  82.  83.
  84.  85.  86.  87.  88.  89.   9.  90.  91.  92.  93.  94.  95.  96.
  97.  98.  99.]
```
gender:
```
[1 3 2]
```
year:
```
[1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1961 1962 1964 1965
 1967 1968 1969 1970 1971 1972 1973 1975 1976 1978 1980 1981 1983 1984
 1986 1987 1988 1989 1991 1992 1993 1994 1996 1998 1999 2000 2001 2002
 2004 2005 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019
 2020 2021 2022 2023 2024 1960 1963 1966 1974 1977 1982 1985 1990 1995
 1997 2003 2006 2007 1979]
```
population:
```
[ 7798286  7739711  7713905 ... 18717600  3448269  7775405]
```

### Column Details
| Column Name    | Data Type | Non-Null Count |  Mean  |
|----------------|-----------|----------------|--------|
| income_groups  | object    | 46695          | [Mean] |
| age            | float64   | 46695          | 50.15  |
| gender         | int64     | 46695          | 1.58   |
| year           | int64     | 46695          | 1987   |
| population     | int64     | 46695          |9.62e+06|

### Summary of Changes
Compared to the original 125,718 rows, the cleaned dataframe now has only 46,695 rows. After cleaning, the missing values are zero, and there are no duplicated rows. Additionally, the average year decreased from 2025 to 1987, and the average population dropped from 111,000,000 to 9,620,000. This is undoubtedly closer to realistic values than before.

In this step, I learned the importance of data cleaning and the  identifying outliers.

I recommend investigating why there are so many entries with future years, as this is unusual and doesn't align with logical expectations.

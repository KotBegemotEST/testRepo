# -*- coding: utf-8 -*-
"""MilitaryPentel

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hw-X4GKH0IqUjJc5F1NVVd8LJR4RxhiO
"""

import pandas as pd
import matplotlib.pyplot as plt

url = 'SIPRI-Milex-data-1949-2022.xlsx'  # Замените на URL вашего файла, если он загружен в ваш Google Drive
data = pd.read_excel(url, sheet_name='Current US$', skiprows=5)

# Замена 'xxx' на NaN для последующего удаления
data = data.replace('xxx', pd.NA)

# Удаление строк, где все значения по годам отсутствуют
data = data.dropna(how='all', subset=[year for year in range(1949, 2023)])

# Проверка на некорректные типы данных и преобразование столбцов с годами в числовой формат
for year in range(1949, 2023):
    data[year] = pd.to_numeric(data[year], errors='coerce')  # Применяем 'coerce' для преобразования ошибок в NaN

# Удаление строк, где данные недоступны или некорректны после попытки конвертации
data = data.dropna(how='all', subset=[year for year in range(1949, 2023)])

print(data)

import pandas as pd
import matplotlib.pyplot as plt

url = 'SIPRI-Milex-data-1949-2022.xlsx'  # Замените на URL вашего файла, если он загружен в ваш Google Drive
data = pd.read_excel(url, sheet_name='Current US$', skiprows=5)

# Замена 'xxx' на NaN для последующего удаления
data = data.replace('xxx', pd.NA)

# Удаление строк, где все значения по годам отсутствуют
data = data.dropna(how='all', subset=[year for year in range(1949, 2023)])

# Проверка на некорректные типы данных и преобразование столбцов с годами в числовой формат
for year in range(1949, 2023):
    data[year] = pd.to_numeric(data[year], errors='coerce')  # Применяем 'coerce' для преобразования ошибок в NaN

# Удаление строк, где данные недоступны или некорректны после попытки конвертации
data = data.dropna(how='all', subset=[year for year in range(1949, 2023)])

# Список стран с наиболее полными данными
selected_countries = ['China', 'Myanmar', 'Indonesia', 'Taiwan', 'Korea, South', 'Korea, North',
                      'Japan', 'Sri Lanka', 'Pakistan', 'Nepal', 'India', 'Bangladesh', 'Afghanistan',
                      'Venezuela', 'Peru', 'Paraguay', 'Ecuador', 'Colombia', 'Chile', 'Bolivia',"United States of America"]

# Фильтрация данных только по выбранным странам
data = data[data['Country'].isin(selected_countries)]

print(data)

plt.figure(figsize=(14, 7))
for country in selected_countries:
    plt.plot(data.columns[2:], data[data['Country'] == country].iloc[0, 2:], label=country)

plt.title('Военные расходы по странам (1949-2022)')
plt.xlabel('Год')
plt.ylabel('Военные расходы (в млн. долларов США)')
plt.legend(title='Страна')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))

# Перебираем страны для построения графиков
for country in selected_countries:
    country_data = share_of_gdp_data[share_of_gdp_data['Country'] == country]

    # Проверяем, есть ли данные для страны
    if not country_data.empty:
        # Выбираем данные для графика
        years = [year for year in range(1949, 2023)]  # Используем числовые значения для годов
        data_values = country_data.iloc[0][years].values  # Извлекаем данные по годам

        # Построение графика, если есть данные
        if not pd.isna(data_values).all():
            plt.plot(years, data_values, label=country)  # Используем числовые значения годов для оси X

plt.title('Доля военных расходов от ВВП по странам (1949-2022)')
plt.xlabel('Год')
plt.ylabel('Доля от ВВП (%)')
plt.legend(title='Страна')
plt.xticks([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020], rotation=45)  # Указываем метки для оси X для удобства чтения
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Путь к файлу Excel
url = 'SIPRI-Milex-data-1949-2022.xlsx'

# Чтение данных о военных расходах в текущих долларах США
data = pd.read_excel(url, sheet_name='Current US$', skiprows=5)
data = data.replace('xxx', pd.NA)
data = data.dropna(how='all', subset=[year for year in range(1949, 2023)])
for year in range(1949, 2023):
    data[year] = pd.to_numeric(data[year], errors='coerce')
data = data.dropna(how='all', subset=[year for year in range(1949, 2023)])

# Чтение данных о доле военных расходов от ВВП
share_of_gdp_data = pd.read_excel(url, sheet_name='Share of GDP', skiprows=5)
share_of_gdp_data = share_of_gdp_data.replace('xxx', pd.NA)
share_of_gdp_data = share_of_gdp_data.dropna(how='all', subset=[year for year in range(1949, 2023)])
for year in range(1949, 2023):
    share_of_gdp_data[year] = pd.to_numeric(share_of_gdp_data[year], errors='coerce')
share_of_gdp_data = share_of_gdp_data.dropna(how='all', subset=[year for year in range(1949, 2023)])

# Список выбранных стран
selected_countries = ['China', 'Myanmar', 'Indonesia', 'Taiwan', 'Korea, South', 'Korea, North',
                      'Japan', 'Sri Lanka', 'Pakistan', 'Nepal', 'India', 'Bangladesh', 'Afghanistan',
                      'Venezuela', 'Peru', 'Paraguay', 'Ecuador', 'Colombia', 'Chile', 'Bolivia', "United States of America"]
data = data[data['Country'].isin(selected_countries)]
share_of_gdp_data = share_of_gdp_data[share_of_gdp_data['Country'].isin(selected_countries)]

# Визуализация военных расходов в долларах
plt.figure(figsize=(14, 7))
for country in selected_countries:
    country_data = data[data['Country'] == country]
    if not country_data.empty:
        plt.plot(country_data.columns[2:], country_data.iloc[0, 2:], label=country)
plt.title('Военные расходы по странам (1949-2022)')
plt.xlabel('Год')
plt.ylabel('Военные расходы (в млн. долларов США)')
plt.legend(title='Страна')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Визуализация доли военных расходов от ВВП
plt.figure(figsize=(14, 7))
for country in selected_countries:
    country_data = share_of_gdp_data[share_of_gdp_data['Country'] == country]
    if not country_data.empty:
        years = [year for year in range(1949, 2023)]
        data_values = country_data.iloc[0][years].values
        if not pd.isna(data_values).all():
            plt.plot(years, data_values, label=country)
plt.title('Доля военных расходов от ВВП по странам (1949-2022)')
plt.xlabel('Год')
plt.ylabel('Доля от ВВП (%)')
plt.legend(title='Страна')
plt.xticks([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020], rotation=45)
plt.grid(True)
plt.show()

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Предполагается, что данные уже загружены в переменную `data`
# Выбор данных за последние 5 лет (2018-2022)

data['mean_last_5_years'] = data[[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]].mean(axis=1)

# Подготовка данных для кластеризации
X = data[['mean_last_5_years']].dropna()  # Удаляем строки с отсутствующими значениями
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Нормализация данных

# Применение K-means
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_

# Добавление меток кластера к исходным данным
data['Cluster'] = pd.NA
data.loc[X.index, 'Cluster'] = labels

# Визуализация результатов кластеризации
plt.figure(figsize=(10, 6))
for label in set(labels):
    cluster_data = data[data['Cluster'] == label]
    plt.scatter(cluster_data['Country'], cluster_data['mean_last_5_years'], label=f'Cluster {label}')
plt.title('Кластеризация стран по военным расходам')
plt.xlabel('Страна')
plt.ylabel('Средние военные расходы (последние 5 лет)')
plt.xticks(rotation=90)
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
url = 'SIPRI-Milex-data-1949-2022.xlsx'  # Укажите актуальный путь к файлу
data = pd.read_excel(url, sheet_name='Current US$', skiprows=5)
data.replace('xxx', pd.NA, inplace=True)
for year in range(1949, 2023):
    data[year] = pd.to_numeric(data[year], errors='coerce')
data.dropna(how='all', subset=[year for year in range(1949, 2023)], inplace=True)

# Определение экономических блоков
economic_blocks = {
    'EU': ['Germany', 'France', 'Italy', 'Spain', 'Poland', 'Netherlands', 'Belgium', 'Sweden', 'Austria', 'Denmark', 'Finland', 'Greece', 'Ireland', 'Portugal'],
    'BRICS': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
    'Arab League': ['Egypt', 'Iraq', 'Jordan', 'Lebanon', 'Saudi Arabia', 'Yemen', 'Syria', 'Sudan', 'Morocco', 'Tunisia', 'Kuwait', 'Algeria', 'Libya', 'United Arab Emirates', 'Qatar', 'Bahrain', 'Oman', 'Mauritania', 'Somalia', 'Palestine', 'Djibouti', 'Comoros'],
    'UNASUR': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela'],
    'USA': ['United States of America']
}

# Присваивание блока каждой стране
data['Block'] = None  # Задаём начальное значение для новой колонки
for block, countries in economic_blocks.items():
    data.loc[data['Country'].isin(countries), 'Block'] = block

# Группировка данных по блокам и агрегирование
numeric_columns = [col for col in data.columns if isinstance(col, int)]
block_data = data.groupby('Block')[numeric_columns].mean().reset_index()

# Визуализация средних военных расходов по блокам для выбранного года
selected_year = 2022
plt.figure(figsize=(12, 8))
block_data.plot(x='Block', y=selected_year, kind='bar', legend=False)
plt.title(f'Средние военные расходы экономических блоков и США в {selected_year}')
plt.xlabel('Экономические блоки и США')
plt.ylabel('Средние военные расходы (млн USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
import pandas as pd
from sklearn.linear_model import LinearRegression


data = [{
    "carcount": 85,
    "Average CO2": 44.294117647058826,
    "date": "2023-02-11"
}, {
    "carcount": 85,
    "Average CO2": 51.4,
    "date": "2023-02-12"
}, {
    "carcount": 435,
    "Average CO2": 50.308045977011496,
    "date": "2023-02-13"
}, {
    "carcount": 85,
    "Average CO2": 52.11764705882353,
    "date": "2023-02-18"
}, {
    "carcount": 85,
    "Average CO2": 43.15294117647059,
    "date": "2023-02-19"
}, {
    "carcount": 85,
    "Average CO2": 51.529411764705884,
    "date": "2023-02-20"
}, {
    "carcount": 85,
    "Average CO2": 50.88235294117647,
    "date": "2023-02-21"
}, {
    "carcount": 85,
    "Average CO2": 46.77647058823529,
    "date": "2023-02-22"
}, {
    "carcount": 47,
    "Average CO2": 45.93617021276596,
    "date": "2023-02-23"
}, {
    "carcount": 90,
    "Average CO2": 49.18888888888889,
    "date": "2023-02-24"
}, {
    "carcount": 87,
    "Average CO2": 52,
    "date": "2023-02-25"
}, {"carcount": 85,
    "Average CO2": 44.294117647058826,
    "date": "2023-02-26"
    },
    {"carcount": 80,
     "Average CO2": 50.4,
     "date": "2023-02-27"
     },
    {"carcount": 95,
     "Average CO2": 49.308045977011496,
     "date": "2023-02-28"
     },
    {"carcount": 80,
     "Average CO2": 52.11764705882353,
     "date": "2023-03-01"
     },
    {"carcount": 80,
     "Average CO2": 42.15294117647059,
     "date": "2023-03-02"
     },
    {"carcount": 85,
     "Average CO2": 51.529411764705884,
     "date": "2023-03-03"
     },
    {"carcount": 90,
     "Average CO2": 50.88235294117647,
     "date": "2023-03-04"
     },
    {"carcount": 100,
     "Average CO2": 46.77647058823529,
     "date": "2023-03-05"
     },
    {"carcount": 95,
     "Average CO2": 45.93617021276596,
     "date": "2023-03-06"
     },
    {"carcount": 105,
     "Average CO2": 49.18888888888889,
     "date": "2023-03-07"
     },
    {"carcount": 110,
     "Average CO2": 52,
     "date": "2023-03-08"
     },
    {
        "carcount": 120,
        "Average CO2": 53.294117647058826,
        "date": "2023-03-09"
    }, {
        "carcount": 110,
        "Average CO2": 51.4,
        "date": "2023-03-10"
    }, {
        "carcount": 95,
        "Average CO2": 50.308045977011496,
        "date": "2023-03-11"
    }, {
        "carcount": 100,
        "Average CO2": 52.11764705882353,
        "date": "2023-03-12"
    }, {
        "carcount": 85,
        "Average CO2": 43.15294117647059,
        "date": "2023-03-13"
    }, {
        "carcount": 95,
        "Average CO2": 51.529411764705884,
        "date": "2023-03-14"
    }, {
        "carcount": 90,
        "Average CO2": 50.88235294117647,
        "date": "2023-03-15"
    }, {
        "carcount": 80,
        "Average CO2": 46.77647058823529,
        "date": "2023-03-16"
    }, {
        "carcount": 85,
        "Average CO2": 45.93617021276596,
        "date": "2023-03-17"
    }, {
        "carcount": 90,
        "Average CO2": 49.18888888888889,
        "date": "2023-03-18"
    }, {
        "carcount": 110,
        "Average CO2": 52,
        "date": "2023-03-19"
    }, {
        "carcount": 105,
        "Average CO2": 51.294117647058826,
        "date": "2023-03-20"
    }, {
        "carcount": 100,
        "Average CO2": 49.4,
        "date": "2023-03-21"
    }, {
        "carcount": 95,
        "Average CO2": 48.308045977011496,
        "date": "2023-03-22"
    }, {
        "carcount": 90,
        "Average CO2": 52.11764705882353,
        "date": "2023-03-23"
    }, {
        "carcount": 85,
        "Average CO2": 43.15294117647059,
        "date": "2023-03-24"
    }, {
        "carcount": 95,
        "Average CO2": 51.529411764705884,
        "date": "2023-03-25"
    }, {
        "carcount": 90,
        "Average CO2": 50.88235294117647,
        "date": "2023-03-26"
    }, {
        "carcount": 80,
        "Average CO2": 46.77647058823529,
        "date": "2023-03-27"
    }, {
        "carcount": 85,
        "Average CO2": 45.93617021276596,
        "date": "2023-03-28"
    }, {
        "carcount": 85,
        "Average CO2": 48.470588235294116,
        "date": "2023-03-29"
    }, {
        "carcount": 85,
        "Average CO2": 50.72941176470588,
        "date": "2023-03-30"
    }, {
        "carcount": 85,
        "Average CO2": 47.41764705882353,
        "date": "2023-03-31"
    }, {
        "carcount": 60,
        "Average CO2": 44.90833333333333,
        "date": "2023-04-01"
    }, {
        "carcount": 75,
        "Average CO2": 50.016666666666666,
        "date": "2023-04-02"
    }, {
        "carcount": 85,
        "Average CO2": 48.55882352941177,
        "date": "2023-04-03"
    }, {
        "carcount": 85,
        "Average CO2": 50.294117647058826,
        "date": "2023-04-04"
    }, {
        "carcount": 85,
        "Average CO2": 51.335294117647056,
        "date": "2023-04-05"
    }, {
        "carcount": 92,
        "Average CO2": 52.391304347826086,
        "date": "2023-04-06"
    }, {
        "carcount": 84,
        "Average CO2": 50.10294117647059,
        "date": "2023-04-07"
    }, {
        "carcount": 85,
        "Average CO2": 49.24705882352941,
        "date": "2023-04-08"
    }, {
        "carcount": 85,
        "Average CO2": 46.87058823529412,
        "date": "2023-04-09"
    }, {
        "carcount": 85,
        "Average CO2": 50.105882352941175,
        "date": "2023-04-10"
    }, {
        "carcount": 85,
        "Average CO2": 50.18235294117647,
        "date": "2023-04-11"
    }, {
        "carcount": 92,
        "Average CO2": 51.82608695652174,
        "date": "2023-04-12"
    }, {
        "carcount": 84,
        "Average CO2": 48.8235294117647,
        "date": "2023-04-13"
    }, {
        "carcount": 85,
        "Average CO2": 50.62352941176471,
        "date": "2023-04-14"
    }, {
        "carcount": 85,
        "Average CO2": 51.77647058823529,
        "date": "2023-04-15"
    }, {
        "carcount": 85,
        "Average CO2": 49.411764705882355,
        "date": "2023-04-16"
    }, {
        "carcount": 85,
        "Average CO2": 50.952941176470585,
        "date": "2023-04-17"
    }
]

df = pd.DataFrame(data)

total_carcount = 0

for item in data:
    total_carcount += item["carcount"]

average_carcount = total_carcount / len(data)
average_carcount = int(average_carcount)


df['dayofyear'] = pd.to_datetime(df['date']).dt.dayofyear


model = LinearRegression()
model.fit(df[['carcount', 'dayofyear']], df['Average CO2'])


future_carcount = average_carcount
future_dates = pd.date_range('2023-04-21', '2025-12-21', freq='D')
future_dayofyear = future_dates.dayofyear
future_predictions = model.predict(pd.DataFrame({'carcount': future_carcount, 'dayofyear': future_dayofyear}))


for date, prediction in zip(future_dates, future_predictions):
    print(f'{date.date()}: {prediction:.2f}')

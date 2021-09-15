import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'csvDir/sitka_weather_07-2014.csv'
# filename = 'csvDir/sitka_weather_2014.csv'
filename = 'csvDir/death_valley_2014.csv'
with open(filename) as f:
    # 创建一个与该文件相关联的阅读器
    reader = csv.reader(f)
    # next()返回文件中的下一行
    header_row = next(reader)
    # print(header_row)

    # # 打印文件头及其位置
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    # 从文件中获取最高气温
    # # 获取文件头
    # highs = []
    # for row in reader:
    #     # 将字符串转换为数字
    #     high = int(row[1])
    #     highs.append(high)
    # print(highs)

    # 存储从文件中提取的最高气温和日期
    dates, highs, lows = [], [], []
    for row in reader:
        # # 将包含日期信息的数据row[0]转换为datetime对象
        # current_date = datetime.strptime(row[0], "%Y-%m-%d")
        # dates.append(current_date)
        #
        # high = int(row[1])
        # highs.append(high)
        #
        # low = int(row[3])
        # lows.append(low)
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            # 打印缺失数据的日期
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', linewidth=1)
    plt.plot(dates, lows, c='blue', linewidth=1)
    # 给图标区域着色
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    plt.title("Daily high and low temperatures,July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature(F)", fontsize=16)
    # 绘制倾斜的日期标签
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

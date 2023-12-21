from date import time

# main関数の定義
def main():
   time_stamp = time.time_stamp()
   week_day = time.week_day()
   print("現在の日付と時刻:", time_stamp)
   print("今日の曜日:", week_day)
   
   # 平日チェッカー
   if week_day != "Sunday" or "Saturday":
     print("今日は平日です。")
   else:
      print("今日は休みです。")

# mainの実行部分
if __name__=="__main__":
   main()


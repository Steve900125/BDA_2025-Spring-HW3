# debug_4_1_patch.py
import pandas as pd
from Markowitz_2 import MyPortfolio, df
from quantstats import stats

# 1) 生成你的策略权重与回报
mp = MyPortfolio(df, "SPY")
weights, returns = mp.get_results()

# 2) 取出 SPY 与 MP 的回报序列
spy_ret = df.pct_change().fillna(0)["SPY"]
mp_ret  = returns["Portfolio"]

# 3) 构造 DataFrame
df_bl = pd.DataFrame({"SPY": spy_ret, "MP": mp_ret})

# 4) 将前 lookback 天剔除（这里 lookback=50）
lookback = mp.lookback
df_bl = df_bl.iloc[lookback:]

# 5) 再算一次 Sharpe
sr = stats.sharpe(df_bl)
print("剔除前 50 天后的 Sharpe：")
print(f"SPY = {sr['SPY']:.3f}")
print(f"MP  = {sr['MP']:.3f}")

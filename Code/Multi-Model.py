
import pandas as pd

df1 = pd.read_excel("/content/drive/MyDrive/Datasets/Curriculum_Results/Qwen3-0.6B/Model_Responses.xlsx")
df2 = pd.read_excel("/content/drive/MyDrive/Datasets/Curriculum_Results/Aragpt2-Base/Model_Responses.xlsx")
df3 = pd.read_excel("/content/drive/MyDrive/Datasets/Curriculum_Results/Aragpt2-Medium/Model_Responses.xlsx")
df4 = pd.read_excel("/content/drive/MyDrive/Datasets/Curriculum_Results/Dialect-ar-gpt-2021/Model_Responses.xlsx")
df5 = pd.read_excel("/content/drive/MyDrive/Datasets/Curriculum_Results/Bloomz/Model_Responses.xlsx")

dfs = [df1, df2, df3, df4, df5]

scores = pd.concat([df['bertscore'] for df in dfs], axis=1)
scores.columns = [0, 1, 2, 3, 4]
best_source = scores.idxmax(axis=1)

result = pd.concat(dfs).iloc[
    [i * len(df1) + row_idx for row_idx, i in enumerate(best_source)]
].reset_index(drop=True)

result.to_excel("/content/drive/MyDrive/Datasets/Curriculum_Results/Selective.xlsx", index=False)





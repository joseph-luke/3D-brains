# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

import plotly.io as pio
pio.renderers.default = "notebook_connected"
import plotly.express as px


# %%
# Import data for Slice 1
data_folder = Path("C:/Users/Josep/Documents/Work/Research/Engram Research/3D Brains/xy_coords_8754")
file_to_open1 = data_folder / "8754_1_area.txt"
file_to_open2 = data_folder / "8754_1_EYFP.txt"
file_to_open3 = data_folder / "8754_1_mKate2.txt"
file_to_open4 = data_folder / "8754_1_c-fos.txt"
file_to_open5 = data_folder / "8754_1_EYFP_mKate2.txt"
file_to_open6 = data_folder / "8754_1_EYFP_c-fos.txt"

df1 = pd.read_csv(file_to_open1, sep="\t", header=None)
df2 = pd.read_csv(file_to_open2, sep="\t", header=None)
df3 = pd.read_csv(file_to_open3, sep="\t", header=None)
df4 = pd.read_csv(file_to_open4, sep="\t", header=None)
df5 = pd.read_csv(file_to_open5, sep="\t", header=None)
df6 = pd.read_csv(file_to_open6, sep="\t", header=None)

frames = [df2, df3, df4, df5, df6]

for i in range(len(frames)):
     # if i == 0:
          # label_id = ["area"] * frames[i].shape[0]
          # frames[i]["label_id"] = label_id
     if i == 0:
          label_id = ["EYFP"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 1:
          label_id = ["mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 2:
          label_id = ["c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 3:
          label_id = ["EYFP_mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 4:
          label_id = ["EYFP_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id

merged_df1 = pd.concat(
    frames,
    axis=0,
    join="outer",
    ignore_index=True,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)

z = [0] * merged_df1.shape[0]

merged_df1["z"] = z
merged_df1["point_size"] = 5

# Fixing col names
merged_df1 = merged_df1.rename(columns={0: 'x', 1: 'y'})

col_order = ["x", "y", "z", "label_id", "point_size"]
merged_df1 = merged_df1[col_order]

for index, row in merged_df1.iterrows():
     if row['label_id'] in ["EYFP_mKate2", "EYFP_c-fos", "mKate2_c-fos", "Triple"]:
          merged_df1.loc[index, 'point_size'] = 15


#%%
# Slice 2
data_folder = Path("C:/Users/Josep/Documents/Work/Research/Engram Research/3D Brains/xy_coords_8754")
file_to_open1 = data_folder / "8754_2_area.txt"
file_to_open2 = data_folder / "8754_2_EYFP.txt"
file_to_open3 = data_folder / "8754_2_mKate2.txt"
file_to_open4 = data_folder / "8754_2_c-fos.txt"
file_to_open5 = data_folder / "8754_2_EYFP_mKate2.txt"
file_to_open6 = data_folder / "8754_2_EYFP_c-fos.txt"
file_to_open7 = data_folder / "8754_2_mKate2_c-fos.txt"

df1 = pd.read_csv(file_to_open1, sep="\t", header=None)
df2 = pd.read_csv(file_to_open2, sep="\t", header=None)
df3 = pd.read_csv(file_to_open3, sep="\t", header=None)
df4 = pd.read_csv(file_to_open4, sep="\t", header=None)
df5 = pd.read_csv(file_to_open5, sep="\t", header=None)
df6 = pd.read_csv(file_to_open6, sep="\t", header=None)
df7 = pd.read_csv(file_to_open7, sep="\t", header=None)

frames = [df2, df3, df4, df5, df6, df7]

for i in range(len(frames)):
     # if i == 0:
          # label_id = ["area"] * frames[i].shape[0]
          # frames[i]["label_id"] = label_id
     if i == 0:
          label_id = ["EYFP"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 1:
          label_id = ["mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 2:
          label_id = ["c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 3:
          label_id = ["EYFP_mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 4:
          label_id = ["EYFP_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 5:
          label_id = ["mKate2_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id

merged_df2 = pd.concat(
    frames,
    axis=0,
    join="outer",
    ignore_index=True,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)

z = [2] * merged_df2.shape[0]

merged_df2["z"] = z
merged_df2["point_size"] = 5

# Fixing col names
merged_df2 = merged_df2.rename(columns={0: 'x', 1: 'y'})

col_order = ["x", "y", "z", "label_id", "point_size"]
merged_df2 = merged_df2[col_order]

# Fixing the orientation for this slice
translation_factor = np.max(merged_df2["x"]) + np.min(merged_df2["x"])
merged_df2["x"] = [((-1 * x) + translation_factor) for x in merged_df2["x"]]

for index, row in merged_df2.iterrows():
     if row['label_id'] in ["EYFP_mKate2", "EYFP_c-fos", "mKate2_c-fos", "Triple"]:
          merged_df2.loc[index, 'point_size'] = 15

#%%
# Slice 3
data_folder = Path("C:/Users/Josep/Documents/Work/Research/Engram Research/3D Brains/xy_coords_8754")
file_to_open1 = data_folder / "8754_3_area.txt"
file_to_open2 = data_folder / "8754_3_EYFP.txt"
file_to_open3 = data_folder / "8754_3_mKate2.txt"
file_to_open4 = data_folder / "8754_3_c-fos.txt"
file_to_open5 = data_folder / "8754_3_EYFP_mKate2.txt"

df1 = pd.read_csv(file_to_open1, sep="\t", header=None)
df2 = pd.read_csv(file_to_open2, sep="\t", header=None)
df3 = pd.read_csv(file_to_open3, sep="\t", header=None)
df4 = pd.read_csv(file_to_open4, sep="\t", header=None)
df5 = pd.read_csv(file_to_open5, sep="\t", header=None)

frames = [df2, df3, df4, df5]

for i in range(len(frames)):
     # if i == 0:
          # label_id = ["area"] * frames[i].shape[0]
          # frames[i]["label_id"] = label_id
     if i == 0:
          label_id = ["EYFP"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 1:
          label_id = ["mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 2:
          label_id = ["c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 3:
          label_id = ["EYFP_mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 4:
          label_id = ["EYFP_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 5:
          label_id = ["mKate2_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id

merged_df3 = pd.concat(
    frames,
    axis=0,
    join="outer",
    ignore_index=True,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)

z = [4] * merged_df3.shape[0]

merged_df3["z"] = z
merged_df3["point_size"] = 5

# Fixing col names
merged_df3 = merged_df3.rename(columns={0: 'x', 1: 'y'})

col_order = ["x", "y", "z", "label_id", "point_size"]
merged_df3 = merged_df3[col_order]

# Fixing the orientation for this slice
# translation_factor = np.max(merged_df3["x"]) + np.min(merged_df3["x"])
# merged_df3["x"] = [((-1 * x) + translation_factor) for x in merged_df3["x"]]

for index, row in merged_df3.iterrows():
     if row['label_id'] in ["EYFP_mKate2", "EYFP_c-fos", "mKate2_c-fos", "Triple"]:
          merged_df3.loc[index, 'point_size'] = 15

#%%
# Slice 4
data_folder = Path("C:/Users/Josep/Documents/Work/Research/Engram Research/3D Brains/xy_coords_8754")
file_to_open1 = data_folder / "8754_4_area.txt"
file_to_open2 = data_folder / "8754_4_EYFP.txt"
file_to_open3 = data_folder / "8754_4_mKate2.txt"
file_to_open4 = data_folder / "8754_4_c-fos.txt"
file_to_open5 = data_folder / "8754_4_EYFP_mKate2.txt"
file_to_open6 = data_folder / "8754_4_EYFP_c-fos.txt"
file_to_open7 = data_folder / "8754_4_mKate2_c-fos.txt"

df1 = pd.read_csv(file_to_open1, sep="\t", header=None)
df2 = pd.read_csv(file_to_open2, sep="\t", header=None)
df3 = pd.read_csv(file_to_open3, sep="\t", header=None)
df4 = pd.read_csv(file_to_open4, sep="\t", header=None)
df5 = pd.read_csv(file_to_open5, sep="\t", header=None)
df6 = pd.read_csv(file_to_open6, sep="\t", header=None)
df7 = pd.read_csv(file_to_open7, sep="\t", header=None)

frames = [df2, df3, df4, df5, df6, df7]

for i in range(len(frames)):
     # if i == 0:
          # label_id = ["area"] * frames[i].shape[0]
          # frames[i]["label_id"] = label_id
     if i == 0:
          label_id = ["EYFP"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 1:
          label_id = ["mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 2:
          label_id = ["c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 3:
          label_id = ["EYFP_mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 4:
          label_id = ["EYFP_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 5:
          label_id = ["mKate2_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id

merged_df4 = pd.concat(
    frames,
    axis=0,
    join="outer",
    ignore_index=True,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)

z = [6] * merged_df4.shape[0]

merged_df4["z"] = z
merged_df4["point_size"] = 5

# Fixing col names
merged_df4 = merged_df4.rename(columns={0: 'x', 1: 'y'})

col_order = ["x", "y", "z", "label_id", "point_size"]
merged_df4 = merged_df4[col_order]

# Fixing the orientation for this slice
# translation_factor = np.max(merged_df4["x"]) + np.min(merged_df4["x"])
# merged_df4["x"] = [((-1 * x) + translation_factor) for x in merged_df4["x"]]


for index, row in merged_df4.iterrows():
     if row['label_id'] in ["EYFP_mKate2", "EYFP_c-fos", "mKate2_c-fos", "Triple"]:
          merged_df4.loc[index, 'point_size'] = 15

#%%
# Slice 5
data_folder = Path("C:/Users/Josep/Documents/Work/Research/Engram Research/3D Brains/xy_coords_8754")
file_to_open1 = data_folder / "8754_5_area.txt"
file_to_open2 = data_folder / "8754_5_EYFP.txt"
file_to_open3 = data_folder / "8754_5_mKate2.txt"
file_to_open4 = data_folder / "8754_5_c-fos.txt"
file_to_open5 = data_folder / "8754_5_EYFP_mKate2.txt"
file_to_open6 = data_folder / "8754_5_EYFP_c-fos.txt"
file_to_open7 = data_folder / "8754_5_mKate2_c-fos.txt"
file_to_open8 = data_folder / "8754_5_Triple.txt"

df1 = pd.read_csv(file_to_open1, sep="\t", header=None)
df2 = pd.read_csv(file_to_open2, sep="\t", header=None)
df3 = pd.read_csv(file_to_open3, sep="\t", header=None)
df4 = pd.read_csv(file_to_open4, sep="\t", header=None)
df5 = pd.read_csv(file_to_open5, sep="\t", header=None)
df6 = pd.read_csv(file_to_open6, sep="\t", header=None)
df7 = pd.read_csv(file_to_open7, sep="\t", header=None)
df8 = pd.read_csv(file_to_open7, sep="\t", header=None)

frames = [df2, df3, df4, df5, df6, df7, df8]

for i in range(len(frames)):
     # if i == 0:
          # label_id = ["area"] * frames[i].shape[0]
          # frames[i]["label_id"] = label_id
     if i == 0:
          label_id = ["EYFP"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 1:
          label_id = ["mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 2:
          label_id = ["c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 3:
          label_id = ["EYFP_mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 4:
          label_id = ["EYFP_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 5:
          label_id = ["mKate2_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 6:
          label_id = ["Triple"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     
merged_df5 = pd.concat(
    frames,
    axis=0,
    join="outer",
    ignore_index=True,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)

z = [8] * merged_df5.shape[0]

merged_df5["z"] = z
merged_df5["point_size"] = 5

# Fixing col names
merged_df5 = merged_df5.rename(columns={0: 'x', 1: 'y'})

col_order = ["x", "y", "z", "label_id", "point_size"]
merged_df5 = merged_df5[col_order]

# Fixing the orientation for this slice
# translation_factor = np.max(merged_df5["x"]) + np.min(merged_df5["x"])
# merged_df5["x"] = [((-1 * x) + translation_factor) for x in merged_df5["x"]]


for index, row in merged_df5.iterrows():
     if row['label_id'] in ["EYFP_mKate2", "EYFP_c-fos", "mKate2_c-fos", "Triple"]:
          merged_df5.loc[index, 'point_size'] = 15

#%%
# Slice 6
data_folder = Path("C:/Users/Josep/Documents/Work/Research/Engram Research/3D Brains/xy_coords_8754")
file_to_open1 = data_folder / "8754_6_area.txt"
file_to_open2 = data_folder / "8754_6_EYFP.txt"
file_to_open3 = data_folder / "8754_6_mKate2.txt"
file_to_open4 = data_folder / "8754_6_c-fos.txt"
file_to_open5 = data_folder / "8754_6_EYFP_mKate2.txt"
# No EYFP_c-fos
file_to_open7 = data_folder / "8754_6_mKate2_c-fos.txt"

df1 = pd.read_csv(file_to_open1, sep="\t", header=None)
df2 = pd.read_csv(file_to_open2, sep="\t", header=None)
df3 = pd.read_csv(file_to_open3, sep="\t", header=None)
df4 = pd.read_csv(file_to_open4, sep="\t", header=None)
df5 = pd.read_csv(file_to_open5, sep="\t", header=None)

df7 = pd.read_csv(file_to_open7, sep="\t", header=None)

frames = [df2, df3, df4, df5, df7]

for i in range(len(frames)):
     # if i == 0:
          # label_id = ["area"] * frames[i].shape[0]
          # frames[i]["label_id"] = label_id
     if i == 0:
          label_id = ["EYFP"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 1:
          label_id = ["mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 2:
          label_id = ["c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 3:
          label_id = ["EYFP_mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id


     if i == 4:
          label_id = ["mKate2_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id

merged_df6 = pd.concat(
    frames,
    axis=0,
    join="outer",
    ignore_index=True,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)

z = [10] * merged_df6.shape[0]

merged_df6["z"] = z
merged_df6["point_size"] = 5

# Fixing col names
merged_df6 = merged_df6.rename(columns={0: 'x', 1: 'y'})

col_order = ["x", "y", "z", "label_id", "point_size"]
merged_df6 = merged_df6[col_order]

# Fixing the orientation for this slice
translation_factor = np.max(merged_df6["x"]) + np.min(merged_df6["x"])
merged_df6["x"] = [((-1 * x) + translation_factor) for x in merged_df6["x"]]


for index, row in merged_df6.iterrows():
     if row['label_id'] in ["EYFP_mKate2", "EYFP_c-fos", "mKate2_c-fos", "Triple"]:
          merged_df6.loc[index, 'point_size'] = 15

#%%
# Slice 7
data_folder = Path("C:/Users/Josep/Documents/Work/Research/Engram Research/3D Brains/xy_coords_8754")
file_to_open1 = data_folder / "8754_7_area.txt"
file_to_open2 = data_folder / "8754_7_EYFP.txt"
file_to_open3 = data_folder / "8754_7_mKate2.txt"
file_to_open4 = data_folder / "8754_7_c-fos.txt"
file_to_open5 = data_folder / "8754_7_EYFP_mKate2.txt"
file_to_open6 = data_folder / "8754_7_EYFP_c-fos.txt"
file_to_open7 = data_folder / "8754_7_mKate2_c-fos.txt"

df1 = pd.read_csv(file_to_open1, sep="\t", header=None)
df2 = pd.read_csv(file_to_open2, sep="\t", header=None)
df3 = pd.read_csv(file_to_open3, sep="\t", header=None)
df4 = pd.read_csv(file_to_open4, sep="\t", header=None)
df5 = pd.read_csv(file_to_open5, sep="\t", header=None)
df6 = pd.read_csv(file_to_open6, sep="\t", header=None)
df7 = pd.read_csv(file_to_open7, sep="\t", header=None)

frames = [df2, df3, df4, df5, df6, df7]

for i in range(len(frames)):
     # if i == 0:
          # label_id = ["area"] * frames[i].shape[0]
          # frames[i]["label_id"] = label_id
     if i == 0:
          label_id = ["EYFP"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 1:
          label_id = ["mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 2:
          label_id = ["c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 3:
          label_id = ["EYFP_mKate2"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 4:
          label_id = ["EYFP_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id
     if i == 5:
          label_id = ["mKate2_c-fos"] * frames[i].shape[0]
          frames[i]["label_id"] = label_id

merged_df7 = pd.concat(
    frames,
    axis=0,
    join="outer",
    ignore_index=True,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)

z = [12] * merged_df7.shape[0]

merged_df7["z"] = z
merged_df7["point_size"] = 5

# Fixing col names
merged_df7 = merged_df7.rename(columns={0: 'x', 1: 'y'})

col_order = ["x", "y", "z", "label_id", "point_size"]
merged_df7 = merged_df7[col_order]

# Fixing the orientation for this slice
translation_factor = np.max(merged_df7["x"]) + np.min(merged_df7["x"])
merged_df7["x"] = [((-1 * x) + translation_factor) for x in merged_df7["x"]]

for index, row in merged_df7.iterrows():
     if row['label_id'] in ["EYFP_mKate2", "EYFP_c-fos", "mKate2_c-fos", "Triple"]:
          merged_df7.loc[index, 'point_size'] = 15

#%%
# Merge all dfs
all_frames = [merged_df1, merged_df2, merged_df3, merged_df4, merged_df5,
              merged_df6, merged_df7]

full_merged_df = pd.concat(
    all_frames,
    axis=0,
    join="outer",
    ignore_index=True,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)


# %%
# Generate 3D data
x = full_merged_df.iloc[:,0]
y = full_merged_df.iloc[:,1]
z = full_merged_df.loc[:,"z"]

group_color = {'EYFP': 'rgb(38, 155, 63, 0.4)',
               'mKate2': 'rgb(251, 0, 12, 0.4)',
               'c-fos': 'rgb(212, 9, 218, 0.4)',
               'EYFP_mKate2': 'rgb(255, 161, 90, 1)',
               'EYFP_c-fos': 'rgb(102, 102, 102, 1)',
               'mKate2_c-fos': 'rgb(160, 35, 94, 1)',
               'Triple': 'rgb(255, 250, 20, 1)'}

# Initialize figure
fig = px.scatter_3d(x=x,
                    y=y,
                    z=z,
                    color=full_merged_df.loc[:,"label_id"],
                    color_discrete_map=group_color,
                    size=full_merged_df.loc[:,"point_size"])

# Show figure (tight)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()


# Export figure to html
fig.write_html("8754_3D_Brain.html", include_plotlyjs='cdn')

#%%
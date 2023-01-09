#%%
import pandas as pd

#%%
title_image = pd.read_csv('title_imageName_rename_dict.csv', index_col=0)
title_image_dict = dict(zip(title_image.index, title_image['col2']))

title_som = pd.read_csv('title_som_result20230107_105041.csv', index_col=0)

#%%
print(title_image_dict)
# %%
print(title_som.index[0])


# %%
image_name_list = ['col1']
for i in title_som.index:
    if i != '-1':
        image_name = title_image_dict[i]
    else:
        image_name = '1'
    image_name_list.append(image_name)
#%%
print(image_name_list)
# %%
#%%
import csv

f = open('title_som_result' + '.csv', 'w')
writer = csv.writer(f)
for i in image_name_list:
    writer.writerow([i])
f.close()
# %%

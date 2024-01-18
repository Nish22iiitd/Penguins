# %%
import seaborn as sns
import pandas as pd
# Load the Penguins dataset from seaborn
pengunis_df=sns.load_dataset('penguins')
# %%
print("First 5 rows of Penguins dataset:")
print(pengunis_df.head())
# %%
pengunis_df.head()
# %%
# Calculate the average 'bill_length_mm' for each species of penguins
avg_bill_len_by_species=pengunis_df.groupby('species')['bill_length_mm'].mean()
print(avg_bill_len_by_species)
# %%
# Find the penguin with the highest 'body_mass_g' and display its species and other information
highest_body_mass=pengunis_df.loc[pengunis_df['body_mass_g'].idxmax()]
print("\nPenguin with the highest 'body_mass_g':")
print(highest_body_mass)
# %%
# Create a new DataFrame containing only the penguins with 'sex' as 'MALE' and 'island' as 'Torgersen'
male_torgersen_peng=pengunis_df[(pengunis_df['sex']=='Male') & (pengunis_df['island']=='Torgersen')]
print("\nDataFrame containing penguins with 'sex' as 'MALE' and 'island' as 'Torgersen':")
print(male_torgersen_peng)
# %%
male_torgersen_peng
# %%
# Calculate the correlation matrix for 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', and 'body_mass_g'.
corr_mat=pengunis_df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].corr()
print(corr_mat)
# %%
corr_mat
# %%
# For each species of penguins, find the mean, median, minimum, and maximum 'body_mass_g'.
species_body_mass_sts=pengunis_df.groupby('species')['body_mass_g'].agg(['mean', 'median', 'min', 'max'])
print("\nBody mass statistics for each species of penguins:")
print(species_body_mass_sts)
# %%
species_body_mass_sts
# %%
# Replace any missing values in the 'sex' column with the most frequent value in that column.
most_freq_sex=pengunis_df['sex'].mode().iloc[0]
pengunis_df['sex'].fillna(most_freq_sex,inplace=True)

# %%
pengunis_df.head()
# %%
# Create a new column in the DataFrame called 'bill_area', which is the product of 'bill_length_mm' and 'bill_depth_mm'.
pengunis_df['bill_area']=pengunis_df['bill_length_mm']*pengunis_df['bill_depth_mm']
pengunis_df.head()
# %%
mean_bill_area=pengunis_df['bill_area'].mean()
pengunis_df['bill_area'].fillna(mean_bill_area,inplace=True)
pengunis_df.head()
# %%
# Group the DataFrame by 'species' and calculate the average 'body_mass_g' and 'flipper_length_mm' for each species.
species_frouped_sts=pengunis_df.groupby('species').agg({'body_mass_g': 'mean', 'flipper_length_mm': 'mean'})
print("\nAverage 'body_mass_g' and 'flipper_length_mm' for each species:")
print(species_body_mass_sts)
# %%
species_body_mass_sts
# %%
# Calculate the total count of penguins for each 'island' and 'sex' combination.
peng_cnt_by_island_sex=pengunis_df.groupby(['island', 'sex']).size().reset_index(name='count')
print("\nTotal count of penguins for each 'island' and 'sex' combination:")
print(peng_cnt_by_island_sex)
# %%
peng_cnt_by_island_sex
# %%
pengunis_df.to_csv('penguins.csv')
# %%

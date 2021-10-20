import pandas as pd
df = pd.read_csv("CreditSesame_Postlogs_wk06.28.2021 - wk09.13.2020.csv")
df.set_index('master', append=True, inplace=True)
data_agg_df['daily'] = 'daily'
data_agg_df.set_index('daily', append=True, inplace=True)

    # crear nuvo df con informacion de los anteriores y eliminar duplicados
merged = db_redshift.append(data_agg_df)
merged = merged.drop_duplicates().sort_index()

outp_df = pd.IndexSlice
# salida
df = (merged.loc[outp_df[:, 'daily'], :])

df = df.rename(columns={'Media Outlet': 'media_outlet',
                        'media outlet': 'media_outlet',
                        'Program Title': 'program_title',
                        'Attributes': 'attributes',
                        'Feed': 'feed',
                        'Length': 'length',
                        'Ad': 'ad',
                        'Estimated Date': 'estimated_date',
                        'Estimated Time': 'estimated_time',
                        'Gross Rate': 'gross_rate',
                        'Client Net Rate': 'client_net_rate'})


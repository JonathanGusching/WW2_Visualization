import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['axes.facecolor'] = '#bebebe'


def dataframe_preprocess(df):
    df.loc[df["Target Country"] == "JAPAN","Target Country"] = "JAPAN AND SURROUNDING ISLANDS"
    df.loc[df["Target Country"] == "JAPAN MINING","Target Country"] = "JAPAN AND SURROUNDING ISLANDS"
    df.loc[df["Target Country"] == "KURILE ISLANDS","Target Country"] = "JAPANESE POSSESSIONS"
    df.loc[df["Target Country"] == "CELEBES ISLANDS","Target Country"] = "JAPANESE POSSESSIONS"
    df.loc[df["Target Country"] == "PHILIPPINE ISLANDS","Target Country"] = "JAPANESE POSSESSIONS"
    df.loc[df["Target Country"] == "PALAU ISLANDS","Target Country"] = "JAPANESE POSSESSIONS"
    df.loc[df["Target Country"] == "SOLOMON ISLANDS","Target Country"] = "NEW GUINEA"
    df.loc[df["Target Country"] == "CORAL SEA AREA","Target Country"] = "JAPANESE POSSESSIONS"
    df.loc[df["Target Country"] == "MARIANAS ISLANDS","Target Country"] = "JAPANESE POSSESSIONS"
    df.loc[df["Target Country"] == "CAROLINE ISLANDS","Target Country"] = "JAPANESE POSSESSIONS"
    df.loc[df["Target Country"] == "MARSHALL ISLANDS","Target Country"] = "JAPANESE POSSESSIONS"
    df.loc[df["Target Country"] == "ALEUTIAN ISLANDS","Target Country"] = "JAPAN AND SURROUNDING ISLANDS"

    df.loc[df["Target Country"] == "INDONESIA","Target Country"] = "DUTCH EAST INDIES"
    df.loc[df["Target Country"] == "BALI","Target Country"] = "DUTCH EAST INDIES"
    df.loc[df["Target Country"] == "SUMATRA MINING","Target Country"] = "DUTCH EAST INDIES"
    df.loc[df["Target Country"] == "BORNEO","Target Country"] = "DUTCH EAST INDIES"
    df.loc[df["Target Country"] == "JAVA","Target Country"] = "DUTCH EAST INDIES"
    df.loc[df["Target Country"] == "MALAY STATES MINING","Target Country"] = "DUTCH EAST INDIES"
    df.loc[df["Target Country"] == "MALAY STATES","Target Country"] = "DUTCH EAST INDIES"
    df.loc[df["Target Country"] == "SUMATRA","Target Country"] = "DUTCH EAST INDIES"
    df.loc[df["Target Country"] == "TIMOR","Target Country"] = "DUTCH EAST INDIES"
    df.loc[df["Target Country"] == "NETHERLANDS EAST INDIES","Target Country"] = "DUTCH EAST INDIES"

    df.loc[df["Target Country"] == "FORMOSA AND RYUKYU ISLANDS","Target Country"] = "JAPAN AND SURROUNDING ISLANDS"
    df.loc[df["Target Country"] == "FORMOSA","Target Country"] = "JAPAN AND SURROUNDING ISLANDS"
    df.loc[df["Target Country"] == "VOLCANO AND BONIN ISLANDS","Target Country"] = "JAPAN AND SURROUNDING ISLANDS"

    df.loc[df["Target Country"] == "MANCHURIA","Target Country"] = "JAPANESE MANCHURIA & KOREA"
    df.loc[df["Target Country"] == "KOREA OR CHOSEN MINING","Target Country"] = "JAPANESE MANCHURIA & KOREA"
    df.loc[df["Target Country"] == "KOREA OR CHOSEN","Target Country"] = "JAPANESE MANCHURIA & KOREA"

    df.loc[df["Target Country"] == "EGYPT","Target Country"] = "EGYPT & SUDAN"
    df.loc[df["Target Country"] == "SUDAN","Target Country"] = "EGYPT & SUDAN"

    df.loc[df["Target Country"] == "SICILY","Target Country"] = "ITALY"
    df.loc[df["Target Country"] == "ETHIOPIA/ABSINNYA","Target Country"] = "ITALIAN AFRICA"
    df.loc[df["Target Country"] == "ETHIOPIA","Target Country"] = "ITALIAN AFRICA"
    df.loc[df["Target Country"] == "LIBYA","Target Country"] = "ITALIAN AFRICA"
    df.loc[df["Target Country"] == "ERITREA","Target Country"] = "ITALIAN AFRICA"
    df.loc[df["Target Country"] == "SOMALIA","Target Country"] = "ITALIAN AFRICA"

    df.loc[df["Target Country"] == "SYRIA","Target Country"] = "FRENCH MANDATE IN SYRIA"
    df.loc[df["Target Country"] == "LEBANON","Target Country"] = "FRENCH MANDATE IN SYRIA"

    df.loc[df["Target Country"] == "CORSICA","Target Country"] = "FRANCE"

    df.loc[df["Target Country"] == "BELGIUM","Target Country"] = "BENELUX"
    df.loc[df["Target Country"] == "LUXEMBOURG","Target Country"] = "BENELUX"
    df.loc[df["Target Country"] == "HOLLAND OR NETHERLANDS","Target Country"] = "BENELUX"


    df.loc[df["Target Country"] == "BISMARK ARCHIPELAGO","Target Country"] = "PAPUA NEW GUINEA"
    df.loc[df["Target Country"] == "BOUGAINVILLE","Target Country"] = "PAPUA NEW GUINEA"
    df.loc[df["Target Country"] == "PAPUA NEW GUINEA","Target Country"] = "PAPUA NEW GUINEA"
    df.loc[df["Target Country"] == "MANUS ISLAND","Target Country"] = "PAPUA NEW GUINEA"
    df.loc[df["Target Country"] == '"PAPUA NEW GUINEA, MANUS ISLAND"',"Target Country"] = "PAPUA NEW GUINEA"

    df.loc[df["Target Country"] == "UNKNOWN","Target Country"] = "UNKNOWN OR NOT INDICATED"
    df.loc[df["Target Country"] == "UNSPECIFIED","Target Country"] = "UNKNOWN OR NOT INDICATED"

    df.loc[df["Target Country"] == "TUNISIA","Target Country"] = "MAGHREB"
    df.loc[df["Target Country"] == "ALGERIA","Target Country"] = "MAGHREB"
    df.loc[df["Target Country"] == "MOROCCO","Target Country"] = "MAGHREB"

    df.loc[df["Target Country"] == "THAILAND OR SIAM MINING","Target Country"] = "THAILAND OR SIAM"
    df.loc[df["Target Country"] == "FRENCH INDO CHINA MINING","Target Country"] = "FRENCH INDO CHINA"

    df.loc[df["Target Country"] == "MARCUS ISLANDS","Target Country"] = "JAPAN AND SURROUNDING ISLANDS"

    df.loc[df["Target Country"] == "NORWAY","Target Country"] = "DENMARK, NORWAY"
    df.loc[df["Target Country"] == "DENMARK","Target Country"] = "DENMARK, NORWAY"

    df.loc[df["Target Country"] == "TURKEY","Target Country"] = "TURKEY, CYPRUS"
    df.loc[df["Target Country"] == "CYPRUS","Target Country"] = "TURKEY, CYPRUS"

    df.loc[df["Target Country"] == "CRETE","Target Country"] = "GREECE"

    df.loc[df["Target Country"] == "GILBERT ISLANDS","Target Country"] = "BRITISH/AMERICAN PACIFIC ISLANDS"
    df.loc[df["Target Country"] == "WAKE ISLAND","Target Country"] = "BRITISH/AMERICAN PACIFIC ISLANDS"

    df.loc[df["Target Country"] == "ANDAMAN ISLANDS","Target Country"] = "INDIA"
    df.loc[df["Target Country"] == "INDIAN OCEAN","Target Country"] = "INDIA"


    df.loc[df["Target Country"] == "CHINA MINING","Target Country"] = "CHINA"


    df.loc[df["Target Country"] == "SARDINIA","Target Country"] = "ITALY"
    df.loc[df["Target Country"] == "PANTELLARIA","Target Country"] = "ITALY"

    print((df["Target Country"].unique()))

def get_clean_df(df):
    return df[~(df['Country'].eq('AUSTRALIA')) & ~(df['Country'].eq('SOUTH AFRICA')) & ~(df['Country'].eq('NEW ZEALAND'))]


def plot_aircraft(df):
    sns.countplot(x=df["Aircraft Series"], order=df["Aircraft Series"].value_counts().index,
                  hue=df["Theater of Operations"])
    plt.title(
        "Number of bombing operations per plane category between 1939 and 1945 and all theaters of operation by USAF and RAF")
    plt.xlabel("Plane family")
    plt.ylabel("Number of bombing operations")
    plt.xticks(rotation=70)
    plt.show()

def plot_targets(df):
    df_targets = get_clean_df(df)
    df_targets.fillna("UNKNOWN OR NOT INDICATED", inplace=True)
    sns.countplot(x=df_targets["Target Country"], order=df_targets["Target Country"].value_counts().index,
                  hue=df_targets["Country"], palette=["#1338be", "#990f02", "#545454"])
    plt.title("Count of targets per country between 1939 and 1945 and all theaters of operation by USAF and RAF")
    plt.grid()
    plt.xlabel("Targeted country")
    plt.ylabel("Number of bombing operations")
    plt.xticks(rotation=90)
    plt.show()

def plot_airborne(df):
    print(np.sum(df["Airborne Aircraft"] < 0))
    # sns.kdeplot(data=df, x="Airborne Aircraft")
    sns.histplot(data=df, kde=True, stat="density", x="Airborne Aircraft", fill=True, hue="Mission Type",
                 multiple="dodge")
    plt.show()

def num_of_operations(df):
    sns.countplot(x=df["Country"], order=df["Country"].value_counts().index, hue=df["Theater of Operations"])
    plt.title("Number of operations per country between 1939 and 1945")
    plt.xlabel("Country")
    plt.ylabel("Count of bombing operations")
    plt.xticks(rotation=90)
    plt.show()

def plot_bombs(df):
    df_targets = get_clean_df(df)

    df2 = df_targets.groupby('Target Country', as_index=False)['Total Weight (Tons)'].sum()
    order = df_targets.groupby('Target Country', as_index=False)['Total Weight (Tons)'].sum().sort_values(["Total Weight (Tons)"], ascending=False)["Target Country"]
    p = sns.barplot('Target Country', 'Total Weight (Tons)',data=df2, ci=False, order = order)


    plt.title("Count of targets per country between 1939 and 1945 and all theaters of operation by USAF and RAF")
    plt.grid()
    plt.xlabel("Targeted country")
    plt.ylabel("Total Weight of bombs dropped by USAF and RAF (Tons)")

    plt.xticks(rotation=90)
    plt.show()

def plot_cities_france(df):
    df2 = df[df["Target Country"] == "FRANCE"].groupby('Target City', as_index=False)['Total Weight (Tons)'].sum()
    df2.to_csv("france.csv", index=False)
    df3 = (df2[df2["Total Weight (Tons)"] > 1500])
    order = df3.groupby('Target City', as_index=False)['Total Weight (Tons)'].sum().sort_values(
        ["Total Weight (Tons)"], ascending=False)["Target City"]
    print(df3[df3["Target City"]=="LE HAVRE"])
    #print(order)

    p = sns.barplot('Target City', 'Total Weight (Tons)', data=df3, order=order)

    plt.title("Count of targets per French city between 1939 and 1945 by USAF and RAF")
    plt.grid()
    plt.xlabel("Target City")
    plt.ylabel("Total Weight of bombs dropped by USAF and RAF (Tons)")
    plt.xticks(rotation=90)

    plt.show()


df = pd.read_csv("operations.csv", na_values=' ')
print(df.columns)
plot_cities_france(df)


dataframe_preprocess(df)

plot_bombs(df)


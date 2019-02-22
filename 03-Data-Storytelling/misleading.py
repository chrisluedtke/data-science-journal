# Data from National Association of Insurance Commissioners
# https://www.naic.org/prod_serv_alpha_listing.htm

import pandas as pd

insurance = pd.DataFrame(
    index=['State Farm', 'GEICO'], 
    data={'Market Share %': [18.07, 12.79]})


def plot1():
    return insurance.plot.bar(ylim=(10, 20))


def plot2():
    return insurance.plot.pie('Market Share %', figsize=(5, 5))

def plot3():
    # Based on https://altair-viz.github.io/gallery/choropleth_repeat.html
    import altair as alt
    from vega_datasets import data

    url = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-1-Sprint-3-Data-Storytelling/master/module2-choose-appropriate-visualizations/direct_written_premium_by_state_by_group_private_passenger_auto.csv'
    df = pd.read_csv(url)
    df.rename(columns={'STATE FARM GRP': 'State Farm policy premiums'}, inplace=True)
    variable = 'State Farm policy premiums'

    states = alt.topo_feature(data.us_10m.url, 'states')

    return alt.Chart(states).mark_geoshape().encode(
        alt.Color(variable, type='quantitative')
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(df, 'id', [variable])
    ).properties(
        width=500,
        height=300
    ).project(
        type='albersUsa'
    )


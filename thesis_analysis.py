import matplotlib.pyplot as plt
import pandas as pd
# A function for  the creation, management, and process of the thesis's dataframes
def data_setting(data,table_no,hw_no=69,sw_no=72,calc_percent=False):
    df=pd.DataFrame(data)
    print(f'\n---The table for the{table_no}st set of data:---\n')

    #if the table requires calculating the percentages for the data
    if calc_percent:
        # It is supposed that the columns for the row data are named as 'Hardware' and 'Software'
        # The calculation of percentages of Hardware and Software groups for further comparisons
        # The 'round(2)' func is used to round the percentages to two decimal places for a cleaner look
        df['Hardware_Percentage'] =  ((df['Hardware']/hw_no)*100).round(2)
        df['Software_Percentage'] = ((df['Software'] / sw_no) * 100).round(2)

    # For displaying dataframes in full, especially wide ones with many columns
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    return df

def draw_bar_chart(df,x_axis,chart_title,showfile_name):
    df.plot(x=x_axis, kind='bar', figsize=(9,6))
    plt.title(chart_title, fontsize=14, fontweigth='bold')
    #the rotation of titles of the long rows for more readability
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig(showfile_name, dpi=300)
    plt.show()


# Filling the first dataframe with data for the table 4.1 of my thesis
data_table1= {
    'En_project_participation': ['Missing', 'Yes' , 'No'],
     'Hardware': [0,26,44],
     'Software': [0,40,32]
              }
# Filling the second dataframe for the table 4.3 of my thesis
data_table3={
    'Ability_perceptions':['Listening','Listening',
                           'Speaking','Speaking',
                           'Reading','Reading',
                           'Writing','Writing',
                           'Translation_P_E','Translation_P_E',
                           'Translation_E_P','Translation_E_P',
                           'vocab_use','vocab_use'
                           ],

    'Group':[
                            'Hardware','Software',
                            'Hardware','Software',
                            'Hardware','Software',
                            'Hardware','Software',
                            'Hardware','Software',
                            'Hardware','Software',
                            'Hardware','Software'
            ],
    'Very_Little(%)':[31.4,8.3,22.9,16.7,12.9,6.9,25.7,19.4,17.1,9.7,10.0,5.6,15.7,6.9],
     'Little(%)':[7.1,13.9,24.3,19.4,7.1,12.5,22.9,15.3,22.9,22.2,12.9,15.3,28.6,13.9],
     'Moderate(%)':[31.4,48.6,28.6,50.0,41.4,38.9,27.1,43.1,28.6,31.9,35.7,27.8,34.3,40.3],
     'A_Lot(%)':[20.0,16.7,17.1,4.2,25.7,27.8,18.6,19.4,21.4,29.2,31.4,37.5,17.1,26.4],
      'Very_Much(%)':[10.0,12.5,7.1,9.7,12.9,13.9,5.7,2.8,10.0,6.9,10.0,13.9,4.3,12.5]
}
#calling the functions for the first dataframe
df1=data_setting(data_table1,1,calc_percent=True)
print(df1)

draw_bar_chart(
    df=df1,
    x_axis='En_project_participation',
    chart_title='Table 4.1:English Project Participation',
    showfile_name='Table_4_1_chart.png'
)

# The table 4.3 does not include row data to calculate percentages; that is why I used the pre-set 'False' value for the 'calc_percent variable
df3=data_setting(data_table3,3)
print(df3)

draw_bar_chart(
    df=df3,
    x_axis='Ability Perceptions',
    chart_title='Table 4.3: Perceptions of Ability Dealing with Language Skills',
    showfile_name='Table_4_3_chart.png'
)



import pandas as pd
import chartify

data = chartify.examples.example_data()


total_quantity_by_month_and_fruit = (data.groupby([data['date'] + pd.offsets.MonthBegin(-1),'fruit'])['quantity'].sum().reset_index().rename(columns = {'date' : 'month'}).sort_values('month').sort_values('month'))
print(total_quantity_by_month_and_fruit.head())


ch = chartify.Chart(blank_labels = True, x_axis_type = 'datetime')
ch.set_title("Stacked area")
ch.set_subtitle("Represent changes in distribution.")
ch.plot.area(
        data_frame = total_quantity_by_month_and_fruit,
        x_column = 'month',
        y_column = 'quantity',
        color_column = 'fruit',
        stacked = True
        )
ch.show('png')

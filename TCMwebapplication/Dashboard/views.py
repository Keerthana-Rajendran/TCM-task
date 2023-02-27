from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure
from CustomerData.models import Customer_data
from datetime import datetime, timedelta
from django.db.models import Count
from django.db.models.functions import TruncDay

def line_chart(request):
    # create some data
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)
    sales_by_date  = Customer_data.objects.all() \
                          .annotate(date=TruncDay('Revisit_date')) \
                          .values('date') \
                          .annotate(total=Count('id')) \
                          .order_by('date')
    x = []
    y = []

    # Create the x and y values for the chart
    x = [str(purchase['date']) for purchase in sales_by_date]
    y = [purchase['total'] for purchase in sales_by_date]
    # convert x to datetime object
    x = [datetime.strptime(d, '%Y-%m-%d') for d in x]

    # create ColumnDataSource
    source = ColumnDataSource(data=dict(x=x, y=y))
    print(x)
    print(y)
    # create figure
    p = figure(title="Sales Chart", x_axis_type='datetime')

    # add line
    p.line(x='x', y='y', source=source, line_width=2)

    # add x-axis label
    p.xaxis.axis_label = "Date"

    # add y-axis label
    p.yaxis.axis_label = "Count"

    # add x-axis formatter
    p.xaxis.formatter = DatetimeTickFormatter(days="%m/%d")

    # add grid
    p.grid.grid_line_alpha = 0.3
    script, div = components(p, CDN)
    context = {'script': script, 'div': div}
    return render(request, 'Dashboard/customer_dashboard.html', context)

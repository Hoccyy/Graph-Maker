import os
import numpy as np
from csv import writer
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

'''
Additional columns can be made as an option, but appropriate alterations must be made to other functions
- Empties the logs file in case you need more space etc.
- Can also be used to initialize an empty log if none exist

Args:
    column_names (list): A list of all the column headers (best left empty)
'''
def clear_logs(column_names: list = ['filename', 'date created']):
    with open ('logs.csv', 'w') as logs_file:
        writer_obj = writer(logs_file)
        writer_obj.writerow(column_names)

'''
Parameters must either be of size 1 or equal to data array size

Args:
    graph_max_vals (list): The maximum X and Y values of the graph
    data_label_x (str): Text label for the X-axis
    data_label_y (str): Text label for the Y-axis
    title (str): Title of the graph
    x_axis_data (list): Data to include in the X-axis
    y_axis_data (list): Data to include in the Y-axis
    size_of_plots (list): Size of the plot points, size is 1 or equal to array size
    plot_color (list): Color for all or each plot point
    chart_file_type (str): Saves the graph in file form of PNG, JPEG, or PDF (Default)

Returns:
    Error message in the event of a failure and an int (1)
'''
def show_graph(graph_max_vals: list = [20,20], data_label_x: str = 'Data', data_label_y: str ='Data2', title: str ='Title', x_axis_data: list = [1,2,3,4,5], y_axis_data: list = [1,2,3,6,7], size_of_plots: list = [30], plot_color: list = ['Red'], chart_file_type: str = 'pdf'):
    try:
        filename = datetime.now().strftime('%Y-%m-%d__%H%M%S') + '__Graph.'
        # File logging operation
        row_file = (filename)
        row_data = [(row_file + chart_file_type), datetime.now().strftime('%Y-%m-%d__%H:%M:%S')]

        if not os.path.exists('logs.csv'):
            clear_logs()
        with open ('logs.csv', 'a') as file:
            writer_obj = writer(file)
            writer_obj.writerow(row_data)
        # File logging operation - Can be removed without drastic effects

        plt.xlabel(data_label_x)
        plt.xlabel(data_label_y)
        plt.title(title)

        X_Y_Spline = make_interp_spline(np.array(x_axis_data), np.array(y_axis_data))
        X_ = np.linspace(np.array(x_axis_data).min(), np.array(x_axis_data).max(), 500)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_, Y_)
        plt.savefig(filename + chart_file_type)
        plt.show()
        return None
    except Exception as e:
        print('Exception occurred : ', e)
        return 1

import chartFunctions

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
    1 and error message in the case of failure
'''
print(chartFunctions.show_graph([30,30]))
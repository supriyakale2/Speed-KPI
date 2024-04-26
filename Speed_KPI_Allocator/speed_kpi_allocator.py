import pandas as pd
import os
import time
# import speed_kpi_main as sp_main
start = time.time()
import speed_kpi_main as sp_main

#
# df = pd.DataFrame()
# # read the input file
# # filename = "galar.xlsx"
# # filename = "saga.xlsx"
# filename = "NORVE.xlsx"
# # filename = "S26 & S24_input_file.xlsx"
# # filename = "TUNGSTEN_MANGETTI-1X.xlsx"
#
# pathname = "C:/Users/Supriya/Desktop/Supriya/"
# # data = pd.read_excel(pathname+filename, sheet_name="slip and cut - S24")
# data = pd.read_excel(pathname+filename, sheet_name = "Sheet1")
# # add the data from the input file to the empty dataframe
# df = df._append(data)
# # apply the function to the dataframe
# columns_to_set_none = ["Speed KPI", "Speed KPI Cat"]
# df.loc[:, columns_to_set_none] = None
#
# # apply function for each row
# # axis=1 specifies that the function should be applied to each row of the DataFrame
# df.apply(lambda row: sp_main.assign_speed_kpi(row, df), axis=1)
#
#
# # write the dataframe to an output file
# df.to_excel(pathname+'Output_'+filename)
#
# print('It took', time.time() - start, 'seconds.')


master_df = pd.DataFrame()
def get_ddr(ddr_file_name):
    global data
    # read the input file
    ddr_file_path = pathname + ddr_file_name
    data = pd.read_excel(ddr_file_path, sheet_name='Sheet1')
    # data = pd.read_excel(ddr_file_path, sheet_name="drill out shoetrack - S26")
    # data_list.append(input_file)
    # data = pd.concat(data_list, ignore_index=True)
    # data.apply(lambda row: sp_main.assign_speed_kpi(row, df), axis=1)
    return data
#
#
def kpi_parser(row):
    sp_main.assign_speed_kpi(row, data)
    return
#
#
def kpi_allocator(ddr_file_name):
    final_output_df = get_ddr(ddr_file_name)
    columns_to_set_none = ["Speed KPI", "Speed KPI Cat"]
    final_output_df.loc[:, columns_to_set_none] = None
    final_output_df.apply(kpi_parser, axis=1)
    return final_output_df

#
#
# ####################################################################
#
#
if __name__ == '__main__':
    # filename = "S26 & S24_input_file"
    # filename = "input.xlsx"
    # filename = "galar.xlsx"
    # filename = "NATT-NNM-206.xlsx"
    # filename = "P5-NNM-503.xlsx"
    filename = "Soehanah_mg-04.xlsx"
    # filename = "Soehanah_wb_h-01.xlsx"
    # filename = "skald-swt-75a.xlsx"
    # filename = "TUNGSTEN_MANGETTI-1X.xlsx"
    # filename = "aquamarine-DC-19.xlsx"
    pathname = "C:/Users/Supriya/Desktop/Supriya/"
    data = kpi_allocator(filename)
    data.to_excel(pathname+'Output_'+filename)
    print("Output dataframe saved locally in an Excel file.")
    print('It took', time.time() - start, 'seconds.')


# ####################################################################

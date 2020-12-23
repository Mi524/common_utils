import re 

config_table_name = 'process_config-All sources(Others).xlsx'


sheet_name = re.sub(pattern='(.*)(\.xlsx|\.csv|.xls)', repl='\g<1>', string=config_table_name)
sheet_name = re.split('[_\-]',sheet_name)[-1]

print(sheet_name)
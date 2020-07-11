import ownproject
import pandas as pd

message = ownproject.updated_new_df
str_df = pd.DataFrame(message)
strt_df_conv=str_df.to_string()
